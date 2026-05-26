# 利率数据

本文件仅说明 LPR、SHIBOR、准备金率、同业拆借、国债收益率和 Swap 利率数据如何获取。

## 任务路由

| 数据需求 | 目标 | 优先接口 |
|------|------|----------|
| LPR | 获取贷款市场报价利率 | `macro_china_lpr` |
| SHIBOR | 获取银行间拆借利率 | `macro_china_shibor_all` |
| 准备金率 | 获取存款准备金率数据 | `macro_china_reserve_requirement_ratio` |
| 同业拆借 | 获取同业拆借利率 | `rate_interbank` |
| 国债收益率 | 获取中美国债收益率 | `bond_zh_us_rate` |
| Swap 利率 | 获取利率互换数据 | `macro_china_swap_rate` |

## 高频接口

### macro_china_lpr

用途：获取 LPR 历史数据。

关键字段通常包括：`TRADE_DATE`、`LPR1Y`、`LPR5Y`

### macro_china_shibor_all

用途：获取 SHIBOR 历史数据。

### macro_china_reserve_requirement_ratio

用途：获取存款准备金率数据。

### rate_interbank

用途：获取同业拆借利率。

| 名称 | 类型 | 描述 |
|------|------|------|
| market | str | 市场名称 |
| symbol | str | 利率种类 |
| indicator | str | `隔夜` / `1周` / `2周` / `1月` / `3月` / `6月` / `9月` / `1年` |

### bond_zh_us_rate

用途：获取中美国债收益率历史。

### macro_china_swap_rate

用途：获取中国利率互换数据。

## 常见坑

1. 利率数据频率可能是日度、周度或事件驱动。
2. 同业拆借接口依赖多个参数共同确定口径。
3. 国债收益率和政策利率不是同一概念。
