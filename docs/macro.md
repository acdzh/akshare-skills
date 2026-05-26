# 宏观经济数据

本文件仅说明宏观指标、利率和外贸数据如何获取，以及常见指标的基本口径。

## 任务路由

| 数据需求 | 目标 | 优先接口 |
|------|------|----------|
| 增长数据 | GDP、PMI、工业生产、消费、投资 | `macro_china_gdp` / `macro_china_pmi` / `macro_china_industrial_production_yoy` |
| 通胀数据 | CPI、PPI | `macro_china_cpi` / `macro_china_ppi` |
| 货币与利率 | M2、LPR、SHIBOR、社融 | `macro_china_money_supply` / `macro_china_lpr` / `macro_china_shibor_all` |
| 外贸数据 | 出口、进口、贸易差额 | `macro_china_exports_yoy` / `macro_china_imports_yoy` / `macro_china_trade_balance` |

## 高频接口

### macro_china_gdp

用途：GDP 历史数据。

### macro_china_pmi

用途：PMI 历史数据。

### macro_china_cpi

用途：CPI 历史数据。

### macro_china_ppi

用途：PPI 历史数据。

### macro_china_money_supply

用途：M0、M1、M2 历史数据。

### macro_china_lpr

用途：LPR 历史数据。

关键字段通常包括：`TRADE_DATE`、`LPR1Y`、`LPR5Y`

### macro_china_shibor_all

用途：SHIBOR 历史数据。

### macro_china_exports_yoy / macro_china_imports_yoy

用途：进出口同比数据。

### macro_china_trade_balance

用途：贸易差额数据。

### macro_china_consumer_goods_retail

用途：社会消费品零售总额数据。

## 常见坑

1. 宏观指标频率不同，季度、月度、日度不要直接混用。
2. 不同来源的字段名可能不统一，输出前应检查列名。
3. 宏观接口通常返回长时间序列，建议先取尾部样本或指定字段。
