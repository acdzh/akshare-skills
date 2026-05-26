# 能源数据

本文件仅说明油价、碳排放和能源日度指标相关数据如何获取。

## 任务路由

| 数据需求 | 目标 | 优先接口 |
|------|------|----------|
| 油价调价 | 获取汽柴油历史调价数据 | `energy_oil_hist` |
| 地区油价 | 获取各地油价数据 | `energy_oil_detail` |
| 碳排放 | 获取国内碳市场交易数据 | `energy_carbon_domestic` |
| 能源日度指标 | 获取沿海六大电厂库存等能源数据 | `macro_china_daily_energy` |
| 能源指数 | 获取能源指数数据 | `macro_china_energy_index` |

## 高频接口

### energy_oil_hist

用途：获取汽柴油历史调价数据。

### energy_oil_detail

用途：获取全国各地油价数据。

### energy_carbon_domestic

用途：获取国内碳排放交易数据。

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 碳市场名称，如 `全国`、`湖北`、`广东` |

### macro_china_daily_energy

用途：获取中国日度能源相关数据。

### macro_china_energy_index

用途：获取能源指数数据。

## 常见坑

1. 油价调价和地区油价不是同一时间粒度。
2. 碳市场 `symbol` 为市场名称而不是代码。
3. 能源类接口字段口径差异较大，输出前应检查列名。
