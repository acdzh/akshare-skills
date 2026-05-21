# 数字货币数据

## 数字货币实时行情

### crypto_spot_em

描述：东方财富-数字货币实时行情

输入参数：无

```python
import akshare as ak
df = ak.crypto_spot_em()
```

---

## 数字货币历史行情

### crypto_hist_em

描述：东方财富-数字货币历史行情

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 数字货币代码 |
| period | str | "daily"/"weekly"/"monthly" |
| start_date | str | "20240101" |
| end_date | str | "20241231" |

```python
import akshare as ak
df = ak.crypto_hist_em(symbol="BTC", period="daily", start_date="20240101", end_date="20241231")
```

---

## 数字货币-币安

### crypto_bitcoin_hold_report

描述：比特币持仓报告

输入参数：无

```python
import akshare as ak
df = ak.crypto_bitcoin_hold_report()
```

---

## 注意事项

- 数字货币接口可能因网络或数据源不稳定而请求失败
- 部分接口需要能访问境外网络
- 代码格式通常为大写英文简称，如 "BTC"、"ETH"
