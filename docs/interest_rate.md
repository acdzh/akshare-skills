# 利率数据

## LPR 利率

### macro_china_lpr

描述：中国贷款市场报价利率 (LPR)

输入参数：无

输出参数：TRADE_DATE, LPR1Y, LPR5Y

```python
import akshare as ak
df = ak.macro_china_lpr()
```

---

## SHIBOR

### macro_china_shibor_all

描述：上海银行间同业拆放利率 (SHIBOR)

输入参数：无

```python
import akshare as ak
df = ak.macro_china_shibor_all()
```

---

## 存贷款利率

### macro_china_reserve_requirement_ratio

描述：中国存款准备金率数据

输入参数：无

```python
import akshare as ak
df = ak.macro_china_reserve_requirement_ratio()
```

---

## 同业拆借

### rate_interbank

描述：同业拆借利率

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| market | str | "上海银行同业拆借市场"/"中国银行同业拆借市场" 等 |
| symbol | str | "Shibor人民币"/"银银间回购定盘利率" 等 |
| indicator | str | "隔夜"/"1周"/"2周"/"1月"/"3月"/"6月"/"9月"/"1年" |

```python
import akshare as ak
df = ak.rate_interbank(market="上海银行同业拆借市场", symbol="Shibor人民币", indicator="1周")
```

---

## 国债收益率

### bond_zh_us_rate

描述：中美国债收益率

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| start_date | str | "20240101" |

```python
import akshare as ak
df = ak.bond_zh_us_rate(start_date="20240101")
```

---

## Swap 利率

### macro_china_swap_rate

描述：中国利率互换数据

输入参数：无

```python
import akshare as ak
df = ak.macro_china_swap_rate()
```
