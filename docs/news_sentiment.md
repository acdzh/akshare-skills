# 消息面分析

当用户提问涉及消息面/情绪面分析（个股新闻、市场热度、机构评级、概念板块异动等）时，基于 akshare 获取资讯和情绪数据进行分析。

## 个股新闻

### stock_news_em

描述：东方财富-个股新闻资讯（最近 100 条）

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 股票代码或关键词，如 "600519" |

输出参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| 关键词 | object | - |
| 新闻标题 | object | - |
| 新闻内容 | object | 正文摘要 |
| 发布时间 | object | - |
| 文章来源 | object | - |
| 新闻链接 | object | - |

```python
import akshare as ak
df = ak.stock_news_em(symbol="600519")
print(df[['新闻标题', '发布时间', '文章来源']].head(20).to_string(index=False))
```

---

## 财经资讯

### stock_news_main_cx

描述：财新网-最新财经资讯（100 条）

输入参数：无

输出参数：tag(分类)、summary(摘要)、url(链接)

```python
import akshare as ak
df = ak.stock_news_main_cx()
print(df[['tag', 'summary']].head(20).to_string(index=False))
```

---

## 千股千评（市场综合评价）

### stock_comment_em

描述：东方财富-千股千评（含机构参与度、综合得分、排名）

输入参数：无

输出参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| 代码 | object | - |
| 名称 | object | - |
| 最新价 | float64 | - |
| 涨跌幅 | float64 | - |
| 换手率 | float64 | % |
| 市盈率 | float64 | - |
| 主力成本 | float64 | - |
| 机构参与度 | float64 | - |
| 综合得分 | float64 | 0-100 |
| 目前排名 | int64 | - |
| 关注指数 | float64 | - |

```python
import akshare as ak
df = ak.stock_comment_em()
# 筛选个股
target = df[df['代码'] == '600519']
print(target[['代码', '名称', '综合得分', '机构参与度', '目前排名']].to_string(index=False))
```

### stock_comment_detail_zlkp_jgcyd_em

描述：东方财富-千股千评-机构参与度历史

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 股票代码，如 "600519" |

```python
import akshare as ak
df = ak.stock_comment_detail_zlkp_jgcyd_em(symbol="600519")
```

---

## 市场热度

### stock_hot_rank_em

描述：东方财富-个股人气榜（热度排名）

输入参数：无

```python
import akshare as ak
df = ak.stock_hot_rank_em()
print(df.head(20).to_string(index=False))
```

### stock_hot_rank_detail_em

描述：东方财富-个股热度历史趋势

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 股票代码，如 "SZ000665" (需带市场前缀) |

```python
import akshare as ak
df = ak.stock_hot_rank_detail_em(symbol="SZ000665")
```

### stock_hot_keyword_em

描述：东方财富-热搜关键词

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 股票代码，如 "SZ000665" |

```python
import akshare as ak
df = ak.stock_hot_keyword_em(symbol="SZ000665")
```

### stock_hot_rank_latest_em

描述：东方财富-最新热门股票

输入参数：无

```python
import akshare as ak
df = ak.stock_hot_rank_latest_em()
```

---

## 雪球热度

### stock_hot_follow_xq

描述：雪球-关注排行榜

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | "最热门" / "本周新增" |

```python
import akshare as ak
df = ak.stock_hot_follow_xq(symbol="最热门")
```

### stock_hot_tweet_xq

描述：雪球-讨论排行榜

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | "最热门" / "本周新增" |

```python
import akshare as ak
df = ak.stock_hot_tweet_xq(symbol="最热门")
```

### stock_hot_deal_xq

描述：雪球-交易排行榜

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | "最热门" / "本周新增" |

```python
import akshare as ak
df = ak.stock_hot_deal_xq(symbol="最热门")
```

---

## 百度热搜

### stock_hot_search_baidu

描述：百度-股票热搜榜

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| date | str | 日期，如 "20241220" |

```python
import akshare as ak
df = ak.stock_hot_search_baidu(date="20241220")
```

---

## 公告/研报

### stock_notice_report

描述：东方财富-个股公告

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 股票代码，如 "600519" |

```python
import akshare as ak
df = ak.stock_notice_report(symbol="600519")
```

### stock_report_disclosure

描述：东方财富-研究报告披露

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 股票代码 |

```python
import akshare as ak
df = ak.stock_report_disclosure(symbol="600519")
```

---

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
