# 基本面分析

当用户提问涉及基本面分析（财务指标、估值、盈利能力、成长性、行业对比等）时，基于 akshare 获取财务数据并进行分析。

## 财务指标概览

### stock_financial_analysis_indicator_em

描述：东方财富-A股财务分析主要指标（最全面）

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 股票代码，如 "SH600519"（需带市场前缀 SH/SZ） |
| indicator | str | "按报告期" / "按单季度" |

关键输出字段：

| 字段 | 含义 |
|------|------|
| EPSJB | 基本每股收益(元) |
| EPSKCJB | 扣非每股收益(元) |
| BPS | 每股净资产(元) |
| MGJYXJJE | 每股经营现金流(元) |
| TOTALOPERATEREVE | 营业总收入(元) |
| PARENTNETPROFIT | 归属净利润(元) |
| TOTALOPERATEREVETZ | 营业总收入同比增长(%) |
| PARENTNETPROFITTZ | 归属净利润同比增长(%) |
| ROEJQ | 净资产收益率ROE(加权)(%) |
| XSJLL | 净利率(%) |
| XSMLL | 毛利率(%) |
| ZCFZL | 资产负债率(%) |
| LD | 流动比率 |
| SD | 速动比率 |
| ZZCZZTS | 总资产周转天数 |
| CHZZTS | 存货周转天数 |

```python
import akshare as ak
df = ak.stock_financial_analysis_indicator_em(symbol="SH600519", indicator="按报告期")
```

### stock_financial_analysis_indicator

描述：新浪财经-财务分析-财务指标

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 股票代码，如 "600519"（不带前缀） |

```python
import akshare as ak
df = ak.stock_financial_analysis_indicator(symbol="600519")
```

---

## 利润表

### stock_profit_sheet_by_report_em

描述：东方财富-利润表（按报告期）

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | "SH600519" |

```python
import akshare as ak
df = ak.stock_profit_sheet_by_report_em(symbol="SH600519")
```

### stock_profit_sheet_by_yearly_em

描述：东方财富-利润表（按年度）

```python
import akshare as ak
df = ak.stock_profit_sheet_by_yearly_em(symbol="SH600519")
```

### stock_profit_sheet_by_quarterly_em

描述：东方财富-利润表（按单季度）

```python
import akshare as ak
df = ak.stock_profit_sheet_by_quarterly_em(symbol="SH600519")
```

---

## 资产负债表

### stock_balance_sheet_by_report_em

描述：东方财富-资产负债表（按报告期）

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | "SH600519" |

```python
import akshare as ak
df = ak.stock_balance_sheet_by_report_em(symbol="SH600519")
```

### stock_balance_sheet_by_yearly_em

描述：东方财富-资产负债表（按年度）

```python
import akshare as ak
df = ak.stock_balance_sheet_by_yearly_em(symbol="SH600519")
```

---

## 现金流量表

### stock_cash_flow_sheet_by_report_em

描述：东方财富-现金流量表（按报告期）

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | "SH600519" |

```python
import akshare as ak
df = ak.stock_cash_flow_sheet_by_report_em(symbol="SH600519")
```

### stock_cash_flow_sheet_by_yearly_em

描述：东方财富-现金流量表（按年度）

```python
import akshare as ak
df = ak.stock_cash_flow_sheet_by_yearly_em(symbol="SH600519")
```

---

## 财务摘要

### stock_financial_abstract

描述：新浪财经-财务关键指标摘要（含盈利能力、偿债能力、营运能力）

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | "600519" |

```python
import akshare as ak
df = ak.stock_financial_abstract(symbol="600519")
```

---

## 个股基本信息

### stock_individual_info_em

描述：东方财富-个股基本面信息（总市值、流通市值、行业、PE、PB 等）

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | "600519" |

```python
import akshare as ak
df = ak.stock_individual_info_em(symbol="600519")
```

---

## 盈利预测（机构一致预期）

### stock_profit_forecast_em

描述：东方财富-盈利预测（研报数、机构评级、预测 EPS）

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 空字符串获取全部；或行业板块名如 "白酒" |

输出包含：代码、名称、研报数、机构买入/增持/中性/减持/卖出评级数、各年预测 EPS

```python
import akshare as ak
# 获取全部股票盈利预测
df = ak.stock_profit_forecast_em()
# 筛选特定股票
target = df[df['代码'] == '600519']
```

---

## 行业对比

### stock_board_industry_spot_em

描述：东方财富-行业板块实时行情

输入参数：无

```python
import akshare as ak
df = ak.stock_board_industry_spot_em()
```

### stock_board_industry_cons_em

描述：东方财富-行业板块成份股

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 行业名称，如 "白酒"（通过 stock_board_industry_name_em 获取） |

```python
import akshare as ak
# 获取行业列表
industries = ak.stock_board_industry_name_em()
# 获取行业成份股
df = ak.stock_board_industry_cons_em(symbol="白酒")
```

### stock_industry_pe_ratio_cninfo

描述：巨潮-行业市盈率

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 行业代码 |
| date | str | "20241220" |

```python
import akshare as ak
df = ak.stock_industry_pe_ratio_cninfo(symbol="巨潮行业分类", date="20241220")
```

---

## 概念板块

### stock_board_concept_name_em

描述：东方财富-概念板块列表

输入参数：无

```python
import akshare as ak
df = ak.stock_board_concept_name_em()
```

### stock_board_concept_cons_em

描述：东方财富-概念板块成份股

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 概念名称，如 "人工智能" |

```python
import akshare as ak
df = ak.stock_board_concept_cons_em(symbol="人工智能")
```

---

## 机构持仓

### stock_report_fund_hold

描述：东方财富-机构持股汇总

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 股票代码 |
| date | str | 报告期 |

```python
import akshare as ak
df = ak.stock_report_fund_hold(symbol="基金", date="20240630")
```

---

## 港股/美股财务

### stock_financial_hk_report_em

描述：东方财富-港股财务报表

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| stock | str | 港股代码，如 "00700" |
| symbol | str | "资产负债表"/"利润表"/"现金流量表" |

```python
import akshare as ak
df = ak.stock_financial_hk_report_em(stock="00700", symbol="利润表")
```

### stock_financial_us_report_em

描述：东方财富-美股财务报表

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| stock | str | 美股代码，如 "AAPL" |
| symbol | str | "资产负债表"/"利润表"/"现金流量表" |

```python
import akshare as ak
df = ak.stock_financial_us_report_em(stock="AAPL", symbol="利润表")
```

---

## 基本面分析框架

### 盈利能力分析

```python
import akshare as ak
import pandas as pd

df = ak.stock_financial_analysis_indicator_em(symbol="SH600519", indicator="按报告期")
# 关键指标趋势
metrics = df[['REPORT_DATE_NAME', 'XSMLL', 'XSJLL', 'ROEJQ', 'PARENTNETPROFITTZ']].head(8)
print("毛利率/净利率/ROE/归属净利润增速 趋势:")
print(metrics.to_string(index=False))
```

### 估值分析

```python
import akshare as ak

# 获取实时估值数据
spot = ak.stock_zh_a_spot_em()
stock = spot[spot['代码'] == '600519'][['代码', '名称', '最新价', '市盈率-动态', '市净率', '总市值']].iloc[0]
print(f"PE(动态): {stock['市盈率-动态']:.2f}")
print(f"PB: {stock['市净率']:.2f}")
print(f"总市值: {stock['总市值']/1e8:.0f}亿")
```

### 成长性分析

```python
import akshare as ak

df = ak.stock_financial_analysis_indicator_em(symbol="SH600519", indicator="按报告期")
growth = df[['REPORT_DATE_NAME', 'TOTALOPERATEREVETZ', 'PARENTNETPROFITTZ', 'KCFJCXSYJLRTZ']].head(8)
print("营收增速/归属净利润增速/扣非净利润增速:")
print(growth.to_string(index=False))
```

### 同行业对比

```python
import akshare as ak
import pandas as pd

# 获取行业内公司列表
cons = ak.stock_board_industry_cons_em(symbol="白酒")
# 获取实时行情（含PE/PB）
spot = ak.stock_zh_a_spot_em()
# 合并对比
compare = spot[spot['代码'].isin(cons['代码'].tolist())][['代码', '名称', '最新价', '涨跌幅', '市盈率-动态', '市净率', '总市值']]
compare = compare.sort_values('总市值', ascending=False).head(10)
print(compare.to_string(index=False))
```

---

## 分析回答规范

1. **杜邦分析**：ROE = 净利率 × 资产周转率 × 权益乘数，拆解盈利来源
2. **纵向对比**：同一公司多个报告期趋势（成长性判断）
3. **横向对比**：同行业公司间估值、盈利能力对比
4. **量化结论**：每个结论都有具体数据支撑
5. **风险提示**：基本面分析有滞后性，财务数据存在报告期延迟，不构成投资建议
