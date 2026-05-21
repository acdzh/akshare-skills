# 技术分析

当用户提问涉及技术面分析（均线、MACD、RSI、KDJ、布林带、量价关系、形态分析等）时，基于 akshare 获取历史行情数据，使用 pandas/numpy 计算技术指标并给出分析结论。

## 数据获取

技术分析依赖历史 K 线数据，建议至少获取 120 个交易日：

```python
import akshare as ak
import pandas as pd
import numpy as np

# A股历史数据（前复权）
df = ak.stock_zh_a_hist(symbol="600519", period="daily", start_date="20230101", end_date="20241231", adjust="qfq")
df = df.sort_values('日期').reset_index(drop=True)

# 指数历史数据
df = ak.index_zh_a_hist(symbol="000001", period="daily", start_date="20230101", end_date="20241231")

# ETF 历史数据
df = ak.fund_etf_hist_em(symbol="510300", period="daily", start_date="20230101", end_date="20241231", adjust="qfq")

# 期货主力合约
df = ak.futures_main_sina(symbol="RB0", start_date="20230101", end_date="20241231")
```

---

## 均线系统（MA/EMA）

```python
# 简单移动平均线
df['MA5'] = df['收盘'].rolling(window=5).mean()
df['MA10'] = df['收盘'].rolling(window=10).mean()
df['MA20'] = df['收盘'].rolling(window=20).mean()
df['MA60'] = df['收盘'].rolling(window=60).mean()
df['MA120'] = df['收盘'].rolling(window=120).mean()

# 指数移动平均线
df['EMA12'] = df['收盘'].ewm(span=12, adjust=False).mean()
df['EMA26'] = df['收盘'].ewm(span=26, adjust=False).mean()

# 均线排列判断
last = df.iloc[-1]
ma_bullish = last['MA5'] > last['MA10'] > last['MA20'] > last['MA60']  # 多头排列
ma_bearish = last['MA5'] < last['MA10'] < last['MA20'] < last['MA60']  # 空头排列

# 金叉/死叉
df['MA5_cross_MA20'] = (df['MA5'] > df['MA20']) & (df['MA5'].shift(1) <= df['MA20'].shift(1))
df['MA5_death_MA20'] = (df['MA5'] < df['MA20']) & (df['MA5'].shift(1) >= df['MA20'].shift(1))
```

---

## MACD

```python
def calc_macd(close, fast=12, slow=26, signal=9):
    ema_fast = close.ewm(span=fast, adjust=False).mean()
    ema_slow = close.ewm(span=slow, adjust=False).mean()
    dif = ema_fast - ema_slow
    dea = dif.ewm(span=signal, adjust=False).mean()
    macd_hist = (dif - dea) * 2
    return dif, dea, macd_hist

df['DIF'], df['DEA'], df['MACD'] = calc_macd(df['收盘'])

# 信号判断
last, prev = df.iloc[-1], df.iloc[-2]
golden_cross = (last['DIF'] > last['DEA']) and (prev['DIF'] <= prev['DEA'])  # 金叉
death_cross = (last['DIF'] < last['DEA']) and (prev['DIF'] >= prev['DEA'])   # 死叉
above_zero = last['DIF'] > 0 and last['DEA'] > 0  # 零轴上方（强势区）
```

---

## RSI（相对强弱指标）

```python
def calc_rsi(close, period=14):
    delta = close.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.ewm(alpha=1/period, min_periods=period).mean()
    avg_loss = loss.ewm(alpha=1/period, min_periods=period).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

df['RSI6'] = calc_rsi(df['收盘'], 6)
df['RSI12'] = calc_rsi(df['收盘'], 12)
df['RSI24'] = calc_rsi(df['收盘'], 24)

# 超买(>80) / 超卖(<20) / 正常区间
```

---

## KDJ（随机指标）

```python
def calc_kdj(high, low, close, n=9, m1=3, m2=3):
    lowest_low = low.rolling(window=n).min()
    highest_high = high.rolling(window=n).max()
    rsv = (close - lowest_low) / (highest_high - lowest_low) * 100
    k = pd.Series(index=close.index, dtype=float)
    d = pd.Series(index=close.index, dtype=float)
    k.iloc[n-1] = 50
    d.iloc[n-1] = 50
    for i in range(n, len(close)):
        k.iloc[i] = (m1 - 1) / m1 * k.iloc[i-1] + 1 / m1 * rsv.iloc[i]
        d.iloc[i] = (m2 - 1) / m2 * d.iloc[i-1] + 1 / m2 * k.iloc[i]
    j = 3 * k - 2 * d
    return k, d, j

df['K'], df['D'], df['J'] = calc_kdj(df['最高'], df['最低'], df['收盘'])

# K>80且D>80 超买 / K<20且D<20 超卖
# K上穿D为金叉，K下穿D为死叉
```

---

## 布林带（Bollinger Bands）

```python
def calc_bollinger(close, period=20, std_dev=2):
    middle = close.rolling(window=period).mean()
    std = close.rolling(window=period).std()
    upper = middle + std_dev * std
    lower = middle - std_dev * std
    bandwidth = (upper - lower) / middle * 100
    percent_b = (close - lower) / (upper - lower)
    return upper, middle, lower, bandwidth, percent_b

df['BOLL_UP'], df['BOLL_MID'], df['BOLL_LOW'], df['BOLL_BW'], df['BOLL_PB'] = calc_bollinger(df['收盘'])

# 突破上轨 → 强势/超买
# 跌破下轨 → 弱势/超卖
# 带宽收窄 → 变盘信号
```

---

## 成交量分析

```python
# 量均线
df['VOL_MA5'] = df['成交量'].rolling(5).mean()
df['VOL_MA20'] = df['成交量'].rolling(20).mean()
df['量比'] = df['成交量'] / df['VOL_MA5']

# OBV（能量潮）
df['OBV'] = (np.sign(df['收盘'].diff()) * df['成交量']).fillna(0).cumsum()

# 量价判断
last = df.iloc[-1]
vol_amplify = last['成交量'] > last['VOL_MA5'] * 1.5  # 放量
vol_shrink = last['成交量'] < last['VOL_MA5'] * 0.7   # 缩量
```

---

## 支撑位与阻力位

```python
def find_support_resistance(df, window=60):
    recent = df.tail(window)
    resistance = recent.nlargest(3, '最高')['最高'].tolist()
    support = recent.nsmallest(3, '最低')['最低'].tolist()
    # 整数关口
    price = df['收盘'].iloc[-1]
    round_levels = [round(price / 10) * 10, round(price / 50) * 50]
    return support, resistance, round_levels
```

---

## 趋势综合判断

```python
def judge_trend(df):
    last = df.iloc[-1]
    signals = {}
    # 均线
    if last['MA5'] > last['MA20'] > last['MA60']:
        signals['均线'] = '多头排列'
    elif last['MA5'] < last['MA20'] < last['MA60']:
        signals['均线'] = '空头排列'
    else:
        signals['均线'] = '震荡整理'
    # MACD
    if last['DIF'] > 0 and last['DEA'] > 0 and last['MACD'] > 0:
        signals['MACD'] = '强势'
    elif last['DIF'] < 0 and last['DEA'] < 0 and last['MACD'] < 0:
        signals['MACD'] = '弱势'
    else:
        signals['MACD'] = '转折中'
    # RSI
    rsi = last['RSI6']
    if rsi > 80: signals['RSI'] = '超买'
    elif rsi < 20: signals['RSI'] = '超卖'
    elif rsi > 50: signals['RSI'] = '偏强'
    else: signals['RSI'] = '偏弱'
    # 量价
    if last['收盘'] > df['收盘'].iloc[-2] and last['成交量'] > last['VOL_MA5']:
        signals['量价'] = '放量上涨'
    elif last['收盘'] < df['收盘'].iloc[-2] and last['成交量'] > last['VOL_MA5']:
        signals['量价'] = '放量下跌'
    elif last['收盘'] > df['收盘'].iloc[-2]:
        signals['量价'] = '缩量上涨'
    else:
        signals['量价'] = '缩量下跌'
    return signals
```

---

## 综合技术分析模板

```python
import akshare as ak
import pandas as pd
import numpy as np

def full_technical_analysis(symbol, start_date, end_date):
    df = ak.stock_zh_a_hist(symbol=symbol, period="daily",
                            start_date=start_date, end_date=end_date, adjust="qfq")
    df = df.sort_values('日期').reset_index(drop=True)

    # 均线
    for p in [5, 10, 20, 60, 120]:
        df[f'MA{p}'] = df['收盘'].rolling(p).mean()
    # MACD
    ema12 = df['收盘'].ewm(span=12, adjust=False).mean()
    ema26 = df['收盘'].ewm(span=26, adjust=False).mean()
    df['DIF'] = ema12 - ema26
    df['DEA'] = df['DIF'].ewm(span=9, adjust=False).mean()
    df['MACD'] = (df['DIF'] - df['DEA']) * 2
    # RSI
    delta = df['收盘'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    df['RSI6'] = 100 - 100 / (1 + gain.ewm(alpha=1/6, min_periods=6).mean() / loss.ewm(alpha=1/6, min_periods=6).mean())
    # 布林带
    df['BOLL_MID'] = df['收盘'].rolling(20).mean()
    std = df['收盘'].rolling(20).std()
    df['BOLL_UP'] = df['BOLL_MID'] + 2 * std
    df['BOLL_LOW'] = df['BOLL_MID'] - 2 * std
    # 成交量
    df['VOL_MA5'] = df['成交量'].rolling(5).mean()

    last = df.iloc[-1]
    print(f"=== {symbol} 技术分析 ===")
    print(f"日期: {last['日期']}  收盘: {last['收盘']:.2f}")
    print(f"MA5={last['MA5']:.2f} MA20={last['MA20']:.2f} MA60={last['MA60']:.2f}")
    print(f"DIF={last['DIF']:.4f} DEA={last['DEA']:.4f} MACD={last['MACD']:.4f}")
    print(f"RSI6={last['RSI6']:.2f}")
    print(f"BOLL: {last['BOLL_LOW']:.2f} - {last['BOLL_MID']:.2f} - {last['BOLL_UP']:.2f}")
    print(f"量比: {last['成交量']/last['VOL_MA5']:.2f}")

full_technical_analysis("600519", "20240101", "20251231")
```

---

## 分析回答规范

1. **多指标交叉验证**：至少结合 2-3 个指标综合判断，不依赖单一指标
2. **明确参数**：说明所用指标的参数（RSI 周期、均线天数等）
3. **时间周期**：明确分析基于的 K 线周期（日线/周线/月线）
4. **信号强度**：区分强信号（多指标共振）和弱信号（单指标触发）
5. **风险提示**：技术分析有滞后性，需结合基本面和市场环境，不构成投资建议
