# 银行数据

本文件仅说明银行理财产品、同业拆借利率以及银行个股相关数据的获取方式。

## 任务路由

| 数据需求 | 目标 | 优先接口 |
|------|------|----------|
| 银行理财产品 | 获取理财产品列表 | `bank_financial_product_em` |
| 同业拆借利率 | 获取银行间利率数据 | `rate_interbank` |
| 银行股行情 | 获取银行个股行情 | `stock_zh_a_spot_em` |
| 银行股财务 | 获取银行个股财务数据 | `stock_financial_analysis_indicator_em` |

## 高频接口

### bank_financial_product_em

用途：获取银行理财产品列表。

### rate_interbank

用途：获取同业拆借利率。

| 名称 | 类型 | 描述 |
|------|------|------|
| market | str | 市场名称 |
| symbol | str | 利率种类 |
| indicator | str | `隔夜` / `1周` / `2周` / `1月` / `3月` / `6月` / `9月` / `1年` |

### stock_zh_a_spot_em

用途：获取银行股实时行情，需再按行业或名称筛字段。

### stock_financial_analysis_indicator_em

用途：获取银行个股财务指标。

## 常见坑

1. 银行理财产品数据和银行股行情是两类完全不同的数据。
2. 同业拆借参数需要组合指定市场和利率种类。
3. 银行个股财务接口通常需要带市场前缀的股票代码。
