# 指数数据

## 指数实时行情

### stock_zh_index_spot_em

描述：东方财富-沪深京指数实时行情

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | "沪深重要指数"/"上证系列指数"/"深证系列指数"/"指数成份"/"中证系列指数" |

输出参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| 代码 | object | - |
| 名称 | object | - |
| 最新价 | float64 | - |
| 涨跌额 | float64 | - |
| 涨跌幅 | float64 | 单位: % |
| 成交量 | float64 | - |
| 成交额 | float64 | - |

```python
import akshare as ak
df = ak.stock_zh_index_spot_em(symbol="沪深重要指数")
```

---

## 指数历史行情

### index_zh_a_hist

描述：东方财富-A 股指数历史行情

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 指数代码，如 "000001"(上证指数)、"399001"(深证成指)、"399006"(创业板指) |
| period | str | "daily"/"weekly"/"monthly" |
| start_date | str | "20240101" |
| end_date | str | "20241231" |

输出参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| 日期 | object | - |
| 开盘 | float64 | - |
| 收盘 | float64 | - |
| 最高 | float64 | - |
| 最低 | float64 | - |
| 成交量 | int64 | - |
| 成交额 | float64 | - |
| 振幅 | float64 | 单位: % |
| 涨跌幅 | float64 | 单位: % |
| 涨跌额 | float64 | - |
| 换手率 | float64 | 单位: % |

```python
import akshare as ak
df = ak.index_zh_a_hist(symbol="000001", period="daily", start_date="20240101", end_date="20241231")
```

### stock_zh_index_daily

描述：新浪-股票指数历史数据（日频率）

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 指数代码，需带前缀如 "sh000001"(上证指数)、"sz399001"(深证成指) |

输出参数：date, open, high, low, close, volume

```python
import akshare as ak
df = ak.stock_zh_index_daily(symbol="sh000001")
```

---

## 常用指数代码

| 代码 | 名称 |
|------|------|
| 000001 | 上证指数 |
| 399001 | 深证成指 |
| 399006 | 创业板指 |
| 000300 | 沪深300 |
| 000016 | 上证50 |
| 000905 | 中证500 |
| 000852 | 中证1000 |
| 399303 | 国证2000 |

---

## 指数成份股

### index_stock_cons

描述：指数成份股列表

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 指数代码，如 "000300" |

```python
import akshare as ak
df = ak.index_stock_cons(symbol="000300")
```

### index_stock_cons_weight_csindex

描述：中证指数-指数成份股权重

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 指数代码，如 "000300" |
| start_date | str | "20240101" |

```python
import akshare as ak
df = ak.index_stock_cons_weight_csindex(symbol="000300", start_date="20240101")
```
