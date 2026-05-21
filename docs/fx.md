# 外汇数据

## 外汇实时行情

### forex_spot_em

描述：东方财富-外汇市场所有汇率实时行情

输入参数：无

输出参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| 代码 | object | 货币对代码，如 USDJPY |
| 名称 | object | 如 "美元兑日元" |
| 最新价 | float64 | - |
| 涨跌额 | float64 | - |
| 涨跌幅 | float64 | - |
| 今开 | float64 | - |
| 最高 | float64 | - |
| 最低 | float64 | - |
| 昨收 | float64 | - |

```python
import akshare as ak
df = ak.forex_spot_em()
```

---

## 外汇历史行情

### forex_hist_em

描述：东方财富-外汇历史行情

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 货币对代码，如 "USDCNH"(美元/离岸人民币)、"EURUSD"(欧元/美元) |

输出参数：日期、开盘、收盘、最高、最低

```python
import akshare as ak
df = ak.forex_hist_em(symbol="USDCNH")
```

---

## 人民币汇率

### currency_boc_safe

描述：中国银行外汇牌价

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 币种，如 "美元"、"欧元"、"日元"、"英镑" |
| start_date | str | "20240101" |
| end_date | str | "20241231" |

```python
import akshare as ak
df = ak.currency_boc_safe(symbol="美元", start_date="20240101", end_date="20241231")
```

---

## 人民币中间价

### macro_china_rmb

描述：人民币汇率中间价数据

输入参数：无

```python
import akshare as ak
df = ak.macro_china_rmb()
```

---

## 常用货币对代码

| 代码 | 含义 |
|------|------|
| USDCNH | 美元/离岸人民币 |
| USDCNY | 美元/在岸人民币 |
| EURUSD | 欧元/美元 |
| USDJPY | 美元/日元 |
| GBPUSD | 英镑/美元 |
| AUDUSD | 澳元/美元 |
| USDCHF | 美元/瑞郎 |
| USDCAD | 美元/加元 |
| USDHKD | 美元/港币 |
