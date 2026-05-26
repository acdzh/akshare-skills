# 基本面分析

本文件服务于 4 类高频任务：

1. 判断公司盈利质量和成长性。
2. 判断当前估值贵不贵、值不值得这个价格。
3. 做行业内横向对比。
4. 为“综合分析个股”提供长期证据。

基本面分析的重点不是把财报字段报全，而是提炼出增长、盈利、质量、估值这 4 条主线。

## 任务路由

| 任务 | 目标 | 优先接口 |
|------|------|----------|
| 财务质量 | 看营收、利润、ROE、利润率、负债率 | `stock_financial_analysis_indicator_em` |
| 三表验证 | 看利润表、资产负债表、现金流 | `stock_profit_sheet_by_report_em` + `stock_balance_sheet_by_report_em` + `stock_cash_flow_sheet_by_report_em` |
| 估值快照 | 看 PE、PB、市值 | `stock_individual_info_em` |
| 一致预期 | 看机构盈利预测和评级分布 | `stock_profit_forecast_em` |
| 行业对比 | 看行业成份股与行业估值 | `stock_board_industry_cons_em` + `stock_industry_pe_ratio_cninfo` |

## 推荐工作流

### 单股基本面判断

至少覆盖以下 4 个维度中的 3 个：

1. 增长：营收增速、净利增速
2. 盈利能力：ROE、毛利率、净利率
3. 质量与稳健性：现金流、负债率、周转效率
4. 估值：PE、PB、行业相对位置

### 基本面和股价的关系

1. 好公司不一定是好价格，估值仍要单独判断。
2. 财务数据是报告期口径，不能当成实时经营状态。
3. 单季大增不一定代表趋势反转，最好看连续性。

## 高频接口

### stock_financial_analysis_indicator_em

用途：A 股基本面主接口，适合快速拿到增长、盈利、偿债和周转相关核心指标。

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 带市场前缀的代码，如 `SH600519` |
| indicator | str | `按报告期` / `按单季度` |

关键字段：

| 字段 | 含义 |
|------|------|
| TOTALOPERATEREVETZ | 营业总收入同比增长 |
| PARENTNETPROFITTZ | 归母净利润同比增长 |
| ROEJQ | 加权 ROE |
| XSMLL | 毛利率 |
| XSJLL | 净利率 |
| ZCFZL | 资产负债率 |
| LD | 流动比率 |
| SD | 速动比率 |

```python
import akshare as ak

fin = ak.stock_financial_analysis_indicator_em(symbol="SH600519", indicator="按报告期")
print(fin.head())
```

使用建议：

1. 优先作为基本面分析的起点。
2. 财务结论必须注明报告期。
3. `symbol` 带 `SH` / `SZ` 前缀是高频易错点。

### stock_profit_sheet_by_report_em

用途：补利润表细节，适合验证收入和利润结构。

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 如 `SH600519` |

### stock_balance_sheet_by_report_em

用途：补充资产负债结构，适合判断杠杆和财务稳健性。

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 如 `SH600519` |

### stock_cash_flow_sheet_by_report_em

用途：补充现金流质量，适合判断利润是否“有现金支撑”。

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 如 `SH600519` |

使用建议：

1. 三表更适合深挖，不一定每次都要全用。
2. 当利润高增但现金流很弱时，要提高警惕。

### stock_financial_abstract

用途：快速查看财务摘要，适合做辅助概览。

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 不带前缀的代码，如 `600519` |

### stock_individual_info_em

用途：查看个股基础画像，适合补 PE、PB、市值、行业等快照信息。

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 股票代码，如 `600519` |

```python
import akshare as ak

info = ak.stock_individual_info_em(symbol="600519")
print(info)
```

使用建议：

1. 适合补估值快照，不是完整财务接口。
2. 做“贵不贵”判断时最好结合行业估值一起看。

### stock_profit_forecast_em

用途：看机构盈利预测与评级分布，适合补一致预期维度。

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 空字符串获取全部；也可按行业名筛选 |

```python
import akshare as ak

forecast = ak.stock_profit_forecast_em()
target = forecast[forecast["代码"] == "600519"]
print(target)
```

使用建议：

1. 一致预期可以辅助判断，但不能代替财务事实。
2. 研报评级容易滞后或拥挤。

## 行业对比

### stock_board_industry_cons_em

用途：获取行业成份股，适合做同行横向比较。

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 行业名称，如 `白酒` |

### stock_industry_pe_ratio_cninfo

用途：获取行业估值口径，适合判断个股 PE 是否高于或低于行业水平。

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 行业分类口径 |
| date | str | 如 `20241220` |

使用建议：

1. 个股估值一定要放回行业环境里看。
2. 周期股和消费股不能用同一估值标准硬比。

## 低频但常用补充接口

### stock_financial_analysis_indicator

用途：新浪口径财务指标，可做交叉验证。

### stock_profit_sheet_by_yearly_em / stock_profit_sheet_by_quarterly_em

用途：年度或单季度利润表，适合观察连续趋势。

### stock_balance_sheet_by_yearly_em / stock_cash_flow_sheet_by_yearly_em

用途：更长周期的稳健性分析。

### stock_report_fund_hold

用途：看机构持股情况，适合辅助判断机构偏好。

## 结论输出建议

当用户问“这家公司基本面怎么样”时，建议按以下结构输出：

1. 一句话结论
2. 增长证据
3. 盈利能力证据
4. 财务质量证据
5. 估值判断
6. 主要风险

示例：

```text
结论：基本面整体较强，但当前估值已经不算便宜。

核心证据：
1. 最近一期营收和净利润仍保持较快增长。
2. ROE 和净利率维持在较高水平，盈利质量较好。
3. 现金流没有明显恶化，资产负债率处在可接受区间。

估值判断：
1. 动态 PE 明显高于行业中位数，说明市场已提前反映部分乐观预期。

主要风险：
1. 财务数据存在报告期滞后。
2. 如果后续增长放缓，高估值容易被压缩。
```

## 常见坑

1. 不要只看 PE 或只看 ROE。
2. 不要忽略财务数据的报告期滞后。
3. 不要把高增长单季数据当成长期趋势。
4. 不要脱离行业背景谈估值高低。
5. 用户要的是“公司好不好、贵不贵、风险在哪”，不是财报字段全集。

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| stock | str | 港股代码，如 "00700" |
| symbol | str | "资产负债表"/"利润表"/"现金流量表" |

```python
import akshare as ak
df = ak.stock_financial_hk_report_em(stock="00700", symbol="利润表")
```

### stock_financial_us_report_em

描述：东方财富-美股财务报表

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| stock | str | 美股代码，如 "AAPL" |
| symbol | str | "资产负债表"/"利润表"/"现金流量表" |

```python
import akshare as ak
df = ak.stock_financial_us_report_em(stock="AAPL", symbol="利润表")
```

---

## 基本面分析框架

### 盈利能力分析

```python
import akshare as ak
import pandas as pd

df = ak.stock_financial_analysis_indicator_em(symbol="SH600519", indicator="按报告期")
# 关键指标趋势
metrics = df[['REPORT_DATE_NAME', 'XSMLL', 'XSJLL', 'ROEJQ', 'PARENTNETPROFITTZ']].head(8)
print("毛利率/净利率/ROE/归属净利润增速 趋势:")
print(metrics.to_string(index=False))
```

### 估值分析

```python
import akshare as ak

# 获取实时估值数据
spot = ak.stock_zh_a_spot_em()
stock = spot[spot['代码'] == '600519'][['代码', '名称', '最新价', '市盈率-动态', '市净率', '总市值']].iloc[0]
print(f"PE(动态): {stock['市盈率-动态']:.2f}")
print(f"PB: {stock['市净率']:.2f}")
print(f"总市值: {stock['总市值']/1e8:.0f}亿")
```

### 成长性分析

```python
import akshare as ak

df = ak.stock_financial_analysis_indicator_em(symbol="SH600519", indicator="按报告期")
growth = df[['REPORT_DATE_NAME', 'TOTALOPERATEREVETZ', 'PARENTNETPROFITTZ', 'KCFJCXSYJLRTZ']].head(8)
print("营收增速/归属净利润增速/扣非净利润增速:")
print(growth.to_string(index=False))
```

### 同行业对比

```python
import akshare as ak
import pandas as pd

# 获取行业内公司列表
cons = ak.stock_board_industry_cons_em(symbol="白酒")
# 获取实时行情（含PE/PB）
spot = ak.stock_zh_a_spot_em()
# 合并对比
compare = spot[spot['代码'].isin(cons['代码'].tolist())][['代码', '名称', '最新价', '涨跌幅', '市盈率-动态', '市净率', '总市值']]
compare = compare.sort_values('总市值', ascending=False).head(10)
print(compare.to_string(index=False))
```

---

## 分析回答规范

1. **杜邦分析**：ROE = 净利率 × 资产周转率 × 权益乘数，拆解盈利来源
2. **纵向对比**：同一公司多个报告期趋势（成长性判断）
3. **横向对比**：同行业公司间估值、盈利能力对比
4. **量化结论**：每个结论都有具体数据支撑
5. **风险提示**：基本面分析有滞后性，财务数据存在报告期延迟，不构成投资建议
