# 现货数据

## 现货实时行情

### spot_em

描述：东方财富-现货实时行情

输入参数：无

```python
import akshare as ak
df = ak.spot_em()
```

---

## 现货历史行情

### spot_hist_em

描述：东方财富-现货历史行情

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 现货品种代码 |
| period | str | "daily"/"weekly"/"monthly" |
| start_date | str | "20240101" |
| end_date | str | "20241231" |

```python
import akshare as ak
df = ak.spot_hist_em(symbol="Au99.99", period="daily", start_date="20240101", end_date="20241231")
```

---

## 黄金/白银现货

### spot_golden_benchmark_sge

描述：上海黄金交易所-黄金基准价

输入参数：无

```python
import akshare as ak
df = ak.spot_golden_benchmark_sge()
```

### spot_silver_benchmark_sge

描述：上海黄金交易所-白银基准价

输入参数：无

```python
import akshare as ak
df = ak.spot_silver_benchmark_sge()
```

---

## 大宗商品现货价格

### futures_spot_sys

描述：期货与现货对照价格

输入参数：无

```python
import akshare as ak
df = ak.futures_spot_sys()
```
