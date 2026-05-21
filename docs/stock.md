# 股票数据

## A股实时行情

### stock_zh_a_spot_em

描述：东方财富-沪深京 A 股实时行情数据

输入参数：无

输出参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| 代码 | object | 股票代码 |
| 名称 | object | 股票名称 |
| 最新价 | float64 | - |
| 涨跌幅 | float64 | 单位: % |
| 涨跌额 | float64 | - |
| 成交量 | float64 | 单位: 手 |
| 成交额 | float64 | 单位: 元 |
| 振幅 | float64 | 单位: % |
| 最高 | float64 | - |
| 最低 | float64 | - |
| 今开 | float64 | - |
| 昨收 | float64 | - |
| 量比 | float64 | - |
| 换手率 | float64 | 单位: % |
| 市盈率-动态 | float64 | - |
| 市净率 | float64 | - |
| 总市值 | float64 | 单位: 元 |
| 流通市值 | float64 | 单位: 元 |
| 60日涨跌幅 | float64 | 单位: % |
| 年初至今涨跌幅 | float64 | 单位: % |

```python
import akshare as ak
df = ak.stock_zh_a_spot_em()
```

---

## A股历史行情

### stock_zh_a_hist

描述：东方财富-沪深京 A 股历史行情数据（日/周/月频率）

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 股票代码，如 "600519"、"000001" |
| period | str | "daily"(日) / "weekly"(周) / "monthly"(月) |
| start_date | str | 开始日期，格式 "20240101" |
| end_date | str | 结束日期，格式 "20241231" |
| adjust | str | 复权：""(不复权) / "qfq"(前复权) / "hfq"(后复权) |

输出参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| 日期 | object | 交易日 |
| 股票代码 | object | - |
| 开盘 | float64 | - |
| 收盘 | float64 | - |
| 最高 | float64 | - |
| 最低 | float64 | - |
| 成交量 | int64 | 单位: 手 |
| 成交额 | float64 | 单位: 元 |
| 振幅 | float64 | 单位: % |
| 涨跌幅 | float64 | 单位: % |
| 涨跌额 | float64 | - |
| 换手率 | float64 | 单位: % |

```python
import akshare as ak
# 前复权日线
df = ak.stock_zh_a_hist(symbol="600519", period="daily", start_date="20240101", end_date="20241231", adjust="qfq")
```

---

## A股分钟级行情

### stock_zh_a_hist_min_em

描述：东方财富-A 股分钟级历史行情

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 股票代码，如 "000001" |
| period | str | "1"(1分钟) / "5" / "15" / "30" / "60" |
| start_date | str | "2024-01-01 09:30:00" |
| end_date | str | "2024-01-05 15:00:00" |
| adjust | str | ""(不复权) / "qfq" / "hfq" |

```python
import akshare as ak
df = ak.stock_zh_a_hist_min_em(symbol="000001", period="5", start_date="2024-01-01 09:30:00", end_date="2024-01-05 15:00:00", adjust="qfq")
```

---

## 个股基本信息

### stock_individual_info_em

描述：东方财富-个股基本信息（总市值、流通市值、行业、上市时间等）

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 股票代码，如 "000001" |

```python
import akshare as ak
df = ak.stock_individual_info_em(symbol="000001")
```

---

## 个股资金流向

### stock_individual_fund_flow

描述：东方财富-个股资金流向

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| stock | str | 股票代码，如 "600519" |
| market | str | "sh"(沪) / "sz"(深) |

```python
import akshare as ak
df = ak.stock_individual_fund_flow(stock="600519", market="sh")
```

### stock_individual_fund_flow_rank

描述：东方财富-个股资金流排名

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| indicator | str | "今日"/"3日"/"5日"/"10日" |

```python
import akshare as ak
df = ak.stock_individual_fund_flow_rank(indicator="今日")
```

---

## 财务数据

### stock_financial_analysis_indicator

描述：新浪财经-财务分析-财务指标

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 股票代码，如 "600519" |

```python
import akshare as ak
df = ak.stock_financial_analysis_indicator(symbol="600519")
```

### stock_financial_abstract

描述：东方财富-财务摘要

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 股票代码，如 "000001" |

```python
import akshare as ak
df = ak.stock_financial_abstract(symbol="000001")
```

---

## 港股

### stock_hk_spot_em

描述：东方财富-港股实时行情

输入参数：无

```python
import akshare as ak
df = ak.stock_hk_spot_em()
```

### stock_hk_hist

描述：东方财富-港股历史行情

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 港股代码，如 "00700"(腾讯) |
| period | str | "daily"/"weekly"/"monthly" |
| start_date | str | "20240101" |
| end_date | str | "20241231" |
| adjust | str | ""/"qfq"/"hfq" |

```python
import akshare as ak
df = ak.stock_hk_hist(symbol="00700", period="daily", start_date="20240101", end_date="20241231", adjust="qfq")
```

---

## 美股

### stock_us_spot_em

描述：东方财富-美股实时行情

输入参数：无

```python
import akshare as ak
df = ak.stock_us_spot_em()
```

### stock_us_hist

描述：东方财富-美股历史行情

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 美股代码，如 "105.AAPL"(需带市场前缀，可通过 stock_us_spot_em 获取) |
| period | str | "daily"/"weekly"/"monthly" |
| start_date | str | "20240101" |
| end_date | str | "20241231" |
| adjust | str | ""/"qfq"/"hfq" |

```python
import akshare as ak
df = ak.stock_us_hist(symbol="105.AAPL", period="daily", start_date="20240101", end_date="20241231", adjust="qfq")
```

---

## 股东数据

### stock_zh_a_gdhs

描述：A股股东户数

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 股票代码，如 "600519" |

```python
import akshare as ak
df = ak.stock_zh_a_gdhs(symbol="600519")
```

---

## ST 股票

### stock_zh_a_st_em

描述：东方财富-A 股 ST 板块实时行情

输入参数：无

```python
import akshare as ak
df = ak.stock_zh_a_st_em()
```

---

## 新股数据

### stock_zh_a_new_em

描述：东方财富-A 股新股实时行情

输入参数：无

```python
import akshare as ak
df = ak.stock_zh_a_new_em()
```
