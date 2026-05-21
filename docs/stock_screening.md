# 量化选股与筛选策略

当用户需要按条件筛选股票、构建选股策略时，使用本文档中的模板。

## 基础：获取全市场数据

```python
import akshare as ak
import pandas as pd

# 全市场实时行情（含 PE/PB/市值/换手率等）
df = ak.stock_zh_a_spot_em()
print(f"全市场共 {len(df)} 只股票")
print(df.columns.tolist())  # 查看可用字段
```

---

## 多条件筛选模板

### 价值型选股（低估值 + 高盈利）

```python
import akshare as ak
import pandas as pd

df = ak.stock_zh_a_spot_em()

# 筛选条件
conditions = (
    (df['市盈率-动态'] > 0) & (df['市盈率-动态'] < 15) &  # PE < 15（盈利且低估）
    (df['市净率'] > 0) & (df['市净率'] < 2) &              # PB < 2
    (df['总市值'] > 100e8) &                                # 总市值 > 100亿
    (df['涨跌幅'] > -9.5) &                                 # 排除跌停
    (~df['名称'].str.contains('ST|退'))                      # 排除 ST 和退市股
)

result = df[conditions][['代码', '名称', '最新价', '涨跌幅', '市盈率-动态', '市净率', '总市值']]
result['总市值(亿)'] = result['总市值'] / 1e8
result = result.sort_values('市盈率-动态')
print(f"符合条件: {len(result)} 只")
print(result.head(20).to_string(index=False))
```

### 成长型选股（高增长 + 合理估值）

```python
import akshare as ak
import pandas as pd
import time

# 先获取全市场行情
spot = ak.stock_zh_a_spot_em()
# 筛选大市值（减少遍历量）
candidates = spot[(spot['总市值'] > 50e8) & (~spot['名称'].str.contains('ST|退'))].head(100)

results = []
for _, row in candidates.iterrows():
    try:
        symbol = f"{'SH' if row['代码'].startswith('6') else 'SZ'}{row['代码']}"
        fin = ak.stock_financial_analysis_indicator_em(symbol=symbol, indicator="按报告期")
        if fin.empty:
            continue
        latest = fin.iloc[0]
        revenue_growth = latest.get('TOTALOPERATEREVETZ', None)
        profit_growth = latest.get('PARENTNETPROFITTZ', None)
        roe = latest.get('ROEJQ', None)
        if revenue_growth and profit_growth and roe:
            if float(revenue_growth) > 20 and float(profit_growth) > 20 and float(roe) > 15:
                results.append({
                    '代码': row['代码'],
                    '名称': row['名称'],
                    '最新价': row['最新价'],
                    'PE': row['市盈率-动态'],
                    '营收增速%': revenue_growth,
                    '净利增速%': profit_growth,
                    'ROE%': roe,
                })
        time.sleep(0.3)  # 避免限流
    except:
        continue

print(f"成长型选股结果: {len(results)} 只")
print(pd.DataFrame(results).to_string(index=False))
```

### 动量型选股（强势股）

```python
import akshare as ak
import pandas as pd

df = ak.stock_zh_a_spot_em()

# 筛选条件：近期强势
conditions = (
    (df['涨跌幅'] > 3) &                    # 今日涨幅 > 3%
    (df['60日涨跌幅'] > 20) &                # 60日涨幅 > 20%
    (df['量比'] > 1.5) &                     # 放量
    (df['换手率'] > 3) & (df['换手率'] < 15) &  # 换手率适中
    (df['总市值'] > 30e8) &                  # 市值 > 30亿
    (~df['名称'].str.contains('ST|退'))
)

result = df[conditions][['代码', '名称', '最新价', '涨跌幅', '60日涨跌幅', '量比', '换手率', '总市值']]
result['总市值(亿)'] = result['总市值'] / 1e8
result = result.sort_values('60日涨跌幅', ascending=False)
print(f"动量选股: {len(result)} 只")
print(result.head(20).to_string(index=False))
```

### 低位放量选股（底部信号）

```python
import akshare as ak
import pandas as pd

df = ak.stock_zh_a_spot_em()

conditions = (
    (df['60日涨跌幅'] < -10) &               # 近60日跌幅超10%（低位）
    (df['涨跌幅'] > 2) &                     # 今日反弹 > 2%
    (df['量比'] > 2) &                       # 明显放量
    (df['总市值'] > 50e8) &
    (df['市盈率-动态'] > 0) & (df['市盈率-动态'] < 50) &
    (~df['名称'].str.contains('ST|退'))
)

result = df[conditions][['代码', '名称', '最新价', '涨跌幅', '60日涨跌幅', '量比', '换手率', '市盈率-动态']]
result = result.sort_values('量比', ascending=False)
print(f"低位放量: {len(result)} 只")
print(result.head(20).to_string(index=False))
```

---

## 技术面筛选

### 均线突破选股

```python
import akshare as ak
import pandas as pd
import time
from datetime import datetime, timedelta

today = datetime.now().strftime('%Y%m%d')
start = (datetime.now() - timedelta(days=120)).strftime('%Y%m%d')

# 先从实时行情中选候选（避免遍历太多）
spot = ak.stock_zh_a_spot_em()
candidates = spot[
    (spot['涨跌幅'] > 1) & (spot['涨跌幅'] < 7) &
    (spot['总市值'] > 50e8) &
    (~spot['名称'].str.contains('ST|退'))
].head(50)

breakout_stocks = []
for _, row in candidates.iterrows():
    try:
        df = ak.stock_zh_a_hist(symbol=row['代码'], period="daily", start_date=start, end_date=today, adjust="qfq")
        if len(df) < 60:
            continue
        df['MA20'] = df['收盘'].rolling(20).mean()
        df['MA60'] = df['收盘'].rolling(60).mean()
        last = df.iloc[-1]
        prev = df.iloc[-2]
        # 今日收盘突破20日均线，且在60日均线上方
        if (last['收盘'] > last['MA20'] and prev['收盘'] <= prev['MA20'] and last['收盘'] > last['MA60']):
            breakout_stocks.append({
                '代码': row['代码'],
                '名称': row['名称'],
                '收盘': last['收盘'],
                'MA20': round(last['MA20'], 2),
                'MA60': round(last['MA60'], 2),
            })
        time.sleep(0.3)
    except:
        continue

print(f"均线突破: {len(breakout_stocks)} 只")
print(pd.DataFrame(breakout_stocks).to_string(index=False))
```

### MACD 金叉选股

```python
import akshare as ak
import pandas as pd
import time
from datetime import datetime, timedelta

today = datetime.now().strftime('%Y%m%d')
start = (datetime.now() - timedelta(days=90)).strftime('%Y%m%d')

spot = ak.stock_zh_a_spot_em()
candidates = spot[
    (spot['总市值'] > 50e8) & (spot['涨跌幅'] > 0) &
    (~spot['名称'].str.contains('ST|退'))
].head(50)

golden_cross = []
for _, row in candidates.iterrows():
    try:
        df = ak.stock_zh_a_hist(symbol=row['代码'], period="daily", start_date=start, end_date=today, adjust="qfq")
        if len(df) < 35:
            continue
        ema12 = df['收盘'].ewm(span=12, adjust=False).mean()
        ema26 = df['收盘'].ewm(span=26, adjust=False).mean()
        dif = ema12 - ema26
        dea = dif.ewm(span=9, adjust=False).mean()
        # 今日金叉（DIF上穿DEA）
        if dif.iloc[-1] > dea.iloc[-1] and dif.iloc[-2] <= dea.iloc[-2]:
            golden_cross.append({
                '代码': row['代码'],
                '名称': row['名称'],
                '收盘': df['收盘'].iloc[-1],
                'DIF': round(dif.iloc[-1], 4),
                'DEA': round(dea.iloc[-1], 4),
            })
        time.sleep(0.3)
    except:
        continue

print(f"MACD金叉: {len(golden_cross)} 只")
print(pd.DataFrame(golden_cross).to_string(index=False))
```

---

## 板块轮动分析

```python
import akshare as ak
import pandas as pd

# 行业板块资金流向
df = ak.stock_sector_fund_flow_rank(indicator="今日", sector_type="行业资金流")
print("【今日行业资金流入 TOP 10】")
print(df.head(10).to_string(index=False))
print("\n【今日行业资金流出 TOP 10】")
print(df.tail(10).to_string(index=False))

# 概念板块涨幅排行
concepts = ak.stock_board_concept_spot_em()
print("\n【今日概念涨幅 TOP 10】")
print(concepts.sort_values('涨跌幅', ascending=False).head(10)[['板块名称', '涨跌幅', '总市值', '换手率']].to_string(index=False))
```

---

## 龙虎榜分析

### stock_lhb_detail_em

描述：东方财富-龙虎榜详情

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| start_date | str | "20241220" |
| end_date | str | "20241220" |

```python
import akshare as ak
df = ak.stock_lhb_detail_em(start_date="20241220", end_date="20241220")
print(df[['代码', '名称', '收盘价', '涨跌幅', '龙虎榜净买额', '龙虎榜买入额', '龙虎榜卖出额']].to_string(index=False))
```

### stock_lhb_stock_statistic_em

描述：东方财富-龙虎榜个股统计

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | "近一月"/"近三月"/"近六月"/"近一年" |

```python
import akshare as ak
df = ak.stock_lhb_stock_statistic_em(symbol="近一月")
print(df.head(20).to_string(index=False))
```

---

## 大单/主力资金

### stock_individual_fund_flow_rank

描述：东方财富-个股资金流排名

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| indicator | str | "今日"/"3日"/"5日"/"10日" |

```python
import akshare as ak
# 今日主力净流入 TOP
df = ak.stock_individual_fund_flow_rank(indicator="今日")
print("【主力净流入 TOP 20】")
print(df.sort_values('主力净流入-净额', ascending=False).head(20)[['代码', '名称', '最新价', '涨跌幅', '主力净流入-净额', '主力净流入-净占比']].to_string(index=False))
```

---

## 注意事项

1. **控制遍历数量**：全市场有 5000+ 只股票，不要逐一遍历获取历史数据，先用实时行情粗筛后再精选
2. **加限流间隔**：循环调用时加 `time.sleep(0.3~0.5)`
3. **排除异常股**：始终排除 ST、退市、停牌股（`~df['名称'].str.contains('ST|退')`）
4. **结果数量控制**：输出 TOP 10~30 即可，不要输出全部
5. **多因子组合**：单一指标噪音大，建议至少 2-3 个条件交叉验证
6. **回测验证**：筛选结果仅为当前快照，不代表未来表现，需回测验证
