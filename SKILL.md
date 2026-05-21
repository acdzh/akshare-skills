---
name: "akshare"
description: "Use akshare to fetch Chinese financial data via Python for investment analysis. 当用户提问涉及股票行情、基金净值、期货、宏观经济、指数走势、债券利率、技术分析、基本面分析、消息面分析等投资类问题时调用。"
keywords: "akshare, finance, investment, data analysis, stock, fund, futures, macro economy, indices, bonds, option, fx, bank, energy, interest rate, spot, currency, 股票, 基金, 期货, 宏观经济, 指数, 债券, 期权, 外汇, 银行, 能源, 利率, 现货, 数字货币, 大A, 港股, 美股, 技术分析, 基本面分析, 消息面, K线, 均线, MACD, RSI, KDJ, 布林带, 量价分析, 财务分析, 估值, PE, PB, ROE, 行业分析, 板块, 概念股, 热门股, 龙虎榜, 资金流向, 机构评级, 研报, 涨跌幅, 市盈率, 市净率, 净利润, 营收, 毛利率, GDP, CPI, PMI, LPR, 上证指数, 沪深300, 创业板, 科创板"
---

# AKShare 金融数据分析

当用户咨询投资类问题（如股票行情、基金净值、期货数据、宏观经济指标、指数走势、债券利率等）时，编写一次性 Python 代码调用 [AKShare](https://github.com/akfamily/akshare) 获取数据并进行分析，然后结合分析结果回答用户问题。

## 核心工作流

1. **理解用户问题** → 判断需要哪些金融数据（参考下方"常见问题路由"）
2. **查阅文档** → 优先查阅 `docs/` 目录下的二级文档（见下方"查阅文档"章节）
3. **编写 Python 代码** → 编写一次性脚本调用 akshare 获取数据
4. **执行代码** → 在终端运行脚本，获取输出
5. **分析结果** → 基于数据给出专业的投资分析回答

## 常见问题路由

根据用户问题快速定位应查阅的文档：

| 用户问题类型 | 查阅文档 |
|-------------|----------|
| "帮我看看XX股票" / "XX现在多少钱" | `docs/stock.md` |
| "XX技术面怎么样" / "均线/MACD/KDJ分析" | `docs/technical_analysis.md` |
| "XX基本面如何" / "财报/PE/ROE" | `docs/fundamental_analysis.md` |
| "XX最近有什么消息" / "市场热度" | `docs/news_sentiment.md` |
| "大盘怎么样" / "上证/沪深300走势" | `docs/index.md` |
| "XX基金怎么样" / "基金排行/净值" | `docs/fund.md` |
| "GDP/CPI/PMI数据" / "经济形势" | `docs/macro.md` |
| "XX期货行情" / "螺纹钢/黄金期货" | `docs/futures.md` |
| "可转债" / "国债收益率" | `docs/bond.md` |
| "XX期权" / "隐含波动率" | `docs/option.md` |
| "汇率" / "美元/人民币" | `docs/fx.md` |
| "油价" / "碳交易" | `docs/energy.md` |
| "LPR" / "SHIBOR" / "利率走势" | `docs/interest_rate.md` |
| "黄金现货" / "白银价格" | `docs/spot.md` |
| "比特币" / "数字货币" | `docs/currency.md` |
| "综合分析XX" / "全面分析" | 组合多个文档（见"多源组合分析"） |
| "帮我选股" / "筛选条件" / "低估值/高成长" | `docs/stock_screening.md` |
| "画个图" / "走势图" / "K线图" | `docs/visualization.md` |

## 查阅文档

### 第一步：查阅 `docs/` 二级文档（优先）

`docs/` 目录包含各方向常用接口的精简文档，涵盖接口名、参数、示例，能满足绝大多数需求：

| 文件 | 内容 |
|------|------|
| `docs/stock.md` | A股/港股/美股行情、个股信息、财务数据、资金流向 |
| `docs/fund.md` | 公募基金（净值、ETF、LOF、排行、持仓、规模） |
| `docs/index.md` | 股票指数（实时行情、历史数据、成份股） |
| `docs/macro.md` | 宏观经济（GDP、CPI、PPI、PMI、货币、贸易、就业等） |
| `docs/futures.md` | 期货（实时行情、历史数据、主力合约、持仓、库存） |
| `docs/bond.md` | 债券（可转债、国债收益率、债券查询） |
| `docs/option.md` | 期权（ETF期权、商品期权、股指期权） |
| `docs/fx.md` | 外汇（实时行情、历史数据、人民币汇率） |
| `docs/energy.md` | 能源（油价、碳排放、天然气） |
| `docs/bank.md` | 银行（理财产品、同业拆借） |
| `docs/interest_rate.md` | 利率（LPR、SHIBOR、存款准备金率、国债收益率） |
| `docs/spot.md` | 现货（黄金白银、大宗商品） |
| `docs/currency.md` | 数字货币（实时行情、历史数据） |
| `docs/technical_analysis.md` | 技术分析（均线、MACD、RSI、KDJ、布林带、量价、趋势判断） |
| `docs/fundamental_analysis.md` | 基本面分析（财务指标、三大报表、估值、行业对比、机构持仓） |
| `docs/news_sentiment.md` | 消息面分析（个股新闻、热度排名、千股千评、板块资金流向、概念异动） |
| `docs/stock_screening.md` | 量化选股（多条件筛选、技术面选股、板块轮动、龙虎榜） |
| `docs/visualization.md` | 可视化图表（K线图、MACD图、多股对比、布林带、行业估值分布） |

**查阅方法**：根据用户问题类别，用 Read 工具读取对应的 `docs/` 文件，找到具体的接口名称、参数和示例代码。

### 第二步：查阅 `akshare_docs/` 原始文档（仅在需要时）

如果 `docs/` 中的信息不够（如需要冷门接口、确认参数细节、查看完整输出字段），再去 `akshare_docs/data/` 查阅原始文档：

| 目录 | 内容 |
|------|------|
| `akshare_docs/data/stock/stock.md` | A股/港股/美股完整接口（非常长） |
| `akshare_docs/data/fund/fund_public.md` | 公募基金完整接口 |
| `akshare_docs/data/fund/fund_private.md` | 私募基金数据 |
| `akshare_docs/data/index/index.md` | 指数完整接口 |
| `akshare_docs/data/bond/bond.md` | 债券完整接口 |
| `akshare_docs/data/futures/futures.md` | 期货完整接口 |
| `akshare_docs/data/option/option.md` | 期权完整接口 |
| `akshare_docs/data/macro/macro.md` | 宏观经济完整接口 |
| `akshare_docs/data/fx/fx.md` | 外汇完整接口 |
| `akshare_docs/data/bank/bank.md` | 银行完整接口 |
| `akshare_docs/data/energy/energy.md` | 能源完整接口 |
| `akshare_docs/data/interest_rate/interest_rate.md` | 利率完整接口 |
| `akshare_docs/data/spot/spot.md` | 现货完整接口 |
| `akshare_docs/data/currency/currency.md` | 数字货币完整接口 |
| `akshare_docs/data/others/others.md` | 其他数据 |

**注意**：原始文档内容很长，建议用 Grep 工具搜索具体接口名，而非从头阅读。

### 第三步：通过反射从 akshare 库直接获取文档和参数

当文档信息不确定或需要验证时，可以直接从 akshare 库获取接口签名和文档：

```python
import akshare as ak
import inspect

# 查看接口的函数签名（参数名、默认值）
print(inspect.signature(ak.stock_zh_a_hist))
# 输出: (symbol='000001', period='daily', start_date='19700101', end_date='22220101', adjust='')

# 查看接口的 docstring 文档
print(ak.stock_zh_a_hist.__doc__)

# 列出 akshare 中所有可用接口（按关键词搜索）
all_funcs = [name for name in dir(ak) if not name.startswith('_')]
# 搜索包含 "fund" 的接口
fund_funcs = [f for f in all_funcs if 'fund' in f.lower()]
print(fund_funcs)

# 获取接口源码（查看实现细节）
print(inspect.getsource(ak.stock_zh_a_hist))
```

**适用场景**：
- 确认某接口是否存在（接口可能已更名或移除）
- 查看参数默认值和完整签名
- 按关键词搜索可用接口名
- 文档和实际接口不一致时以反射结果为准

## 编写代码规范

### 基本模板

```python
import akshare as ak
import pandas as pd

# 调用接口获取数据
df = ak.接口名称(参数=值)

# 数据处理与分析
# ... 根据需求进行筛选、计算、排序等

# 输出结果
print(df.to_string())  # 或 print 关键统计结果
```

### 重要规则

1. **始终使用 `python3` 执行脚本**
2. **每次编写独立的一次性脚本**，不依赖外部状态，如果需要在临时目录下创建文件，文件名应足够随机以避免重复覆盖。在编写 Python 文件前，你应当使用 Terminal 工具生成一个随机 uuid 作为 Python 文件的后缀。
3. **Python 脚本的唯一作用是获取数据**，因此输出不需要考虑人的阅读。不需要格式化输出，不需要进度条，格式化等等干扰输出。
4. **控制输出量**：数据量大时使用 `.head()`、`.tail()` 或筛选后再输出，避免输出过多行
5. **使用 pandas** 进行数据处理（akshare 返回的都是 DataFrame）
6. **处理日期格式**：akshare 的日期参数通常为字符串格式如 `"20240101"` 或 `"2024-01-01"`，具体看文档
7. **打印关键信息**而非整个 DataFrame：如统计指标、筛选结果、排序后的 Top N

### 常用分析模式

```python
# 获取实时行情并筛选
import akshare as ak
df = ak.stock_zh_a_spot_em()
target = df[df['名称'].str.contains('贵州茅台')]
print(target[['代码', '名称', '最新价', '涨跌幅', '成交额']].to_string(index=False))
```

```python
# 获取历史数据
import akshare as ak
df = ak.stock_zh_a_hist(symbol="600519", period="daily", start_date="20240101", end_date="20241231", adjust="qfq")
print(df[['日期', '收盘', '成交量']].tail(10).to_string(index=False))
```

更多分析模式参考 `docs/` 下的专题文档：
- 技术面分析 → `docs/technical_analysis.md`
- 基本面分析 → `docs/fundamental_analysis.md`
- 消息面分析 → `docs/news_sentiment.md`

## 执行方式

将代码写入临时文件后用 `python3` 执行：

```bash
python3 /tmp/akshare_analysis.py
```

## 错误处理

### 环境缺失

如果执行时报错 `ModuleNotFoundError: No module named 'akshare'`，提醒用户：

> 当前环境未安装 akshare，请执行以下命令安装：
> ```bash
> pip install akshare
> ```

如果报 `No module named 'pandas'`：

> 请安装 pandas：
> ```bash
> pip install pandas
> ```

### 接口调用失败

- **网络超时**：建议用户检查网络或稍后重试
- **参数错误**：回到文档确认参数格式，常见问题是日期格式不对
- **接口废弃**：akshare 更新频繁，某些接口可能已更名或移除。用反射（第三步）确认接口是否存在，或搜索替代接口

### 数据为空

如果返回的 DataFrame 为空，可能是：
- 日期参数不在交易日范围内
- 股票代码格式不正确（注意某些接口需要带交易所前缀如 `sh600519`，有些只需 `600519`）
- 市场休市中

### 数据质量注意事项

分析前需注意以下常见数据陷阱：

| 场景 | 问题 | 处理方式 |
|------|------|----------|
| 停牌股 | 历史数据缺失交易日，计算收益率会出错 | 检查 `len(df)` 是否合理，或排除停牌股 |
| 复权选择 | 不复权数据在除权日有跳空缺口，计算收益率失真 | 计算收益率/技术指标**必须用前复权**（`adjust="qfq"`） |
| 除权除息日 | 不复权数据当天出现大幅下跌假象 | 使用前复权数据消除影响 |
| ST 股票 | 涨跌停限制为 ±5%，与普通股 ±10% 不同 | 筛选时排除 ST（`~df['名称'].str.contains('ST')`） |
| 北交所/科创板 | 涨跌停为 ±30%（上市前5日不限涨跌），代码规则不同 | 注意代码前缀：科创板68开头，北交所8开头 |
| 新股上市 | 上市首日数据特殊（无涨跌幅限制），均线数据不足 | 获取历史数据时确保有足够交易日（如计算MA60需至少60日数据） |
| 周末/节假日 | 非交易日无数据 | 使用交易日日期，不要用自然日去逐日查询 |
| 收盘时间 | 实时行情接口在 15:00 收盘后数据才完整 | 盘中数据为实时快照，可能与最终收盘不同 |
| 财务数据滞后 | 季报有披露截止日：一季报4/30、中报8/31、三季报10/31、年报4/30 | 注意财务数据的报告期，不等于当前状况 |
| 总市值/流通市值 | 实时行情中的市值是基于最新价动态计算 | 如需历史市值，需用历史收盘价 × 股本 |

### 限流与频率控制

akshare 底层抓取数据源网站，频繁调用可能触发限流：
- 批量请求时在循环中加 `time.sleep(0.5)` 间隔
- 如遇 HTTP 403/503 错误，等待几秒后重试
- 单次脚本中避免超过 20 次 API 调用

## 实用技巧

### 动态日期处理

```python
from datetime import datetime, timedelta

today = datetime.now().strftime('%Y%m%d')
one_year_ago = (datetime.now() - timedelta(days=365)).strftime('%Y%m%d')
half_year_ago = (datetime.now() - timedelta(days=180)).strftime('%Y%m%d')

# 用于接口调用
df = ak.stock_zh_a_hist(symbol="600519", period="daily", start_date=one_year_ago, end_date=today, adjust="qfq")
```

### 版本检查

```python
import akshare as ak
print(f"akshare version: {ak.__version__}")
# 如果版本过旧，某些接口可能不可用，建议 pip install --upgrade akshare
```

### 异常处理模板

```python
import akshare as ak
import time

def safe_call(func, *args, retries=2, **kwargs):
    """带重试的安全调用"""
    for i in range(retries + 1):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if i < retries:
                time.sleep(2)
            else:
                print(f"调用失败: {e}")
                return None

df = safe_call(ak.stock_zh_a_hist, symbol="600519", period="daily", start_date="20240101", end_date="20241231", adjust="qfq")
```

## 回答规范

1. **先展示关键数据**，再给出分析结论
2. **量化支撑**：分析结论要有具体数字支撑
3. **风险提示**：涉及投资建议时，加上风险提示声明
4. **时效性说明**：说明数据的时间范围和更新时间
5. **推荐生成图表**：技术分析、趋势对比等场景应生成可视化图表辅助说明

### 图表与报告

**推荐在分析中生成图表**，将图片嵌入到 Markdown 报告中。工作流：

1. 用 matplotlib 生成图表保存到 `/tmp/` 目录
2. 输出 Markdown 报告时直接引用图片路径

```python
# 生成图表后，在报告中引用
chart_path = "/tmp/stock_600519_analysis.png"
# ... matplotlib 生成图表代码 ...
plt.savefig(chart_path, dpi=150, bbox_inches='tight')
plt.close()

# 输出 Markdown 报告（含图片引用）
report = f"""
## 贵州茅台(600519) 技术分析报告

### K线与均线走势
![K线走势图]({chart_path})

### 分析结论
- 均线多头排列，趋势向上
- MACD 零轴上方运行，动能充足
"""
print(report)
```

**适用场景**：
- 技术分析（K线 + 均线/MACD/布林带叠加）→ 比纯数字直观
- 多股走势对比 → 归一化折线图一目了然
- 行业估值分布 → 柱状图/散点图
- 资金流向 → 热力图/柱状图
- 详见 `docs/visualization.md` 中的完整模板

### 输出格式化

- **大数字**：总市值/成交额用"亿"为单位（`value / 1e8`），成交量用"万手"（`value / 1e4`）
- **百分比**：涨跌幅、收益率保留 2 位小数并带 % 号
- **表格输出**：对比多只股票或多个时间段时用表格，单只股票分析用分段文字
- **分段结构**：综合分析按「行情概览 → 技术面 → 基本面 → 消息面 → 综合结论」组织

```python
# 大数字格式化示例
print(f"总市值: {last['总市值']/1e8:.0f}亿")
print(f"成交额: {last['成交额']/1e8:.2f}亿")
print(f"涨跌幅: {last['涨跌幅']:.2f}%")
```

## 多源组合分析

当用户要求"综合分析"或"全面分析"某只股票时，需组合多个数据源。以下是推荐的组合模式：

### 个股综合分析模板

```python
import akshare as ak
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def comprehensive_analysis(symbol, name):
    """个股综合分析：行情 + 技术 + 基本面 + 消息面"""
    today = datetime.now().strftime('%Y%m%d')
    one_year_ago = (datetime.now() - timedelta(days=365)).strftime('%Y%m%d')

    print(f"{'='*50}")
    print(f"  {name}({symbol}) 综合分析报告")
    print(f"  数据日期: {datetime.now().strftime('%Y-%m-%d')}")
    print(f"{'='*50}\n")

    # ① 实时行情
    spot = ak.stock_zh_a_spot_em()
    stock = spot[spot['代码'] == symbol].iloc[0]
    print("【行情概览】")
    print(f"  最新价: {stock['最新价']:.2f}  涨跌幅: {stock['涨跌幅']:.2f}%")
    print(f"  总市值: {stock['总市值']/1e8:.0f}亿  换手率: {stock['换手率']:.2f}%")
    print(f"  PE(动态): {stock['市盈率-动态']:.2f}  PB: {stock['市净率']:.2f}")

    # ② 技术分析（近一年日线）
    df = ak.stock_zh_a_hist(symbol=symbol, period="daily", start_date=one_year_ago, end_date=today, adjust="qfq")
    df = df.sort_values('日期').reset_index(drop=True)
    for p in [5, 10, 20, 60]:
        df[f'MA{p}'] = df['收盘'].rolling(p).mean()
    ema12 = df['收盘'].ewm(span=12, adjust=False).mean()
    ema26 = df['收盘'].ewm(span=26, adjust=False).mean()
    df['DIF'] = ema12 - ema26
    df['DEA'] = df['DIF'].ewm(span=9, adjust=False).mean()
    last = df.iloc[-1]
    print(f"\n【技术面】")
    print(f"  MA5={last['MA5']:.2f} MA20={last['MA20']:.2f} MA60={last['MA60']:.2f}")
    if last['MA5'] > last['MA20'] > last['MA60']:
        print(f"  均线: 多头排列 ↑")
    elif last['MA5'] < last['MA20'] < last['MA60']:
        print(f"  均线: 空头排列 ↓")
    else:
        print(f"  均线: 震荡整理 →")
    print(f"  MACD: DIF={last['DIF']:.4f} DEA={last['DEA']:.4f}")

    # ③ 基本面（最近财务指标）
    try:
        fin = ak.stock_financial_analysis_indicator_em(symbol=f"{'SH' if symbol.startswith('6') else 'SZ'}{symbol}", indicator="按报告期")
        if not fin.empty:
            latest = fin.iloc[0]
            print(f"\n【基本面】({latest.get('REPORT_DATE_NAME', 'N/A')})")
            print(f"  营收增速: {latest.get('TOTALOPERATEREVETZ', 'N/A')}%")
            print(f"  净利润增速: {latest.get('PARENTNETPROFITTZ', 'N/A')}%")
            print(f"  ROE(加权): {latest.get('ROEJQ', 'N/A')}%")
            print(f"  毛利率: {latest.get('XSMLL', 'N/A')}%  净利率: {latest.get('XSJLL', 'N/A')}%")
    except Exception as e:
        print(f"\n【基本面】获取失败: {e}")

    # ④ 消息面（千股千评）
    try:
        comments = ak.stock_comment_em()
        sc = comments[comments['代码'] == symbol]
        if not sc.empty:
            row = sc.iloc[0]
            print(f"\n【消息面】")
            print(f"  综合得分: {row['综合得分']}  排名: {row['目前排名']}  机构参与度: {row['机构参与度']}")
    except Exception as e:
        print(f"\n【消息面】获取失败: {e}")

comprehensive_analysis("600519", "贵州茅台")
```

### 组合分析场景指引

| 用户需求 | 需要的数据组合 | 涉及文档 |
|----------|---------------|----------|
| 综合分析个股 | 行情 + 技术 + 财务 + 消息 | stock + technical_analysis + fundamental_analysis + news_sentiment |
| 行业对比 | 板块成份股 + 各股PE/PB/ROE | fundamental_analysis |
| 大盘趋势研判 | 指数行情 + 技术指标 + 宏观数据 + 资金流向 | index + technical_analysis + macro + news_sentiment |
| 基金筛选 | 基金列表 + 净值走势 + 持仓 + 规模 | fund |
| 可转债套利 | 可转债行情 + 正股行情 + 转股价值 | bond + stock |
| 宏观环境 | GDP/CPI/PMI + 利率 + 汇率 + 资金面 | macro + interest_rate + fx |
