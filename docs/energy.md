# 能源数据

## 油价数据

### energy_oil_hist

描述：汽柴油历史调价数据

输入参数：无

```python
import akshare as ak
df = ak.energy_oil_hist()
```

### energy_oil_detail

描述：全国各地油价数据

输入参数：无

```python
import akshare as ak
df = ak.energy_oil_detail()
```

---

## 碳排放

### energy_carbon_domestic

描述：国内碳排放交易数据

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 碳市场，如 "湖北"、"广东"、"深圳"、"北京"、"天津"、"上海"、"重庆"、"福建"、"全国" |

```python
import akshare as ak
df = ak.energy_carbon_domestic(symbol="全国")
```

---

## 天然气

### energy_lng_daily

描述：液化天然气日度数据

输入参数：无

```python
import akshare as ak
df = ak.energy_lng_daily()
```
