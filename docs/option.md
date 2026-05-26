# 期权数据

本文件仅说明 ETF 期权、商品期权、股指期权的行情、合约列表、历史和 Greeks 数据如何获取。

> 规则：优先使用非东方财富来源接口；若同主题只有东方财富可用，才将东方财富接口作为回退或兜底选择。

## 任务路由

| 数据需求 | 目标 | 候选接口（优先非东财） |
|------|------|----------|
| ETF 期权快照 | 获取 ETF 期权实时行情 | `option_current_em` |
| 合约列表 | 获取上交所期权合约列表 | `option_sse_list_sina` |
| ETF 期权历史 | 获取上交所期权历史日线 | `option_sse_daily_sina` |
| 风险指标 | 获取 Greeks 数据 | `option_risk_indicator_sse` |
| 商品期权 | 获取交易所商品期权日度数据 | `option_hist_dce` / `option_hist_czce` |
| 股指期权 | 获取沪深300股指期权实时数据 | `option_cffex_hs300_spot_sina` |

## 高频接口

### option_current_em

用途：获取 ETF 期权实时行情。

### option_sse_list_sina

用途：获取上交所期权合约列表。

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | `50ETF` / `300ETF` |
| exchange | str | 通常为 `null` |

### option_sse_daily_sina

用途：获取指定上交所期权历史日线。

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 期权代码，如 `10003889` |

### option_risk_indicator_sse

用途：获取上交所期权风险指标。

| 名称 | 类型 | 描述 |
|------|------|------|
| date | str | `YYYYMMDD` |

### option_hist_dce / option_hist_czce

用途：获取商品期权日度数据。

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 期权品种名称 |
| trade_date | str | `YYYYMMDD` |

### option_cffex_hs300_spot_sina

用途：获取沪深300股指期权实时数据。

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 合约月份，如 `2412` |

## 常见坑

1. 不同期权市场的合约代码格式差异很大。
2. 商品期权和 ETF 期权的字段口径不完全一致。
3. Greeks 数据通常是按日期批量提供，不是逐笔实时字段。
