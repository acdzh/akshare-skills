# 银行数据

## 银行股实时行情

可通过 stock_zh_a_spot_em() 筛选银行板块获取

---

## 银行理财产品

### bank_financial_product_em

描述：银行理财产品列表

输入参数：无

```python
import akshare as ak
df = ak.bank_financial_product_em()
```

---

## 同业拆借利率

### rate_interbank

描述：同业拆借利率数据

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| market | str | "上海银行同业拆借市场"等 |
| symbol | str | "Shibor人民币"等 |
| indicator | str | "隔夜"/"1周"/"2周"/"1月"/"3月"/"6月"/"9月"/"1年" |

```python
import akshare as ak
df = ak.rate_interbank(market="上海银行同业拆借市场", symbol="Shibor人民币", indicator="隔夜")
```

---

## 银行财报

通过 stock_financial_analysis_indicator 系列接口获取银行个股财务数据。
