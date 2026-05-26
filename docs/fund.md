# 基金数据

本文件服务于 3 类高频任务：

1. 回答“这只基金/ETF 最近表现如何”。
2. 比较多只基金并给出排序建议。
3. 结合净值、持仓、经理、规模判断基金是否适合某类需求。

基金分析和股票分析不同，重点不是盘中波动，而是收益表现、风格暴露、持仓结构和适配场景。

## 任务路由

| 任务 | 目标 | 优先接口 |
|------|------|----------|
| 基金检索 | 找代码、名称、类型 | `fund_name_em` |
| 开放式基金分析 | 看净值走势、累计收益、同类排名 | `fund_open_fund_info_em` |
| ETF 快照 | 看盘中价格和成交活跃度 | `fund_etf_spot_em` |
| ETF 趋势 | 看历史行情与阶段表现 | `fund_etf_hist_em` |
| 基金筛选 | 看排行、类型、规模、风格 | `fund_open_fund_rank_em` / `fund_exchange_rank_em` |
| 风格验证 | 看持仓结构、经理画像 | `fund_portfolio_hold_em` + `fund_manager_em` |

## 推荐工作流

### 单只基金判断

1. 先确认基金类型和代码。
2. 用净值或历史行情看表现。
3. 用持仓和基金经理判断风格是否匹配。
4. 再给出“更适合什么场景”的建议，而不是只说涨了多少。

### 多基金比较

至少比较以下 3 个维度中的 2 个：

1. 历史收益或净值走势
2. 持仓与风格暴露
3. 管理人/规模/流动性

### ETF 与开放式基金的区别

1. ETF 更像场内交易工具，盘中价格与成交活跃度很重要。
2. 开放式基金更适合看净值、累计收益、同类排名和持仓风格。
3. 不要把 ETF 实时价格和开放式基金净值混为一谈。

## 高频接口

### fund_name_em

用途：基金基础信息检索，适合先定位基金代码、名称和类型。

输入参数：无

关键字段：

| 字段 | 说明 |
|------|------|
| 基金代码 | 基金唯一代码 |
| 基金简称 | 基金名称 |
| 基金类型 | 股票型、混合型、债券型、指数型等 |

```python
import akshare as ak

funds = ak.fund_name_em()
print(funds.head())
```

### fund_open_fund_info_em

用途：开放式基金净值走势、累计收益、同类排名等，是开放式基金分析主接口。

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 基金代码，如 `110011` |
| indicator | str | `单位净值走势` / `累计净值走势` / `累计收益率走势` / `同类排名走势` / `同类排名百分比` 等 |

常用 `indicator`：

1. `累计净值走势`
2. `累计收益率走势`
3. `同类排名走势`
4. `同类排名百分比`

```python
import akshare as ak

nav = ak.fund_open_fund_info_em(symbol="110011", indicator="累计净值走势")
print(nav.tail())
```

使用建议：

1. 看长期表现优先用累计净值或累计收益率。
2. 看相对强弱时补同类排名，不只看绝对收益。
3. 回答里最好说明观察区间。

### fund_open_fund_daily_em

用途：获取开放式基金日度数据，适合做同类型横向比较。

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| fund_type | str | `全部` / `股票型` / `混合型` / `债券型` / `指数型` / `QDII` / `FOF` |

```python
import akshare as ak

daily = ak.fund_open_fund_daily_em(fund_type="股票型")
print(daily.head())
```

使用建议：

1. 适合先按类型筛出候选。
2. 结果适合横向比较，不适合作为单只基金的完整画像。

### fund_etf_spot_em

用途：ETF 盘中实时快照，适合看最新价、涨跌幅、成交额和流动性。

输入参数：无

关键字段通常包括：`代码`、`名称`、`最新价`、`涨跌幅`、`成交额`

```python
import akshare as ak

etf_spot = ak.fund_etf_spot_em()
print(etf_spot.head())
```

使用建议：

1. 适合回答“现在 ETF 价格怎样”。
2. 不要把盘中价格当成基金净值。

### fund_etf_hist_em

用途：ETF 历史行情，适合趋势判断、区间收益和回撤观察。

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | ETF 代码，如 `510300` |
| period | str | `daily` / `weekly` / `monthly` |
| start_date | str | `YYYYMMDD` |
| end_date | str | `YYYYMMDD` |
| adjust | str | `""` / `qfq` / `hfq` |

```python
import akshare as ak

hist = ak.fund_etf_hist_em(
    symbol="510300",
    period="daily",
    start_date="20240101",
    end_date="20241231",
    adjust="qfq",
)
print(hist.tail())
```

### fund_lof_spot_em

用途：LOF 实时行情，适合场内基金快照。

输入参数：无

### fund_open_fund_rank_em

用途：开放式基金排行，适合先找同类型中的高收益候选。

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | `全部` / `股票型` / `混合型` / `债券型` / `指数型` / `QDII` / `FOF` |

```python
import akshare as ak

rank_df = ak.fund_open_fund_rank_em(symbol="混合型")
print(rank_df.head())
```

使用建议：

1. 排行是入口，不是终点。
2. 排名前列的基金仍要补查持仓和风格，避免只追短期业绩。

### fund_exchange_rank_em

用途：场内基金排行，适合 ETF / LOF 等场内产品横向比较。

输入参数：无

### fund_portfolio_hold_em

用途：看股票持仓，判断基金风格、行业暴露和重仓集中度。

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 基金代码，如 `110011` |
| date | str | 报告期年份，如 `2024` |

```python
import akshare as ak

holdings = ak.fund_portfolio_hold_em(symbol="110011", date="2024")
print(holdings.head())
```

使用建议：

1. 持仓能解释基金为什么涨跌，不只是“最近收益是多少”。
2. 这是披露口径，存在滞后。

### fund_manager_em

用途：看基金经理履历、管理规模和历史表现，辅助判断管理稳定性。

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 基金代码 |

```python
import akshare as ak

manager = ak.fund_manager_em(symbol="110011")
print(manager.head())
```

### fund_aum_em

用途：看基金公司管理规模，辅助判断平台能力和规模画像。

### fund_value_estimation_em

用途：看基金盘中估算值，适合补充实时感知。

使用建议：

1. 估算值不是正式净值。
2. 适合做参考，不适合作为唯一判断依据。

## 低频但常用补充接口

### fund_portfolio_bond_hold_em

用途：债券持仓，适合分析债券基金或固收+产品。

### fund_money_fund_daily_em

用途：货币基金日度数据，适合低风险现金管理场景。

### fund_etf_fund_daily_em / fund_etf_fund_info_em

用途：ETF 净值相关补充口径，适合和场内价格做对照。

## 结论输出建议

当用户问“这只基金值得买吗”时，建议按以下方式组织：

1. 一句话结论
2. 表现证据
3. 风格或持仓证据
4. 适合什么类型的用户或场景
5. 主要风险

示例：

```text
结论：更适合中长期跟踪，不适合把它当短线交易工具。

核心证据：
1. 近一年累计收益在同类中排名靠前。
2. 重仓方向集中在高景气赛道，风格鲜明。
3. 基金经理管理时间较长，风格相对稳定。

主要风险：
1. 持仓集中度高，回撤可能偏大。
2. 持仓披露有滞后，当前实际仓位可能已变化。
```

## 常见坑

1. 不要把 ETF 盘中价格和开放式基金净值混在一起。
2. 不要只看短期收益排行就下结论。
3. 不要忽略基金类型差异，股票型和债券型不可直接横比。
4. 不要把持仓披露当成实时仓位。
5. 用户要的是“适不适合”和“为什么”，不是一串净值表。

### fund_aum_em

描述：东方财富-基金公司管理规模排名

输入参数：无

```python
import akshare as ak
df = ak.fund_aum_em()
```

### fund_scale_change_em

描述：东方财富-基金规模变动

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 基金代码 |

```python
import akshare as ak
df = ak.fund_scale_change_em(symbol="110011")
```

---

## 基金分红

### fund_fh_em

描述：东方财富-基金分红数据

输入参数：无

```python
import akshare as ak
df = ak.fund_fh_em()
```

---

## 基金评级

### fund_rating_all

描述：天天基金-基金评级（综合）

输入参数：无

```python
import akshare as ak
df = ak.fund_rating_all()
```

---

## 基金估值

### fund_value_estimation_em

描述：东方财富-基金估值（盘中实时估算净值）

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 基金代码 |

```python
import akshare as ak
df = ak.fund_value_estimation_em(symbol="110011")
```
