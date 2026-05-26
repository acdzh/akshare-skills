# 技术分析

本文件服务于 3 类高频任务：

1. 判断标的是偏强、偏弱还是震荡。
2. 识别支撑位、阻力位和关键转折信号。
3. 为“个股综合分析”“指数研判”“筛选强势标的”提供趋势证据。

技术分析的目标不是堆指标，而是用少量高价值指标解释趋势、节奏和风险。

## 任务路由

| 任务 | 目标 | 优先数据 |
|------|------|----------|
| 趋势判断 | 看多头、空头或震荡结构 | 历史 K 线 + MA + MACD |
| 强弱判断 | 看动能是否延续 | MA + MACD + RSI |
| 拐点识别 | 看金叉、死叉、背离、放量突破 | MACD + 量价 + 支撑阻力 |
| 超买超卖 | 看短期是否过热或过冷 | RSI + KDJ + 布林带 |
| 技术面筛选 | 挑强势股、突破股、金叉股 | 历史 K 线 + MA + MACD + 成交量 |

## 推荐工作流

### 技术面单次判断

至少组合以下 4 类中的 2 到 3 类：

1. 趋势：MA/EMA
2. 动能：MACD
3. 强弱：RSI/KDJ
4. 量价：成交量、量均线、放量/缩量

### 默认分析顺序

1. 先看趋势是否向上、向下或震荡。
2. 再看 MACD 是否确认动能。
3. 再看 RSI/KDJ 是否处于过热或超卖区。
4. 最后看量价是否支持当前走势。

不要把单一金叉、单次超买或单日放量直接当成强结论。

## 数据获取

技术分析依赖历史 K 线，日线场景通常建议至少取 120 个交易日。

```python
import akshare as ak

df = ak.stock_zh_a_hist(
    symbol="600519",
    period="daily",
    start_date="20230101",
    end_date="20241231",
    adjust="qfq",
).sort_values("日期").reset_index(drop=True)
```

适用场景：

1. A 股：`stock_zh_a_hist`
2. 指数：`index_zh_a_hist`
3. ETF：`fund_etf_hist_em`

## 高频指标

### 均线系统（MA / EMA）

用途：判断趋势方向、均线排列和中短期支撑阻力。

```python
df["MA5"] = df["收盘"].rolling(5).mean()
df["MA10"] = df["收盘"].rolling(10).mean()
df["MA20"] = df["收盘"].rolling(20).mean()
df["MA60"] = df["收盘"].rolling(60).mean()

last = df.iloc[-1]
ma_bullish = last["MA5"] > last["MA10"] > last["MA20"] > last["MA60"]
ma_bearish = last["MA5"] < last["MA10"] < last["MA20"] < last["MA60"]
```

解读建议：

1. 多头排列通常说明趋势偏强。
2. 空头排列通常说明趋势偏弱。
3. 价格靠近 MA20 / MA60 时，常是观察支撑阻力的关键位置。

### MACD

用途：判断趋势动能和拐点确认。

```python
def calc_macd(close, fast=12, slow=26, signal=9):
    ema_fast = close.ewm(span=fast, adjust=False).mean()
    ema_slow = close.ewm(span=slow, adjust=False).mean()
    dif = ema_fast - ema_slow
    dea = dif.ewm(span=signal, adjust=False).mean()
    macd = (dif - dea) * 2
    return dif, dea, macd

df["DIF"], df["DEA"], df["MACD"] = calc_macd(df["收盘"])
```

解读建议：

1. `DIF` 上穿 `DEA` 是金叉，下穿是死叉。
2. 零轴上方金叉一般强于零轴下方金叉。
3. MACD 只能确认动能，不能单独证明趋势可持续。

### RSI

用途：判断短期强弱和超买超卖。

```python
def calc_rsi(close, period=14):
    delta = close.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.ewm(alpha=1 / period, min_periods=period).mean()
    avg_loss = loss.ewm(alpha=1 / period, min_periods=period).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

df["RSI6"] = calc_rsi(df["收盘"], 6)
df["RSI14"] = calc_rsi(df["收盘"], 14)
```

解读建议：

1. 高 RSI 不等于马上下跌，低 RSI 也不等于马上反转。
2. 更适合辅助判断短线是否过热或过冷。

### KDJ

用途：辅助识别短线超买超卖与节奏变化。

```python
import pandas as pd

def calc_kdj(high, low, close, n=9, m1=3, m2=3):
    lowest_low = low.rolling(window=n).min()
    highest_high = high.rolling(window=n).max()
    rsv = (close - lowest_low) / (highest_high - lowest_low) * 100
    k = pd.Series(index=close.index, dtype=float)
    d = pd.Series(index=close.index, dtype=float)
    k.iloc[n - 1] = 50
    d.iloc[n - 1] = 50
    for i in range(n, len(close)):
        k.iloc[i] = (m1 - 1) / m1 * k.iloc[i - 1] + 1 / m1 * rsv.iloc[i]
        d.iloc[i] = (m2 - 1) / m2 * d.iloc[i - 1] + 1 / m2 * k.iloc[i]
    j = 3 * k - 2 * d
    return k, d, j
```

解读建议：

1. 更偏短线，噪音通常大于均线和 MACD。
2. 适合做短节奏辅助，不适合独立做中线结论。

### 布林带

用途：判断波动收敛、扩张和价格是否偏离均值。

```python
def calc_bollinger(close, period=20, std_dev=2):
    middle = close.rolling(window=period).mean()
    std = close.rolling(window=period).std()
    upper = middle + std_dev * std
    lower = middle - std_dev * std
    return upper, middle, lower

df["BOLL_UP"], df["BOLL_MID"], df["BOLL_LOW"] = calc_bollinger(df["收盘"])
```

解读建议：

1. 带宽收窄常意味着临近变盘。
2. 突破上轨不必然见顶，跌破下轨也不必然见底。

### 成交量与量价

用途：确认走势质量，而不是只看价格本身。

```python
df["VOL_MA5"] = df["成交量"].rolling(5).mean()
df["VOL_MA20"] = df["成交量"].rolling(20).mean()

last = df.iloc[-1]
vol_amplify = last["成交量"] > last["VOL_MA5"] * 1.5
vol_shrink = last["成交量"] < last["VOL_MA5"] * 0.7
```

解读建议：

1. 放量上涨通常强于缩量上涨。
2. 放量下跌通常比缩量下跌更值得警惕。

## 支撑位与阻力位

```python
def find_support_resistance(df, window=60):
    recent = df.tail(window)
    support = recent.nsmallest(3, "最低")["最低"].tolist()
    resistance = recent.nlargest(3, "最高")["最高"].tolist()
    return support, resistance
```

使用建议：

1. 支撑和阻力不是精确到分的点位，更适合看区间。
2. 如果突破阻力同时放量，信号通常更强。

## 简化综合模板

```python
import akshare as ak

df = ak.stock_zh_a_hist(
    symbol="600519",
    period="daily",
    start_date="20240101",
    end_date="20251231",
    adjust="qfq",
).sort_values("日期").reset_index(drop=True)

for p in [5, 10, 20, 60]:
    df[f"MA{p}"] = df["收盘"].rolling(p).mean()

df["DIF"], df["DEA"], df["MACD"] = calc_macd(df["收盘"])
df["RSI14"] = calc_rsi(df["收盘"], 14)
df["VOL_MA5"] = df["成交量"].rolling(5).mean()

last = df.iloc[-1]
print({
    "date": last["日期"],
    "close": last["收盘"],
    "ma20": last["MA20"],
    "ma60": last["MA60"],
    "dif": last["DIF"],
    "dea": last["DEA"],
    "rsi14": last["RSI14"],
    "volume_ratio": last["成交量"] / last["VOL_MA5"],
})
```

## 结论输出建议

当用户问“技术面怎么看”时，建议按以下结构输出：

1. 一句话趋势判断
2. 趋势证据
3. 动能证据
4. 量价确认
5. 关键支撑和阻力
6. 失效条件

示例：

```text
结论：技术面偏强，但短线已有一定过热迹象。

核心证据：
1. 价格仍在 MA20 和 MA60 上方，均线结构偏多头。
2. MACD 位于零轴上方，动能仍在延续。
3. RSI 已接近高位，短线追高性价比下降。

关键位：
1. 下方先看 MA20 一带支撑。
2. 上方若放量突破前高，趋势有望继续强化。
```

## 常见坑

1. 不要只看一个指标。
2. 不要忽略时间周期，日线和周线结论可能不同。
3. 不要用不复权价格做中长期技术判断。
4. 不要把超买理解成“立刻下跌”。
5. 用户要的是趋势结论和关键位，不是技术指标百科。
