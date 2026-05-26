# 基本面数据

本文件仅说明财务指标、三大报表、估值和行业对比数据如何获取。

## 任务路由

| 数据需求 | 目标 | 优先接口 |
|------|------|----------|
| 财务指标 | 获取增长、盈利、偿债、周转类字段 | `stock_financial_analysis_indicator_em` |
| 利润表 | 获取收入、利润等报表字段 | `stock_profit_sheet_by_report_em` |
| 资产负债表 | 获取资产、负债等报表字段 | `stock_balance_sheet_by_report_em` |
| 现金流量表 | 获取经营、投资、融资现金流字段 | `stock_cash_flow_sheet_by_report_em` |
| 估值快照 | 获取 PE、PB、市值等字段 | `stock_individual_info_em` |
| 一致预期 | 获取盈利预测和评级数 | `stock_profit_forecast_em` |
| 行业对比 | 获取行业成份股和行业估值 | `stock_board_industry_cons_em` / `stock_industry_pe_ratio_cninfo` |

## 高频接口

### stock_financial_analysis_indicator_em

用途：A 股财务分析主接口。

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 带市场前缀的代码，如 `SH600519` |
| indicator | str | `按报告期` / `按单季度` |

关键字段：`TOTALOPERATEREVETZ`、`PARENTNETPROFITTZ`、`ROEJQ`、`XSMLL`、`XSJLL`、`ZCFZL`、`LD`、`SD`

### stock_profit_sheet_by_report_em

用途：利润表。

### stock_balance_sheet_by_report_em

用途：资产负债表。

### stock_cash_flow_sheet_by_report_em

用途：现金流量表。

### stock_financial_abstract

用途：财务摘要。

### stock_individual_info_em

用途：个股基础信息和估值快照。

### stock_profit_forecast_em

用途：盈利预测和评级分布。

### stock_board_industry_cons_em

用途：行业成份股列表。

### stock_industry_pe_ratio_cninfo

用途：行业估值数据。

## 常见坑

1. 财务数据按报告期披露，输出时应保留报告期字段。
2. `stock_financial_analysis_indicator_em` 需要 `SH` / `SZ` 前缀。
3. 估值数据和财报数据可能来自不同时间点。
4. 行业估值口径要和具体行业分类一起输出。
