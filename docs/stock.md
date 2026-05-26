# 股票数据

本文件服务于 3 类高频任务：

1. 快速回答单只股票“现在怎么样”。
2. 支持“值不值得买/持有/减仓”的综合判断。
3. 支持选股、排序、候选池筛选。

优先顺序不是“先把所有接口都读一遍”，而是先判断任务类型，再取最少但最关键的数据。

## 任务路由

| 任务 | 目标 | 优先接口 |
|------|------|----------|
| 快速行情 | 看最新价、涨跌幅、成交额、估值快照 | `stock_zh_a_spot_em` |
| 趋势判断 | 看近一段时间走势、均线、波动、量价 | `stock_zh_a_hist` |
| 综合分析 | 趋势 + 基本面 + 消息/资金 | `stock_zh_a_spot_em` + `stock_zh_a_hist` + `stock_financial_analysis_indicator_em` + `stock_comment_em` / `stock_individual_fund_flow_rank` |
| 选股 | 快照粗筛后再少量深挖 | `stock_zh_a_spot_em` + `stock_zh_a_hist` + `stock_financial_analysis_indicator_em` |
| 事件辅助 | 看公告、新闻、热度 | `stock_notice_report` + `stock_news_em` + `stock_comment_em` |

## 推荐工作流

### 单股快速判断

1. 用 `stock_zh_a_spot_em` 拿到实时快照。
2. 用股票代码筛出目标行。
3. 如果用户追问趋势，再补 `stock_zh_a_hist`。
4. 如果用户追问“值不值”，再补财务和情绪维度。

### 单股综合判断

至少覆盖以下 4 个维度中的 3 个：

1. 价格与趋势
2. 估值
3. 基本面
4. 消息与资金

不要只看一个指标就下结论，例如“PE 低就买”“涨幅大就强势”都不够稳。

### 选股

1. 先用 `stock_zh_a_spot_em` 做粗筛，排除 `ST|退`、低流动性、极端小市值。
2. 再对少量候选补历史走势或财务数据。
3. 结果输出 Top 5 到 Top 20，并说明入选原因。

## 高频接口

### stock_zh_a_spot_em

用途：A 股全市场实时快照，适合快速行情、粗筛和估值快照。

输入参数：无

关键字段：

| 字段 | 说明 |
|------|------|
| 代码 | 股票代码 |
| 名称 | 股票名称 |
| 最新价 | 当前最新价 |
| 涨跌幅 | 当日涨跌幅，单位 % |
| 成交额 | 当日成交额，单位元 |
| 换手率 | 当日换手率，单位 % |
| 市盈率-动态 | 动态 PE |
| 市净率 | PB |
| 总市值 | 总市值，单位元 |
| 60日涨跌幅 | 中短期相对强弱参考 |
| 年初至今涨跌幅 | 年内表现参考 |

```python
import akshare as ak

spot = ak.stock_zh_a_spot_em()
target = spot[spot["代码"] == "600519"]
print(target[["代码", "名称", "最新价", "涨跌幅", "成交额", "市盈率-动态", "市净率"]])
```

使用建议：

1. 适合先拿快照，不适合单独用来做长期结论。
2. 盘中数据会变化，回答时要标注数据时点。
3. 做选股时先粗筛，不要直接对全市场逐只深挖。

### stock_zh_a_hist

用途：A 股历史行情，适合趋势分析、收益率、均线、MACD、波动率和阶段表现。

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 股票代码，如 `600519`、`000001` |
| period | str | `daily` / `weekly` / `monthly` |
| start_date | str | 开始日期，格式 `YYYYMMDD` |
| end_date | str | 结束日期，格式 `YYYYMMDD` |
| adjust | str | `""` / `qfq` / `hfq` |

关键字段：

| 字段 | 说明 |
|------|------|
| 日期 | 交易日 |
| 开盘/收盘/最高/最低 | K 线基础字段 |
| 成交量/成交额 | 量价分析基础字段 |
| 振幅 | 波动强弱参考 |
| 涨跌幅 | 单日收益率 |
| 换手率 | 活跃度参考 |

```python
import akshare as ak

hist = ak.stock_zh_a_hist(
    symbol="600519",
    period="daily",
    start_date="20240101",
    end_date="20241231",
    adjust="qfq",
)
print(hist.tail())
```

使用建议：

1. 涉及收益率、均线、MACD 时优先用前复权 `qfq`。
2. 非交易日无数据，不要按自然日逐天请求。
3. 次新股样本不足时，不要强算长周期指标。

### stock_financial_analysis_indicator_em

用途：东财财务分析指标，是股票基本面判断的高频主接口。

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 带市场前缀的代码，如 `SH600519` |
| indicator | str | `按报告期` / `按单季度` |

关键字段：

| 字段 | 说明 |
|------|------|
| TOTALOPERATEREVETZ | 营收同比增速 |
| PARENTNETPROFITTZ | 归母净利润同比增速 |
| ROEJQ | 加权 ROE |
| XSMLL | 毛利率 |
| XSJLL | 净利率 |
| ZCFZL | 资产负债率 |

```python
import akshare as ak

fin = ak.stock_financial_analysis_indicator_em(symbol="SH600519", indicator="按报告期")
print(fin.head())
```

使用建议：

1. 这是报告期数据，不是实时经营快照。
2. 财务结论要注明报告期，避免误导成“当前实时表现”。
3. `symbol` 需要 `SH` / `SZ` 前缀，这是高频易错点。

### stock_individual_fund_flow_rank

用途：看短期主力资金流排名，适合辅助确认情绪和资金方向。

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| indicator | str | `今日` / `3日` / `5日` / `10日` |

关键字段：

| 字段 | 说明 |
|------|------|
| 代码 | 股票代码 |
| 名称 | 股票名称 |
| 主力净流入-净额 | 主力净流入金额 |
| 主力净流入-净占比 | 主力净流入占比 |

```python
import akshare as ak

flow = ak.stock_individual_fund_flow_rank(indicator="5日")
print(flow.head())
```

使用建议：

1. 更适合做确认，不适合单独决定买卖。
2. 短周期资金流波动大，要和趋势或基本面交叉看。

### stock_comment_em

用途：看千股千评类情绪快照，适合补充市场情绪维度。

输入参数：无

关键字段：

| 字段 | 说明 |
|------|------|
| 代码 | 股票代码 |
| 综合得分 | 情绪或评价综合分 |
| 目前排名 | 排名位置 |
| 机构参与度 | 机构关注程度参考 |

```python
import akshare as ak

comment = ak.stock_comment_em()
print(comment.head())
```

使用建议：

1. 情绪数据时效性强，只能做辅助证据。
2. 最好与资金流、价格走势一起使用。

### stock_news_em

用途：查看个股相关新闻，适合解释短期波动或事件驱动。

输入参数：按接口文档传股票代码

优先看字段：`新闻标题`、`发布时间`、`文章来源`

使用建议：

1. 新闻只提供线索，不直接等于基本面变化。
2. 标题党噪音较大，要和价格反应、公告、资金流交叉验证。

### stock_notice_report

用途：查看公告，适合核实分红、业绩预告、融资、风险提示等正式信息。

使用建议：

1. 公告比新闻更适合做事实核验。
2. 如果股价大幅波动，优先检查公告与业绩预告。

## 低频但常用补充接口

### stock_individual_info_em

用途：查上市时间、行业、总股本、流通股本等基础画像。

### stock_zh_a_hist_min_em

用途：分钟级走势，适合盘中结构、短线节奏和精细走势观察。

### stock_hk_spot_em / stock_hk_hist

用途：港股快照和历史走势。

### stock_us_spot_em / stock_us_hist

用途：美股快照和历史走势。

## 结论输出建议

当用户问“这只股票现在怎么看”时，优先输出：

1. 一句话结论
2. 3 条以内核心证据
3. 1 到 2 条反方证据
4. 条件化建议

示例：

```text
结论：当前偏强，但更适合回调观察而不是直接追高。

核心证据：
1. 近 60 日涨幅明显，价格仍在主要均线之上。
2. 动态 PE 高于行业中位数，估值安全边际一般。
3. 最近一期营收和净利仍保持增长。

反方证据：
1. 近 5 日主力资金没有明显持续流入。
2. 财务数据存在报告期滞后。
```

## 常见坑

1. 不要把盘中实时数据说成收盘结论。
2. 不要用不复权价格直接算长期收益率和技术指标。
3. 不要逐只遍历全市场拉历史数据，先粗筛。
4. 不要把财报数据当成“今天的经营状态”。
5. 不要因为拿到一张 DataFrame 就停止分析，用户要的是结论。

---

## 股东数据

### stock_zh_a_gdhs

描述：A股股东户数

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 股票代码，如 "600519" |

```python
import akshare as ak
df = ak.stock_zh_a_gdhs(symbol="600519")
```

---

## ST 股票

### stock_zh_a_st_em

描述：东方财富-A 股 ST 板块实时行情

输入参数：无

```python
import akshare as ak
df = ak.stock_zh_a_st_em()
```

---

## 新股数据

### stock_zh_a_new_em

描述：东方财富-A 股新股实时行情

输入参数：无

```python
import akshare as ak
df = ak.stock_zh_a_new_em()
```
