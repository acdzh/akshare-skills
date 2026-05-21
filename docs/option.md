# 期权数据

## 期权交易所

| 交易所 | 代码 | 品种类型 |
|--------|------|----------|
| 上海证券交易所 | SSE | ETF期权（50ETF、300ETF等） |
| 深圳证券交易所 | SZSE | ETF期权（300ETF、创业板ETF等） |
| 中国金融期货交易所 | CFFEX | 股指期权（沪深300、中证1000等） |
| 上海期货交易所 | SHFE | 商品期权（铜、铝、黄金、白银、螺纹钢等） |
| 大连商品交易所 | DCE | 商品期权（铁矿石、豆粕、玉米等） |
| 郑州商品交易所 | CZCE | 商品期权（白糖、棉花、甲醇、PTA等） |
| 广州期货交易所 | GFEX | 商品期权（工业硅、碳酸锂等） |

---

## ETF 期权实时行情

### option_current_em

描述：东方财富-ETF 期权实时行情

输入参数：无

```python
import akshare as ak
df = ak.option_current_em()
```

---

## 期权合约信息

### option_sse_list_sina

描述：新浪-上交所期权合约列表

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | "50ETF"/"300ETF" |
| exchange | str | "null" |

```python
import akshare as ak
df = ak.option_sse_list_sina(symbol="50ETF", exchange="null")
```

---

## 期权历史行情

### option_hist_em

描述：东方财富-期权历史行情

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 期权合约代码 |

```python
import akshare as ak
df = ak.option_hist_em(symbol="10007830")
```

---

## 期权 Greeks

### option_risk_indicator_sse

描述：上交所-期权风险指标（Greeks）

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| date | str | 日期，如 "20241220" |

```python
import akshare as ak
df = ak.option_risk_indicator_sse(date="20241220")
```

---

## 商品期权行情

### option_dce_daily

描述：大商所-商品期权每日行情

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 品种代码，如 "m"(豆粕) |
| trade_date | str | "20241220" |

```python
import akshare as ak
df = ak.option_dce_daily(symbol="m", trade_date="20241220")
```

### option_czce_daily

描述：郑商所-商品期权每日行情

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 品种代码，如 "SR"(白糖) |
| trade_date | str | "20241220" |

```python
import akshare as ak
df = ak.option_czce_daily(symbol="SR", trade_date="20241220")
```

---

## 股指期权

### option_cffex_hs300_spot_sina

描述：新浪-沪深300股指期权实时行情

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 合约月份，如 "2412" |

```python
import akshare as ak
df = ak.option_cffex_hs300_spot_sina(symbol="2412")
```
