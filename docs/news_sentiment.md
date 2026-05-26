# 消息面分析

本文件服务于 3 类高频任务：

1. 判断某只股票近期是不是有事件驱动。
2. 判断市场或板块当前的热度、情绪和资金关注度。
3. 为“综合分析个股/市场环境”补充情绪与事件证据。

消息面数据的价值不在于“新闻越多越好”，而在于帮助解释价格行为、资金行为和预期变化。

## 任务路由

| 任务 | 目标 | 优先接口 |
|------|------|----------|
| 个股事件核查 | 看新闻、公告、研报披露 | `stock_news_em` + `stock_notice_report` + `stock_report_disclosure` |
| 情绪快照 | 看市场对个股的关注与评价 | `stock_comment_em` |
| 热度趋势 | 看个股热度变化和关键词 | `stock_hot_rank_em` + `stock_hot_rank_detail_em` + `stock_hot_keyword_em` |
| 市场风格/题材热度 | 看热门股和平台热榜 | `stock_hot_rank_latest_em` + 雪球/百度热榜接口 |
| 宏观资讯补充 | 看重要财经资讯 | `stock_news_main_cx` |

## 推荐工作流

### 个股消息面判断

1. 先查 `stock_news_em`，看近几天是否有明显事件。
2. 再查 `stock_notice_report`，确认是否有正式公告支撑。
3. 如果市场热度明显升温，再补 `stock_hot_rank_detail_em` 或 `stock_hot_keyword_em`。
4. 最后用一句话判断这是“基本面事件”“题材催化”还是“情绪噪音”。

### 情绪与热度判断

至少交叉 2 类数据：

1. 新闻/公告
2. 千股千评或热度排名
3. 平台热榜

不要只因为某股上了热榜就下结论，也不要把新闻标题直接当成事实。

## 高频接口

### stock_news_em

用途：查看个股最近一批新闻，适合识别事件驱动和舆情变化。

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 股票代码或关键词，如 `600519` |

关键字段：

| 字段 | 说明 |
|------|------|
| 新闻标题 | 事件摘要 |
| 新闻内容 | 正文摘要 |
| 发布时间 | 时间信息 |
| 文章来源 | 来源 |
| 新闻链接 | 原文地址 |

```python
import akshare as ak

news = ak.stock_news_em(symbol="600519")
print(news[["新闻标题", "发布时间", "文章来源"]].head(10))
```

使用建议：

1. 先按时间排序，优先看最近 3 到 10 条。
2. 先识别是业绩、公告、监管、产品、行业政策还是市场传闻。
3. 只把它当线索，不把它直接当结论。

### stock_notice_report

用途：查看公司公告，适合确认正式事件和风险提示。

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 股票代码，如 `600519` |

```python
import akshare as ak

notice = ak.stock_notice_report(symbol="600519")
print(notice.head())
```

使用建议：

1. 公告优先级通常高于新闻标题。
2. 出现大涨大跌时，优先检查是否有业绩预告、分红、融资、减持、风险提示等公告。

### stock_report_disclosure

用途：查看研报披露，适合补充机构关注与一致预期变化。

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 股票代码 |

### stock_comment_em

用途：获取千股千评快照，适合补充综合得分、机构参与度和市场关注度。

输入参数：无

关键字段：

| 字段 | 说明 |
|------|------|
| 代码 | 股票代码 |
| 综合得分 | 情绪综合分 |
| 机构参与度 | 机构关注程度参考 |
| 目前排名 | 相对排名 |
| 关注指数 | 关注度参考 |

```python
import akshare as ak

comment = ak.stock_comment_em()
target = comment[comment["代码"] == "600519"]
print(target[["代码", "名称", "综合得分", "机构参与度", "目前排名"]])
```

使用建议：

1. 只适合做辅助确认，不适合作为唯一判断依据。
2. 最好与新闻、价格和资金流一起看。

### stock_comment_detail_zlkp_jgcyd_em

用途：查看机构参与度历史，适合观察情绪是否持续升温或降温。

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 股票代码，如 `600519` |

### stock_hot_rank_em

用途：查看个股人气榜，适合识别市场热度聚焦方向。

输入参数：无

```python
import akshare as ak

hot = ak.stock_hot_rank_em()
print(hot.head(20))
```

使用建议：

1. 热度只能说明关注，不说明方向正确。
2. 热度大增时要区分是业绩催化还是情绪炒作。

### stock_hot_rank_detail_em

用途：查看个股热度历史趋势，适合判断热度是突发拉升还是持续升温。

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 带市场前缀的股票代码，如 `SZ000665` |

### stock_hot_keyword_em

用途：看个股关联热搜关键词，适合快速识别当前市场在交易什么叙事。

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 带市场前缀的股票代码，如 `SZ000665` |

### stock_hot_rank_latest_em

用途：看最新热门股票，适合补充短线情绪快照。

输入参数：无

### stock_news_main_cx

用途：看综合财经资讯，适合解释宏观事件或行业事件。

输入参数：无

## 平台热榜补充

### stock_hot_follow_xq / stock_hot_tweet_xq / stock_hot_deal_xq

用途：分别看雪球关注、讨论、交易排行榜，适合观察散户平台情绪。

### stock_hot_search_baidu

用途：看百度热搜，适合识别大众关注度。

使用建议：

1. 平台热榜更适合判断情绪，不适合判断价值。
2. 平台间口径差异较大，最好不要单独引用一个榜单做强结论。

## 结论输出建议

当用户问“最近这只股票消息面怎么样”时，建议按以下结构输出：

1. 一句话判断
2. 关键事件
3. 情绪热度变化
4. 对价格的潜在影响
5. 需要警惕的噪音或不确定性

示例：

```text
结论：近期消息面偏积极，但更像“事件催化 + 情绪升温”，还需要后续业绩或公告继续验证。

核心证据：
1. 最近几天出现多条与业绩/产品/订单相关的新闻。
2. 个股热度排名上升，关键词集中在同一条主线。
3. 公告层面没有看到明显利空。

不确定性：
1. 目前热度上升可能带有短线资金博弈成分。
2. 如果后续没有正式业绩或公告兑现，情绪可能回落。
```

## 常见坑

1. 不要把新闻标题直接当事实。
2. 不要把热榜排名直接当买入理由。
3. 不要忽略公告与新闻的优先级差异。
4. 不要把情绪数据当长期价值判断依据。
5. 用户要的是“这条消息意味着什么”，不是一串资讯列表。

## 盈利预测与评级

### stock_profit_forecast_em

描述：东方财富-机构盈利预测（含评级汇总：买入/增持/中性/减持/卖出）

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 空字符串获取全部，或行业名如 "白酒" |

```python
import akshare as ak
df = ak.stock_profit_forecast_em()
# 查看特定股票的机构一致预期
target = df[df['代码'] == '600519']
```

---

## 板块资金流向

### stock_sector_fund_flow_rank

描述：东方财富-板块资金流向排名

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| indicator | str | "今日"/"5日"/"10日" |
| sector_type | str | "行业资金流"/"概念资金流"/"地区资金流" |

```python
import akshare as ak
df = ak.stock_sector_fund_flow_rank(indicator="今日", sector_type="行业资金流")
print(df.head(20).to_string(index=False))
```

### stock_concept_fund_flow_hist

描述：东方财富-概念板块资金流向历史

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 概念板块名 |

```python
import akshare as ak
df = ak.stock_concept_fund_flow_hist(symbol="人工智能")
```

---

## 概念板块异动

### stock_board_concept_spot_em

描述：东方财富-概念板块实时行情

输入参数：无

```python
import akshare as ak
df = ak.stock_board_concept_spot_em()
# 按涨跌幅排序看当日热门概念
print(df.sort_values('涨跌幅', ascending=False).head(10)[['板块名称', '涨跌幅', '总市值', '换手率']].to_string(index=False))
```

### stock_board_concept_hist_em

描述：东方财富-概念板块历史行情

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 概念板块名 |
| period | str | "daily"/"weekly"/"monthly" |
| start_date | str | "20240101" |
| end_date | str | "20241231" |
| adjust | str | "" |

```python
import akshare as ak
df = ak.stock_board_concept_hist_em(symbol="人工智能", period="daily", start_date="20240101", end_date="20241231", adjust="")
```

---

## 消息面分析模板

```python
import akshare as ak
import pandas as pd

def news_sentiment_analysis(symbol):
    """个股消息面综合分析"""
    print(f"=== {symbol} 消息面分析 ===\n")

    # 1. 最新新闻
    news = ak.stock_news_em(symbol=symbol)
    print("【近期新闻】")
    print(news[['新闻标题', '发布时间']].head(10).to_string(index=False))

    # 2. 千股千评
    comments = ak.stock_comment_em()
    stock_comment = comments[comments['代码'] == symbol]
    if not stock_comment.empty:
        row = stock_comment.iloc[0]
        print(f"\n【千股千评】")
        print(f"  综合得分: {row['综合得分']}  排名: {row['目前排名']}  机构参与度: {row['机构参与度']}")

    # 3. 机构预测
    forecast = ak.stock_profit_forecast_em()
    stock_fc = forecast[forecast['代码'] == symbol]
    if not stock_fc.empty:
        row = stock_fc.iloc[0]
        print(f"\n【机构预测】")
        print(f"  研报数: {row['研报数']}  买入: {row.get('机构投资评级(近六个月)-买入', 'N/A')}  增持: {row.get('机构投资评级(近六个月)-增持', 'N/A')}")

news_sentiment_analysis("600519")
```

---

## 分析回答规范

1. **新闻摘要**：提取关键新闻标题和时间，概括近期舆论方向
2. **情绪量化**：利用热度排名、关注指数、讨论量等量化市场关注度
3. **机构态度**：结合盈利预测、评级汇总判断机构看法
4. **板块联动**：关注所属概念板块的资金流向和异动情况
5. **风险提示**：消息面分析具有时效性，市场情绪变化快，不构成投资建议
