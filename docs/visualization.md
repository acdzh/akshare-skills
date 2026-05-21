# 可视化图表模板

当需要生成图表辅助分析时，使用 matplotlib 绘图并保存为图片文件供用户查看。

## 环境准备

```python
import matplotlib
matplotlib.use('Agg')  # 无头模式，不需要 GUI
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']  # 中文字体
plt.rcParams['axes.unicode_minus'] = False  # 负号显示
```

---

## K线图 + 均线

```python
import akshare as ak
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# 获取数据
today = datetime.now().strftime('%Y%m%d')
start = (datetime.now() - timedelta(days=180)).strftime('%Y%m%d')
df = ak.stock_zh_a_hist(symbol="600519", period="daily", start_date=start, end_date=today, adjust="qfq")
df['日期'] = pd.to_datetime(df['日期'])
df['MA5'] = df['收盘'].rolling(5).mean()
df['MA20'] = df['收盘'].rolling(20).mean()
df['MA60'] = df['收盘'].rolling(60).mean()

# 绘图
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 8), height_ratios=[3, 1], sharex=True)

# 上图：价格 + 均线
ax1.plot(df['日期'], df['收盘'], label='收盘价', linewidth=1.5, color='black')
ax1.plot(df['日期'], df['MA5'], label='MA5', linewidth=0.8, color='orange')
ax1.plot(df['日期'], df['MA20'], label='MA20', linewidth=0.8, color='blue')
ax1.plot(df['日期'], df['MA60'], label='MA60', linewidth=0.8, color='purple')
ax1.set_title('贵州茅台(600519) 日线走势', fontsize=14)
ax1.set_ylabel('价格(元)')
ax1.legend(loc='upper left')
ax1.grid(True, alpha=0.3)

# 下图：成交量
colors = ['red' if df['收盘'].iloc[i] >= df['开盘'].iloc[i] else 'green' for i in range(len(df))]
ax2.bar(df['日期'], df['成交量'] / 1e4, color=colors, width=0.8, alpha=0.7)
ax2.set_ylabel('成交量(万手)')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/tmp/stock_kline.png', dpi=150, bbox_inches='tight')
plt.close()
print("图表已保存: /tmp/stock_kline.png")
```

---

## K线图 + MACD

```python
import akshare as ak
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

today = datetime.now().strftime('%Y%m%d')
start = (datetime.now() - timedelta(days=180)).strftime('%Y%m%d')
df = ak.stock_zh_a_hist(symbol="600519", period="daily", start_date=start, end_date=today, adjust="qfq")
df['日期'] = pd.to_datetime(df['日期'])

# MACD
ema12 = df['收盘'].ewm(span=12, adjust=False).mean()
ema26 = df['收盘'].ewm(span=26, adjust=False).mean()
df['DIF'] = ema12 - ema26
df['DEA'] = df['DIF'].ewm(span=9, adjust=False).mean()
df['MACD'] = (df['DIF'] - df['DEA']) * 2

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 8), height_ratios=[2, 1], sharex=True)

# 价格
ax1.plot(df['日期'], df['收盘'], color='black', linewidth=1.2)
ax1.set_title('贵州茅台(600519) MACD分析', fontsize=14)
ax1.set_ylabel('价格(元)')
ax1.grid(True, alpha=0.3)

# MACD
ax2.plot(df['日期'], df['DIF'], label='DIF', color='blue', linewidth=1)
ax2.plot(df['日期'], df['DEA'], label='DEA', color='orange', linewidth=1)
colors = ['red' if v >= 0 else 'green' for v in df['MACD']]
ax2.bar(df['日期'], df['MACD'], color=colors, width=0.8, alpha=0.6)
ax2.axhline(y=0, color='gray', linewidth=0.5)
ax2.set_ylabel('MACD')
ax2.legend(loc='upper left')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/tmp/stock_macd.png', dpi=150, bbox_inches='tight')
plt.close()
print("图表已保存: /tmp/stock_macd.png")
```

---

## 多股对比走势

```python
import akshare as ak
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

today = datetime.now().strftime('%Y%m%d')
start = (datetime.now() - timedelta(days=365)).strftime('%Y%m%d')

stocks = {"600519": "贵州茅台", "000858": "五粮液", "000568": "泸州老窖"}
fig, ax = plt.subplots(figsize=(14, 6))

for code, name in stocks.items():
    df = ak.stock_zh_a_hist(symbol=code, period="daily", start_date=start, end_date=today, adjust="qfq")
    df['日期'] = pd.to_datetime(df['日期'])
    # 归一化（以起始日为100）
    df['归一化'] = df['收盘'] / df['收盘'].iloc[0] * 100
    ax.plot(df['日期'], df['归一化'], label=name, linewidth=1.2)

ax.axhline(y=100, color='gray', linewidth=0.5, linestyle='--')
ax.set_title('白酒三巨头 年度走势对比（归一化）', fontsize=14)
ax.set_ylabel('归一化价格（起始=100）')
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/tmp/stock_compare.png', dpi=150, bbox_inches='tight')
plt.close()
print("图表已保存: /tmp/stock_compare.png")
```

---

## 行业估值分布

```python
import akshare as ak
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# 获取行业板块数据
df = ak.stock_board_industry_spot_em()
df = df[df['市盈率'] > 0]  # 排除负值

fig, ax = plt.subplots(figsize=(14, 6))
df_sorted = df.sort_values('市盈率').head(30)
bars = ax.barh(df_sorted['板块名称'], df_sorted['市盈率'], color='steelblue', alpha=0.7)
ax.set_xlabel('市盈率(PE)')
ax.set_title('行业板块 PE 估值分布（前30低估值行业）', fontsize=14)
ax.grid(True, alpha=0.3, axis='x')

plt.tight_layout()
plt.savefig('/tmp/industry_pe.png', dpi=150, bbox_inches='tight')
plt.close()
print("图表已保存: /tmp/industry_pe.png")
```

---

## 布林带图

```python
import akshare as ak
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

today = datetime.now().strftime('%Y%m%d')
start = (datetime.now() - timedelta(days=120)).strftime('%Y%m%d')
df = ak.stock_zh_a_hist(symbol="600519", period="daily", start_date=start, end_date=today, adjust="qfq")
df['日期'] = pd.to_datetime(df['日期'])

# 布林带
df['MID'] = df['收盘'].rolling(20).mean()
std = df['收盘'].rolling(20).std()
df['UP'] = df['MID'] + 2 * std
df['LOW'] = df['MID'] - 2 * std

fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(df['日期'], df['收盘'], label='收盘价', color='black', linewidth=1.2)
ax.plot(df['日期'], df['MID'], label='中轨(MA20)', color='blue', linewidth=0.8)
ax.plot(df['日期'], df['UP'], label='上轨', color='red', linewidth=0.8, linestyle='--')
ax.plot(df['日期'], df['LOW'], label='下轨', color='green', linewidth=0.8, linestyle='--')
ax.fill_between(df['日期'], df['UP'], df['LOW'], alpha=0.1, color='blue')
ax.set_title('贵州茅台(600519) 布林带', fontsize=14)
ax.set_ylabel('价格(元)')
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/tmp/stock_bollinger.png', dpi=150, bbox_inches='tight')
plt.close()
print("图表已保存: /tmp/stock_bollinger.png")
```

---

## 资金流向热力图

```python
import akshare as ak
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# 行业板块涨跌幅
df = ak.stock_board_industry_spot_em()
df = df.sort_values('涨跌幅', ascending=False).head(20)

fig, ax = plt.subplots(figsize=(14, 6))
colors = ['red' if v >= 0 else 'green' for v in df['涨跌幅']]
ax.barh(df['板块名称'], df['涨跌幅'], color=colors, alpha=0.7)
ax.axvline(x=0, color='gray', linewidth=0.5)
ax.set_xlabel('涨跌幅(%)')
ax.set_title('今日行业板块涨跌幅 TOP 20', fontsize=14)
ax.grid(True, alpha=0.3, axis='x')

plt.tight_layout()
plt.savefig('/tmp/sector_heatmap.png', dpi=150, bbox_inches='tight')
plt.close()
print("图表已保存: /tmp/sector_heatmap.png")
```

---

## 使用规范

1. **始终使用 `matplotlib.use('Agg')`**：避免在无 GUI 环境报错
2. **保存路径**：统一保存到 `/tmp/` 目录，文件名体现内容
3. **中文字体**：设置 `plt.rcParams['font.sans-serif']` 确保中文正常显示
4. **图片大小**：宽度 14 英寸，DPI 150，保证清晰度
5. **打印路径**：生成后 `print` 文件路径，告诉用户去哪里查看
6. **plt.close()**：绑图后关闭，释放内存
