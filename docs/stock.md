# 股票数据

本文件仅说明股票相关数据如何获取、字段代表什么、常见口径差异在哪里。

## 任务路由

| 数据需求 | 目标 | 优先接口 |
|------|------|----------|
| 实时行情 | 获取最新价、涨跌幅、成交额、估值快照 | `stock_zh_a_spot_em` |
| 历史行情 | 获取日线、周线、月线历史数据 | `stock_zh_a_hist` |
| 分钟数据 | 获取盘中分钟级序列 | `stock_zh_a_hist_min_em` |
| 基础画像 | 获取行业、上市时间、市值等信息 | `stock_individual_info_em` |
| 资金流 | 获取个股资金流或资金流排名数据 | `stock_individual_fund_flow` / `stock_individual_fund_flow_rank` |
| 港股/美股行情 | 获取港股、美股快照与历史 | `stock_hk_spot_em` / `stock_hk_hist` / `stock_us_spot_em` / `stock_us_hist` |

## 高频接口

### stock_zh_a_spot_em

用途：A 股全市场实时快照。

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

```python
import akshare as ak
spot = ak.stock_zh_a_spot_em()
print(spot[["代码", "名称", "最新价", "涨跌幅", "成交额"]].head())
```

### stock_zh_a_hist

用途：A 股历史行情。

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 股票代码，如 `600519` |
| period | str | `daily` / `weekly` / `monthly` |
| start_date | str | `YYYYMMDD` |
| end_date | str | `YYYYMMDD` |
| adjust | str | `""` / `qfq` / `hfq` |

关键字段：`日期`、`开盘`、`收盘`、`最高`、`最低`、`成交量`、`成交额`、`涨跌幅`、`换手率`

```python
import akshare as ak
hist = ak.stock_zh_a_hist(symbol="600519", period="daily", start_date="20240101", end_date="20241231", adjust="qfq")
print(hist.tail())
```

### stock_zh_a_hist_min_em

用途：A 股分钟级历史行情。

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 股票代码，如 `000001` |
| period | str | `1` / `5` / `15` / `30` / `60` |
| start_date | str | `YYYY-MM-DD HH:MM:SS` |
| end_date | str | `YYYY-MM-DD HH:MM:SS` |
| adjust | str | `""` / `qfq` / `hfq` |

### stock_individual_info_em

用途：个股基础信息。

### stock_individual_fund_flow

用途：个股资金流明细。

### stock_individual_fund_flow_rank

用途：个股资金流排名数据。

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| indicator | str | `今日` / `3日` / `5日` / `10日` |

### stock_hk_spot_em / stock_hk_hist

用途：港股快照和历史行情。

### stock_us_spot_em / stock_us_hist

用途：美股快照和历史行情。

## 常见坑

1. 涉及收益率和技术指标时优先使用前复权 `qfq`。
2. 盘中实时快照会变化，建议保留抓取时间。
3. 非交易日无历史数据。
4. 不同接口对 `symbol` 是否带市场前缀要求不同。
