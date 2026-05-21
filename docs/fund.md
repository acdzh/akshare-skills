# 基金数据

## 基金基本信息

### fund_name_em

描述：东方财富-天天基金-所有基金基本信息（代码、名称、类型）

输入参数：无

输出参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| 基金代码 | object | - |
| 拼音缩写 | object | - |
| 基金简称 | object | - |
| 基金类型 | object | 混合型/股票型/债券型等 |

```python
import akshare as ak
df = ak.fund_name_em()
```

---

## 开放基金净值与走势

### fund_open_fund_info_em

描述：东方财富-开放基金数据（净值走势、收益走势等）

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 基金代码，如 "110011" |
| indicator | str | "单位净值走势" / "累计净值走势" / "累计收益率走势" / "同类排名走势" / "同类排名百分比" / "分红送配详情" / "拆分详情" |

```python
import akshare as ak
# 获取累计净值走势
df = ak.fund_open_fund_info_em(symbol="110011", indicator="累计净值走势")
```

### fund_open_fund_daily_em

描述：东方财富-开放基金每日净值

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| fund_type | str | "全部"/"股票型"/"混合型"/"债券型"/"指数型"/"QDII"/"FOF" |

```python
import akshare as ak
df = ak.fund_open_fund_daily_em(fund_type="全部")
```

---

## ETF 数据

### fund_etf_spot_em

描述：东方财富-ETF 实时行情

输入参数：无

```python
import akshare as ak
df = ak.fund_etf_spot_em()
```

### fund_etf_hist_em

描述：东方财富-ETF 历史行情

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | ETF代码，如 "510300" |
| period | str | "daily"/"weekly"/"monthly" |
| start_date | str | "20240101" |
| end_date | str | "20241231" |
| adjust | str | ""/"qfq"/"hfq" |

```python
import akshare as ak
df = ak.fund_etf_hist_em(symbol="510300", period="daily", start_date="20240101", end_date="20241231", adjust="qfq")
```

### fund_etf_fund_daily_em

描述：东方财富-ETF 基金每日净值

输入参数：无

```python
import akshare as ak
df = ak.fund_etf_fund_daily_em()
```

### fund_etf_fund_info_em

描述：东方财富-单只 ETF 基金净值走势

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| fund | str | ETF基金代码 |
| start_date | str | "20240101" |
| end_date | str | "20241231" |

```python
import akshare as ak
df = ak.fund_etf_fund_info_em(fund="510300", start_date="20240101", end_date="20241231")
```

---

## LOF 基金

### fund_lof_spot_em

描述：东方财富-LOF 实时行情

输入参数：无

```python
import akshare as ak
df = ak.fund_lof_spot_em()
```

### fund_lof_hist_em

描述：东方财富-LOF 历史行情

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | LOF代码 |
| period | str | "daily"/"weekly"/"monthly" |
| start_date | str | "20240101" |
| end_date | str | "20241231" |
| adjust | str | ""/"qfq"/"hfq" |

```python
import akshare as ak
df = ak.fund_lof_hist_em(symbol="160119", period="daily", start_date="20240101", end_date="20241231", adjust="qfq")
```

---

## 基金排行

### fund_open_fund_rank_em

描述：东方财富-开放基金排行

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | "全部"/"股票型"/"混合型"/"债券型"/"指数型"/"QDII"/"FOF" |

```python
import akshare as ak
df = ak.fund_open_fund_rank_em(symbol="全部")
```

### fund_exchange_rank_em

描述：东方财富-场内基金排行

输入参数：无

```python
import akshare as ak
df = ak.fund_exchange_rank_em()
```

---

## 基金持仓

### fund_portfolio_hold_em

描述：东方财富-基金持仓（股票持仓）

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 基金代码，如 "110011" |
| date | str | 报告期，如 "2024"（年份） |

```python
import akshare as ak
df = ak.fund_portfolio_hold_em(symbol="110011", date="2024")
```

### fund_portfolio_bond_hold_em

描述：东方财富-基金持仓（债券持仓）

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 基金代码 |
| date | str | 报告期年份 |

```python
import akshare as ak
df = ak.fund_portfolio_bond_hold_em(symbol="110011", date="2024")
```

---

## 货币基金

### fund_money_fund_daily_em

描述：东方财富-货币型基金每日数据

输入参数：无

```python
import akshare as ak
df = ak.fund_money_fund_daily_em()
```

---

## 基金经理

### fund_manager_em

描述：东方财富-基金经理信息

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 基金代码 |

```python
import akshare as ak
df = ak.fund_manager_em(symbol="110011")
```

---

## 基金规模

### fund_aum_em

描述：东方财富-基金公司管理规模排名

输入参数：无

```python
import akshare as ak
df = ak.fund_aum_em()
```

### fund_scale_change_em

描述：东方财富-基金规模变动

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 基金代码 |

```python
import akshare as ak
df = ak.fund_scale_change_em(symbol="110011")
```

---

## 基金分红

### fund_fh_em

描述：东方财富-基金分红数据

输入参数：无

```python
import akshare as ak
df = ak.fund_fh_em()
```

---

## 基金评级

### fund_rating_all

描述：天天基金-基金评级（综合）

输入参数：无

```python
import akshare as ak
df = ak.fund_rating_all()
```

---

## 基金估值

### fund_value_estimation_em

描述：东方财富-基金估值（盘中实时估算净值）

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 基金代码 |

```python
import akshare as ak
df = ak.fund_value_estimation_em(symbol="110011")
```
