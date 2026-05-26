# 基金数据

本文件仅说明基金相关数据如何获取，以及净值、行情、持仓、经理等字段的基本口径。

> 规则：优先使用非东方财富来源接口；若同主题只有东方财富可用，才将东方财富接口作为回退或兜底选择。

## 任务路由

| 数据需求 | 目标 | 候选接口（优先非东财） |
|------|------|----------|
| 基金检索 | 找代码、名称、类型 | `fund_name_em` |
| 开放式基金净值 | 获取单位净值、累计净值、收益率走势 | `fund_open_fund_info_em` |
| 开放式基金日表 | 获取同类型基金日度数据 | `fund_open_fund_daily_em` |
| ETF 行情 | 获取 ETF 盘中快照 | `fund_etf_spot_em` |
| ETF 历史 | 获取 ETF 历史价格序列 | `fund_etf_hist_em` |
| 持仓与经理 | 获取持仓、经理和规模信息 | `fund_portfolio_hold_em` / `fund_manager_em` / `fund_aum_em` |

## 高频接口

### fund_name_em

用途：基金基础信息检索。

关键字段：`基金代码`、`基金简称`、`基金类型`

### fund_open_fund_info_em

用途：开放式基金净值走势和同类排名走势。

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 基金代码，如 `110011` |
| indicator | str | `单位净值走势` / `累计净值走势` / `累计收益率走势` / `同类排名走势` / `同类排名百分比` |

### fund_open_fund_daily_em

用途：开放式基金日度数据。

| 名称 | 类型 | 描述 |
|------|------|------|
| fund_type | str | `全部` / `股票型` / `混合型` / `债券型` / `指数型` / `QDII` / `FOF` |

### fund_etf_spot_em

用途：ETF 实时行情。

### fund_etf_hist_em

用途：ETF 历史行情。

### fund_lof_spot_em

用途：LOF 实时行情。

### fund_open_fund_rank_em / fund_exchange_rank_em

用途：基金排行原始数据。

### fund_portfolio_hold_em

用途：股票持仓数据。

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 基金代码 |
| date | str | 报告期年份，如 `2024` |

### fund_portfolio_bond_hold_em

用途：债券持仓数据。

### fund_manager_em

用途：基金经理信息。

### fund_aum_em

用途：基金公司规模数据。

### fund_value_estimation_em

用途：基金估算净值。

## 常见坑

1. ETF 盘中价格和开放式基金净值不是同一口径。
2. 持仓披露存在报告期滞后。
3. 排行数据适合做筛字段，不代表长期稳定性。
4. 部分接口返回的是全量表，需要先筛字段再输出。
