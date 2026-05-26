# 现货数据

本文件仅说明现货实时行情、历史行情、黄金白银基准价和部分商品现货对照数据如何获取。

## 任务路由

| 数据需求 | 目标 | 优先接口 |
|------|------|----------|
| 现货快照 | 获取现货实时行情 | `spot_em` |
| 现货历史 | 获取现货历史行情 | `spot_hist_em` |
| 黄金基准价 | 获取上海黄金交易所黄金基准价 | `spot_golden_benchmark_sge` |
| 白银基准价 | 获取上海黄金交易所白银基准价 | `spot_silver_benchmark_sge` |
| 期现对照 | 获取期货与现货对照价格 | `futures_spot_sys` |

## 高频接口

### spot_em

用途：获取现货实时行情。

### spot_hist_em

用途：获取现货历史行情。

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 现货品种代码 |
| period | str | `daily` / `weekly` / `monthly` |
| start_date | str | `YYYYMMDD` |
| end_date | str | `YYYYMMDD` |

### spot_golden_benchmark_sge

用途：获取黄金基准价。

### spot_silver_benchmark_sge

用途：获取白银基准价。

### futures_spot_sys

用途：获取期货与现货对照价格。

## 常见坑

1. 现货品种代码和期货代码不是同一套命名。
2. 基准价和市场成交价不是同一口径。
3. 历史行情接口返回频率依赖具体品种。
