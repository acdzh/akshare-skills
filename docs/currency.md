# 数字货币数据

本文件仅说明数字货币实时行情、历史行情和持仓报告相关数据如何获取。

## 任务路由

| 数据需求 | 目标 | 优先接口 |
|------|------|----------|
| 数字货币快照 | 获取实时行情 | `crypto_spot_em` |
| 数字货币历史 | 获取历史价格序列 | `crypto_hist_em` |
| 持仓报告 | 获取比特币持仓报告 | `crypto_bitcoin_hold_report` |

## 高频接口

### crypto_spot_em

用途：获取数字货币实时行情。

### crypto_hist_em

用途：获取数字货币历史行情。

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 数字货币代码，如 `BTC`、`ETH` |
| period | str | `daily` / `weekly` / `monthly` |
| start_date | str | `YYYYMMDD` |
| end_date | str | `YYYYMMDD` |

### crypto_bitcoin_hold_report

用途：获取比特币持仓报告。

## 常见坑

1. 数字货币接口可能受网络环境影响较大。
2. 代码通常为大写英文简称。
3. 历史行情和持仓报告不是同一数据口径。
