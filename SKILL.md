---
name: "akshare"
description: "Use akshare to fetch Chinese financial data via Python. 当用户提问涉及股票、基金、期货、宏观、指数、债券、利率、技术指标、基本面、消息面等数据查询时调用。"
keywords: "akshare, finance, stock, fund, futures, macro, indices, bonds, option, fx, bank, energy, interest rate, spot, currency, 股票, 基金, 期货, 宏观经济, 指数, 债券, 期权, 外汇, 银行, 能源, 利率, 现货, 数字货币, K线, 均线, MACD, RSI, KDJ, 布林带, 财务分析, 估值, PE, PB, ROE, 行业分析, 板块, 热门股, 龙虎榜, 资金流向, 机构评级, 研报, 涨跌幅, 市盈率, 市净率, 净利润, 营收, 毛利率, GDP, CPI, PMI, LPR, 上证指数, 沪深300, 创业板, 科创板"
---

# AKShare 金融数据获取

当用户需要查询金融数据、历史序列、财务指标、消息资讯、基金信息、宏观指标等内容时，使用 [AKShare](https://github.com/akfamily/akshare) 获取并整理数据。此 skill 仅负责数据获取、字段说明、口径说明和必要的数据清洗，不负责行情解读、标的选择或图形输出。

## 适用范围

1. 行情快照：股票、指数、基金、期货、外汇、债券等。
2. 历史数据：日线、周线、月线、部分分钟级数据。
3. 基本面数据：财务指标、三大报表、估值、行业对比所需原始字段。
4. 消息数据：新闻、公告、热度、研报披露。
5. 宏观数据：GDP、CPI、PPI、PMI、LPR、SHIBOR、进出口等。

## 任务路由

| 用户需求 | 数据目标 | 优先文档 |
|----------|----------|----------|
| “现在多少钱” “最新行情” | 实时快照 | `docs/stock.md` / `docs/index.md` / `docs/fund.md` |
| “历史走势数据” “K线数据” | 历史价格序列 | `docs/stock.md` / `docs/index.md` / `docs/fund.md` / `docs/technical_analysis.md` |
| “财务数据” “估值指标” | 基本面字段 | `docs/fundamental_analysis.md` |
| “新闻公告热度” | 消息面原始数据 | `docs/news_sentiment.md` |
| “基金净值/持仓/经理” | 基金相关数据 | `docs/fund.md` |
| “GDP/CPI/利率/PMI” | 宏观指标 | `docs/macro.md` |

## 查阅顺序

### 第一步：读取结构化 registry

| 文件 | 用途 |
|------|------|
| `registry/task_playbooks.json` | 数据查询任务和高频接口映射 |
| `registry/interface_catalog.json` | 高频接口的参数格式、关键字段、常见坑和回退方案 |

### 第二步：读取 `docs/` 主题文档

| 文件 | 内容 |
|------|------|
| `docs/stock.md` | 股票行情、历史序列、基础信息、资金流 |
| `docs/fund.md` | 基金列表、净值、ETF/LOF、持仓、经理 |
| `docs/index.md` | 指数快照、历史、成份股 |
| `docs/macro.md` | 宏观指标和利率数据 |
| `docs/technical_analysis.md` | 技术指标所需历史数据和计算模板 |
| `docs/fundamental_analysis.md` | 财务指标、三表、估值、行业对比 |
| `docs/news_sentiment.md` | 新闻、公告、热度、研报披露 |

### 第三步：读取 `akshare_docs/` 原始文档

需要冷门接口、完整字段或参数确认时，再查 `akshare_docs/data/`。

### 第四步：使用反射验证

当文档与实际接口不一致时，直接检查 `akshare`：

```python
import akshare as ak
import inspect

print(inspect.signature(ak.stock_zh_a_hist))
print(ak.stock_zh_a_hist.__doc__)
```

## 执行流程

1. 先确定用户要的是哪类数据。
2. 从 `registry/task_playbooks.json` 找对应的数据任务。
3. 从 `registry/interface_catalog.json` 选高频接口。
4. 编写一次性 Python 脚本拉取数据并做最小清洗。
5. 输出关键字段、少量样例行或结构化摘要。

## 代码规范

1. 始终使用 `python3` 执行脚本。
2. 每次使用独立的一次性脚本，不依赖历史状态。
3. 脚本只做数据获取、清洗、筛字段和简单统计，不生成图表，不输出结论模板。
4. 优先打印关键字段，不要整表无节制输出。
5. 使用 `pandas` 处理数据。
6. 历史价格涉及收益率或技术指标时，优先使用前复权 `adjust="qfq"`。

### 推荐输出形式

```python
import json
from datetime import datetime

result = {
    "task_type": "fundamental_data",
    "symbol": "SH600519",
    "as_of": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "fields": ["ROEJQ", "TOTALOPERATEREVETZ", "PARENTNETPROFITTZ"],
    "rows": []
}
print(json.dumps(result, ensure_ascii=False, default=str))
```

## 数据质量与常见坑

| 场景 | 问题 | 处理方式 |
|------|------|----------|
| 复权选择 | 不复权价格在除权日会失真 | 涉及收益率和技术指标时优先使用前复权 |
| 非交易日 | 周末和节假日无数据 | 使用交易日范围 |
| 财务滞后 | 财务数据按报告期披露 | 输出时保留报告期字段 |
| 盘中快照 | 实时行情会变化 | 标注抓取时间 |
| symbol 格式 | 不同接口要求不同 | 优先查 `interface_catalog.json` |

## 降级策略

1. 接口不存在时，先用 `dir(ak)` 和 `inspect.signature()` 验证。
2. 如果主接口不可用，改用同主题回退接口。
3. 如果返回为空，检查日期、交易日和 `symbol` 格式。

## 环境缺失

```bash
pip install akshare pandas
```

## 文件说明

| 文件 | 作用 |
|------|------|
| `registry/task_playbooks.json` | 数据任务映射 |
| `registry/interface_catalog.json` | 高频接口目录 |
| `docs/*.md` | 主题数据文档 |
| `akshare_docs/data/**/*.md` | 上游原始文档 |
| `scripts/validate_skill_docs.py` | 结构校验脚本 |
