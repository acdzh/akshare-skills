# 消息面数据

本文件仅说明新闻、公告、热度和研报披露类数据如何获取。

> 规则：优先使用非东方财富来源接口；若同主题只有东方财富可用，才将东方财富接口作为回退或兜底选择。

## 任务路由

| 数据需求 | 目标 | 候选接口（优先非东财） |
|------|------|----------|
| 个股新闻 | 获取个股相关新闻 | `stock_news_em` |
| 公司公告 | 获取正式公告数据 | `stock_notice_report` |
| 研报披露 | 获取研究报告披露数据 | `stock_report_disclosure` |
| 情绪快照 | 获取千股千评类数据 | `stock_comment_em` |
| 热度排行 | 获取个股热度与关键词 | `stock_hot_rank_em` / `stock_hot_rank_detail_em` / `stock_hot_keyword_em` |
| 综合资讯 | 获取财经资讯 | `stock_news_main_cx` |

## 高频接口

### stock_news_em

用途：个股新闻列表。

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 股票代码或关键词，如 `600519` |

关键字段：`新闻标题`、`新闻内容`、`发布时间`、`文章来源`、`新闻链接`

### stock_notice_report

用途：公告列表。

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 股票代码 |

### stock_report_disclosure

用途：研报披露数据。

### stock_comment_em

用途：千股千评快照。

关键字段：`代码`、`名称`、`综合得分`、`机构参与度`、`目前排名`

### stock_comment_detail_zlkp_jgcyd_em

用途：机构参与度历史数据。

### stock_hot_rank_em

用途：个股热度排行。

### stock_hot_rank_detail_em

用途：个股热度历史。

### stock_hot_keyword_em

用途：个股关联热搜关键词。

### stock_hot_rank_latest_em

用途：最新热门股票列表。

### stock_news_main_cx

用途：财经资讯列表。

### stock_hot_follow_xq / stock_hot_tweet_xq / stock_hot_deal_xq / stock_hot_search_baidu

用途：平台热榜原始数据。

## 常见坑

1. 新闻标题和公告标题不是结构化事实，必要时要保留原文链接。
2. 热度排行和平台榜单口径不一致。
3. 消息数据时效性强，输出时建议保留时间字段。
