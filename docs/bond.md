# 债券数据

## 可转债实时行情

### bond_zh_hs_cov_spot

描述：可转债实时行情

输入参数：无

输出参数：代码、名称、最新价、涨跌幅 等

```python
import akshare as ak
df = ak.bond_zh_hs_cov_spot()
```

---

## 可转债历史行情

### bond_zh_hs_cov_daily

描述：可转债历史行情数据

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 可转债代码，如 "sz128039" (需带市场前缀 sh/sz) |

```python
import akshare as ak
df = ak.bond_zh_hs_cov_daily(symbol="sz128039")
```

---

## 可转债强赎

### bond_cb_redeem_jsl

描述：集思录-可转债强赎数据

输入参数：无

```python
import akshare as ak
df = ak.bond_cb_redeem_jsl()
```

---

## 债券查询

### bond_info_cm

描述：中国外汇交易中心-债券信息查询

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| bond_name | str | 债券名称（可为空） |
| bond_code | str | 债券代码（可为空） |
| bond_type | str | 债券类型，如 "短期融资券"（可为空） |
| issue_year | str | 发行年份，如 "2024"（可为空） |

```python
import akshare as ak
df = ak.bond_info_cm(bond_name="", bond_type="短期融资券", issue_year="2024")
```

---

## 国债收益率

### bond_zh_us_rate

描述：中国-美国国债收益率数据

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| start_date | str | "20240101" |

输出参数：日期、中国国债2Y/5Y/10Y/30Y、美国国债2Y/5Y/10Y/30Y 等

```python
import akshare as ak
df = ak.bond_zh_us_rate(start_date="20240101")
```

---

## 中国债券收益率曲线

### bond_china_yield

描述：中国债券信息网-国债收益率曲线

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| date | str | "20241220" |

```python
import akshare as ak
df = ak.bond_china_yield(date="20241220")
```

---

## 可转债基本信息

### bond_cb_profile_sina

描述：新浪-可转债详细信息

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 可转债代码，如 "128039" |

```python
import akshare as ak
df = ak.bond_cb_profile_sina(symbol="128039")
```

---

## 债券市场概览

### bond_deal_summary_sse

描述：上交所-债券成交概览

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| date | str | 日期，如 "20241220" |

```python
import akshare as ak
df = ak.bond_deal_summary_sse(date="20241220")
```
