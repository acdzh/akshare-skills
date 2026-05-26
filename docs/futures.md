# 期货数据

本文件仅说明国内外期货行情、历史数据、分钟数据、合约信息和持仓库存数据如何获取。

> 规则：优先使用非东方财富来源接口；若同主题只有东方财富可用，才将东方财富接口作为回退或兜底选择。

## 任务路由

| 数据需求 | 目标 | 候选接口（优先非东财） |
|------|------|----------|
| 国内期货快照 | 获取国内期货实时行情 | `futures_zh_spot` |
| 合约历史 | 获取单合约历史日线 | `futures_zh_daily_sina` / `futures_hist_em` |
| 主力连续 | 获取主力连续合约历史 | `futures_main_sina` |
| 分钟数据 | 获取期货分钟级行情 | `futures_zh_minute_sina` |
| 合约详情 | 获取乘数、最小变动等 | `futures_contract_detail` |
| 持仓排名 | 获取交易所持仓排名 | `futures_dce_position_rank` |
| 库存数据 | 获取库存数据 | `futures_inventory_em` |
| 国际期货 | 获取国际期货实时或历史 | `futures_foreign_commodity_realtime` / `futures_foreign_hist` / `futures_global_spot_em` |

## 高频接口

### futures_zh_spot

用途：获取国内期货实时行情。

关键字段：`代码`、`名称`、`最新价`、`涨跌额`、`涨跌幅`、`持仓量`、`成交量`

### futures_zh_daily_sina

用途：获取单合约历史日线。

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 合约代码，如 `RB2501`、`AU2412` |

### futures_main_sina

用途：获取主力连续合约历史。

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 品种代码，如 `RB0`、`AU0` |
| start_date | str | `YYYYMMDD` |
| end_date | str | `YYYYMMDD` |

### futures_hist_em

用途：获取东财口径期货历史行情。

### futures_zh_minute_sina

用途：获取分钟级期货行情。

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 合约代码 |
| period | str | `1` / `5` / `15` / `30` / `60` |

### futures_contract_detail

用途：获取合约详情。

### futures_dce_position_rank

用途：获取持仓排名。

### futures_inventory_em

用途：获取库存数据。

### futures_fees_info

用途：获取手续费信息。

### futures_foreign_commodity_realtime / futures_foreign_hist / futures_global_spot_em

用途：获取国际或全球期货数据。

## 常见坑

1. 单合约和主力连续不是同一口径。
2. 期货代码大小写和交易所习惯可能不同。
3. 分钟数据与日线数据字段名可能不一致。
4. 国际期货接口的品种名称口径可能与国内不同。
