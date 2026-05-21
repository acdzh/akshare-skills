# 宏观经济数据

## 核心经济指标

### macro_china_gdp

描述：中国 GDP 数据（东方财富）

输入参数：无

输出参数：季度、国内生产总值-绝对值、国内生产总值-同比增长、第一产业-绝对值、第二产业-绝对值、第三产业-绝对值 等

```python
import akshare as ak
df = ak.macro_china_gdp()
```

### macro_china_cpi

描述：中国 CPI 数据（东方财富）

输入参数：无

输出参数：月份、全国-当月、全国-同比增长、全国-环比增长、城市/农村相关字段

```python
import akshare as ak
df = ak.macro_china_cpi()
```

### macro_china_ppi

描述：中国 PPI 数据（东方财富）

输入参数：无

```python
import akshare as ak
df = ak.macro_china_ppi()
```

### macro_china_pmi

描述：中国 PMI 数据（东方财富）

输入参数：无

输出参数：月份、制造业-Loss指数、制造业-同比增长、非制造业-Loss指数、非制造业-同比增长

```python
import akshare as ak
df = ak.macro_china_pmi()
```

---

## 货币与信贷

### macro_china_m2_yearly

描述：中国 M2 货币供应量

输入参数：无

```python
import akshare as ak
df = ak.macro_china_m2_yearly()
```

### macro_china_money_supply

描述：中国货币供应量详细数据

输入参数：无

```python
import akshare as ak
df = ak.macro_china_money_supply()
```

### macro_china_new_financial_credit

描述：中国新增信贷数据

输入参数：无

```python
import akshare as ak
df = ak.macro_china_new_financial_credit()
```

### macro_china_shrzgm

描述：中国社会融资规模

输入参数：无

```python
import akshare as ak
df = ak.macro_china_shrzgm()
```

---

## 利率

### macro_china_lpr

描述：中国 LPR 贷款市场报价利率

输入参数：无

输出参数：TRADE_DATE, LPR1Y, LPR5Y

```python
import akshare as ak
df = ak.macro_china_lpr()
```

### macro_china_shibor_all

描述：中国 SHIBOR 利率数据

输入参数：无

```python
import akshare as ak
df = ak.macro_china_shibor_all()
```

---

## 贸易数据

### macro_china_exports_yoy

描述：中国出口额同比增速

输入参数：无

```python
import akshare as ak
df = ak.macro_china_exports_yoy()
```

### macro_china_imports_yoy

描述：中国进口额同比增速

输入参数：无

```python
import akshare as ak
df = ak.macro_china_imports_yoy()
```

### macro_china_trade_balance

描述：中国贸易差额

输入参数：无

```python
import akshare as ak
df = ak.macro_china_trade_balance()
```

### macro_china_hgjck

描述：中国海关进出口数据（东方财富）

输入参数：无

```python
import akshare as ak
df = ak.macro_china_hgjck()
```

---

## 工业与投资

### macro_china_gdzctz

描述：中国固定资产投资

输入参数：无

```python
import akshare as ak
df = ak.macro_china_gdzctz()
```

### macro_china_industrial_production_yoy

描述：中国工业增加值同比增速

输入参数：无

```python
import akshare as ak
df = ak.macro_china_industrial_production_yoy()
```

### macro_china_pmi_yearly

描述：中国制造业 PMI 年度数据

输入参数：无

```python
import akshare as ak
df = ak.macro_china_pmi_yearly()
```

### macro_china_cx_pmi_yearly

描述：中国财新制造业 PMI

输入参数：无

```python
import akshare as ak
df = ak.macro_china_cx_pmi_yearly()
```

---

## 财政数据

### macro_china_czsr

描述：中国财政收入

输入参数：无

```python
import akshare as ak
df = ak.macro_china_czsr()
```

---

## 消费

### macro_china_consumer_goods_retail

描述：中国社会消费品零售总额

输入参数：无

```python
import akshare as ak
df = ak.macro_china_consumer_goods_retail()
```

### macro_china_xfzxx

描述：中国消费者信心指数

输入参数：无

```python
import akshare as ak
df = ak.macro_china_xfzxx()
```

---

## 就业

### macro_china_urban_unemployment

描述：中国城镇调查失业率

输入参数：无

```python
import akshare as ak
df = ak.macro_china_urban_unemployment()
```

---

## 外汇储备

### macro_china_fx_reserves_yearly

描述：中国外汇储备

输入参数：无

```python
import akshare as ak
df = ak.macro_china_fx_reserves_yearly()
```

---

## 宏观杠杆率

### macro_cnbs

描述：中国国家金融与发展实验室-宏观杠杆率数据

输入参数：无

输出参数：年份、居民部门、非金融企业部门、政府部门、中央政府、地方政府、实体经济部门、金融部门资产方、金融部门负债方

```python
import akshare as ak
df = ak.macro_cnbs()
```

---

## 房地产

### macro_china_real_estate

描述：中国房地产数据

输入参数：无

```python
import akshare as ak
df = ak.macro_china_real_estate()
```

### macro_china_new_house_price

描述：中国新房价格指数

输入参数：无

```python
import akshare as ak
df = ak.macro_china_new_house_price()
```

---

## 香港宏观

### macro_china_hk_cpi

描述：中国香港 CPI

输入参数：无

```python
import akshare as ak
df = ak.macro_china_hk_cpi()
```

### macro_china_hk_gbp

描述：中国香港 GDP

输入参数：无

```python
import akshare as ak
df = ak.macro_china_hk_gbp()
```

### macro_china_hk_rate_of_unemployment

描述：中国香港失业率

输入参数：无

```python
import akshare as ak
df = ak.macro_china_hk_rate_of_unemployment()
```
