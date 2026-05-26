# 宏观经济数据

本文件服务于 2 类高频任务：

1. 判断当前宏观环境偏宽松、偏紧缩、偏复苏还是偏回落。
2. 解释宏观数据对股市、债市、商品和风险偏好的影响。

宏观问题的关键不是“把指标全报一遍”，而是抓住增长、通胀、流动性这三条主线，再说明它们对市场意味着什么。

## 任务路由

| 任务 | 目标 | 优先接口 |
|------|------|----------|
| 经济景气判断 | 看增长与需求 | `macro_china_gdp` + `macro_china_pmi` + `macro_china_industrial_production_yoy` |
| 通胀判断 | 看物价链条 | `macro_china_cpi` + `macro_china_ppi` |
| 流动性判断 | 看货币与利率环境 | `macro_china_money_supply` + `macro_china_lpr` + `macro_china_shibor_all` |
| 内需与外需 | 看消费和外贸 | `macro_china_consumer_goods_retail` + `macro_china_exports_yoy` + `macro_china_imports_yoy` |
| 综合环境判断 | 增长 + 通胀 + 利率 至少三选二 | 组合多个接口 |

## 推荐工作流

### 宏观环境判断

至少覆盖以下 3 条主线中的 2 条：

1. 增长：GDP、PMI、工业生产、消费、固定资产投资
2. 通胀：CPI、PPI
3. 流动性：M2、社融、LPR、SHIBOR

如果用户问“现在市场环境如何”，不要只给一个单点指标，比如“CPI 低所以利好股市”，这种结论太单薄。

### 与市场联动的解释框架

1. 增长走强：通常利好盈利预期，但也要看估值是否已透支。
2. 通胀上行：可能压缩宽松空间，对高估值资产不一定友好。
3. 流动性宽松：一般提升风险偏好，但要结合信用和景气度。
4. 外需改善：出口链和制造业景气度可能受益。

## 高频接口

### macro_china_gdp

用途：看经济总量和增长趋势，是宏观背景判断的基础指标。

输入参数：无

重点字段通常包括：季度、GDP 绝对值、GDP 同比增长

```python
import akshare as ak

gdp = ak.macro_china_gdp()
print(gdp.tail())
```

使用建议：

1. GDP 频率低，适合定大方向，不适合解释短线波动。
2. 最好与 PMI、工业增加值一起看，避免单看 GDP。

### macro_china_pmi

用途：看制造业和非制造业景气度，是市场最常用的宏观高频指标之一。

输入参数：无

```python
import akshare as ak

pmi = ak.macro_china_pmi()
print(pmi.tail())
```

使用建议：

1. 看方向时优先关注是否连续回升或跌破荣枯线附近。
2. 单月波动有噪音，最好看连续 2 到 3 期变化。

### macro_china_cpi

用途：看居民通胀，判断消费价格压力和政策空间。

输入参数：无

```python
import akshare as ak

cpi = ak.macro_china_cpi()
print(cpi.tail())
```

使用建议：

1. 低通胀不一定直接利好股市，还要结合需求和盈利。
2. 要和 PPI 一起看价格链条，而不是孤立解读。

### macro_china_ppi

用途：看工业品价格与上游价格压力，适合结合制造业和盈利预期判断。

输入参数：无

```python
import akshare as ak

ppi = ak.macro_china_ppi()
print(ppi.tail())
```

### macro_china_money_supply

用途：看 M0、M1、M2 的货币增速，辅助判断流动性环境。

输入参数：无

```python
import akshare as ak

money = ak.macro_china_money_supply()
print(money.tail())
```

使用建议：

1. 货币增速变化对资产价格影响常有时滞。
2. 最好和社融、LPR、SHIBOR 一起看。

### macro_china_lpr

用途：看贷款市场报价利率，判断政策利率方向和融资成本环境。

输入参数：无

关键字段通常包括：`TRADE_DATE`、`LPR1Y`、`LPR5Y`

```python
import akshare as ak

lpr = ak.macro_china_lpr()
print(lpr.tail())
```

### macro_china_shibor_all

用途：看资金面利率，适合判断短期流动性松紧。

输入参数：无

```python
import akshare as ak

shibor = ak.macro_china_shibor_all()
print(shibor.tail())
```

使用建议：

1. SHIBOR 更偏短期资金面，不代表中长期基本面。
2. 和股市联动时要避免过度机械解读。

### macro_china_exports_yoy / macro_china_imports_yoy

用途：看外需和内需的外贸侧变化，适合判断出口链、制造业景气和内需修复。

输入参数：无

```python
import akshare as ak

exports = ak.macro_china_exports_yoy()
imports = ak.macro_china_imports_yoy()
print(exports.tail())
print(imports.tail())
```

### macro_china_consumer_goods_retail

用途：看社会消费品零售总额，适合观察内需修复与消费环境。

输入参数：无

```python
import akshare as ak

retail = ak.macro_china_consumer_goods_retail()
print(retail.tail())
```

## 低频但常用补充接口

### macro_china_new_financial_credit

用途：新增信贷，适合补充信用扩张判断。

### macro_china_shrzgm

用途：社融规模，适合看实体融资环境。

### macro_china_gdzctz

用途：固定资产投资，适合看地产、基建、制造业投资趋势。

### macro_china_industrial_production_yoy

用途：工业增加值同比，适合看工业景气修复。

### macro_china_trade_balance

用途：贸易顺差/逆差背景判断。

### macro_china_cx_pmi_yearly

用途：财新 PMI，可补充官方 PMI 的横向视角。

## 结论输出建议

当用户问“当前宏观环境怎么看”时，建议按以下结构输出：

1. 一句话环境判断
2. 增长证据
3. 通胀证据
4. 流动性证据
5. 对市场的含义
6. 需要继续观察的拐点

示例：

```text
结论：当前更接近“弱复苏 + 温和通胀 + 流动性偏稳定”的环境，风险偏好有修复基础，但上行动力仍需更强增长数据确认。

核心证据：
1. PMI 连续改善，说明景气边际修复。
2. CPI 仍处温和区间，通胀压力不强。
3. LPR 和 SHIBOR 没有明显收紧，流动性环境尚可。

市场含义：
1. 对顺周期和高股息方向偏中性偏正面。
2. 对高估值成长风格是否持续占优，还要看后续盈利和利率变化。
```

## 常见坑

1. 不要拿单月数据直接外推全年趋势。
2. 不要把宏观指标变化和市场涨跌做机械一一对应。
3. 不要只说“利率下行利好股市”，要结合增长和盈利。
4. 不要只列指标，不解释它们对资产配置意味着什么。
5. 用户关心的是环境判断和资产含义，不是宏观数据库搬运。

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
