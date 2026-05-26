# 现货数据

本文件仅说明上海黄金交易所现货、现货历史、现货品种表和期现对照数据如何获取。

> 规则：优先使用非东方财富来源接口；若同主题只有东方财富可用，才将东方财富接口作为回退或兜底选择。

## 任务路由

| 数据需求 | 目标 | 候选接口（优先非东财） |
|------|------|----------|
| SGE 实时行情 | 获取上海黄金交易所实时行情 | `spot_quotations_sge` |
| SGE 历史行情 | 获取上海黄金交易所历史行情 | `spot_hist_sge` |
| SGE 品种表 | 获取上海黄金交易所品种清单 | `spot_symbol_table_sge` |
| 现货走势 | 获取 99 期货现货走势 | `spot_price_qh` |
| 品种对照表 | 获取 99 期货现货品种表 | `spot_price_table_qh` |
| 黄金/白银基准价 | 获取基准价数据 | `spot_golden_benchmark_sge` / `spot_silver_benchmark_sge` |
| 期现对照 | 获取期货与现货对照价格 | `futures_spot_sys` |

## 高频接口

### spot_quotations_sge

用途：获取上海黄金交易所实时行情。

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 品种代码，如 `Au99.99` |

### spot_hist_sge

用途：获取上海黄金交易所历史行情。

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 品种代码，如 `Au99.99` |

### spot_symbol_table_sge

用途：获取上海黄金交易所品种表。

### spot_price_qh

用途：获取 99 期货现货走势。

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 品种名称，如 `螺纹钢` |

### spot_price_table_qh

用途：获取 99 期货现货品种对照表。

### spot_golden_benchmark_sge / spot_silver_benchmark_sge

用途：获取黄金和白银基准价。

### futures_spot_sys

用途：获取期货与现货对照价格。

## 常见坑

1. 上海黄金交易所行情和 99 期货现货走势不是同一来源。
2. 基准价和市场成交价不是同一口径。
3. 现货品种代码和期货代码不是同一套命名。
