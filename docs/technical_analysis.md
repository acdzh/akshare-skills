# 技术指标数据

本文件仅说明技术指标计算所需的历史数据接口、常用字段和基础计算模板。

> 规则：优先使用非东方财富来源接口；若同主题只有东方财富可用，才将东方财富接口作为回退或兜底选择。

## 任务路由

| 数据需求 | 目标 | 优先数据 |
|------|------|----------|
| 均线 | 获取用于 MA/EMA 的历史收盘价 | `stock_zh_a_hist` / `index_zh_a_hist` / `fund_etf_hist_em` |
| MACD | 获取收盘价序列 | 同上 |
| RSI / KDJ | 获取收盘、最高、最低序列 | 同上 |
| 布林带 | 获取收盘价序列 | 同上 |
| 量价 | 获取成交量和价格序列 | 同上 |

## 数据获取

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

常用字段：`日期`、`开盘`、`收盘`、`最高`、`最低`、`成交量`、`成交额`

## 高频指标

### 均线系统（MA / EMA）

```python
df["MA5"] = df["收盘"].rolling(5).mean()
df["MA10"] = df["收盘"].rolling(10).mean()
df["MA20"] = df["收盘"].rolling(20).mean()
df["EMA12"] = df["收盘"].ewm(span=12, adjust=False).mean()
```

### MACD

```python
def calc_macd(close, fast=12, slow=26, signal=9):
    ema_fast = close.ewm(span=fast, adjust=False).mean()
    ema_slow = close.ewm(span=slow, adjust=False).mean()
    dif = ema_fast - ema_slow
    dea = dif.ewm(span=signal, adjust=False).mean()
    macd = (dif - dea) * 2
    return dif, dea, macd
```

### RSI

```python
def calc_rsi(close, period=14):
    delta = close.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.ewm(alpha=1 / period, min_periods=period).mean()
    avg_loss = loss.ewm(alpha=1 / period, min_periods=period).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))
```

### KDJ

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

### 布林带

```python
def calc_bollinger(close, period=20, std_dev=2):
    middle = close.rolling(window=period).mean()
    std = close.rolling(window=period).std()
    upper = middle + std_dev * std
    lower = middle - std_dev * std
    return upper, middle, lower
```

## 常见坑

1. 中长期指标优先使用前复权数据。
2. 样本长度不足时不要强算长周期指标。
3. 不同资产的字段名和交易日历可能不同。
4. 技术指标模板只提供计算方法，不包含解释模板。
