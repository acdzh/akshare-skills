# 期权数据

本文件仅说明 ETF 期权、商品期权、股指期权的行情、合约列表、历史和 Greeks 数据如何获取。

## 任务路由

| 数据需求 | 目标 | 优先接口 |
|------|------|----------|
| ETF 期权快照 | 获取 ETF 期权实时行情 | `option_current_em` |
| 合约列表 | 获取上交所期权合约列表 | `option_sse_list_sina` |
| 历史行情 | 获取期权历史行情 | `option_hist_em` |
| 风险指标 | 获取 Greeks 数据 | `option_risk_indicator_sse` |
| 商品期权 | 获取交易所商品期权日度数据 | `option_dce_daily` / `option_czce_daily` |
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

### option_hist_em

用途：获取期权历史行情。

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 期权合约代码 |

### option_risk_indicator_sse

用途：获取上交所期权风险指标。

| 名称 | 类型 | 描述 |
|------|------|------|
| date | str | `YYYYMMDD` |

### option_dce_daily / option_czce_daily

用途：获取商品期权日度数据。

### option_cffex_hs300_spot_sina

用途：获取沪深300股指期权实时数据。

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 合约月份，如 `2412` |

## 常见坑

1. 不同期权市场的合约代码格式差异很大。
2. 商品期权和 ETF 期权的字段口径不完全一致。
3. Greeks 数据通常是按日期批量提供，不是逐笔实时字段。
