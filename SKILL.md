---
name: "akshare"
description: "Use akshare to fetch Chinese financial data via Python for investment analysis and decision support. 当用户提问涉及股票、基金、期货、宏观、指数、债券、利率、技术面、基本面、消息面等问题时调用，并产出证据驱动的分析与判断。"
keywords: "akshare, finance, investment, data analysis, decision support, stock, fund, futures, macro economy, indices, bonds, option, fx, bank, energy, interest rate, spot, currency, 股票, 基金, 期货, 宏观经济, 指数, 债券, 期权, 外汇, 银行, 能源, 利率, 现货, 数字货币, 大A, 港股, 美股, 技术分析, 基本面分析, 消息面, K线, 均线, MACD, RSI, KDJ, 布林带, 量价分析, 财务分析, 估值, PE, PB, ROE, 行业分析, 板块, 概念股, 热门股, 龙虎榜, 资金流向, 机构评级, 研报, 涨跌幅, 市盈率, 市净率, 净利润, 营收, 毛利率, GDP, CPI, PMI, LPR, 上证指数, 沪深300, 创业板, 科创板"
---

# AKShare 金融分析与决策支持

当用户咨询投资、交易、市场研判、资产筛选、宏观环境判断等问题时，使用 [AKShare](https://github.com/akfamily/akshare) 获取数据，并基于证据产出清晰结论。这个 skill 的目标不是罗列原始数据，而是帮助 AI 更稳定地完成分析、比较、判断和决策支持。

## 目标

1. **结论导向**：优先回答“怎么看”“怎么选”“该不该做”，而不是只贴数据表。
2. **证据驱动**：每个核心结论都必须有数字、时间范围和数据来源支撑。
3. **允许明确判断**：可以给出方向性观点、优先级排序、条件化建议，不要因过度保守而回避分析。
4. **显式表达不确定性**：不确定时说明缺口、置信度和结论失效条件，而不是停止推断。
5. **优先高频方案**：先用结构化 registry 和 `docs/` 快速命中高频接口，再按需下探原始文档。

## 核心原则

1. **先判断任务，再取数据**：先识别用户要的是行情、趋势、估值、筛选、比较还是决策支持，再决定接口。
2. **至少两类证据交叉验证**：对“值得买吗”“该不该持有”“哪个更优”这类问题，至少同时使用两类证据，例如趋势 + 基本面、估值 + 消息面、宏观 + 利率。
3. **原始数据不是最终答案**：脚本输出应服务于后续推理，不能把 DataFrame 直接当最终回答。
4. **简短风险提示，不弱化判断**：可以提示时效性、波动性、样本限制，但不要用模板化免责声明替代结论。
5. **优先稳定接口**：先使用 `registry/interface_catalog.json` 中定义的高频接口；冷门需求再查 `akshare_docs/`。

## 任务路由

优先查阅 `registry/task_playbooks.json`，按任务目标而不是按资产类别路由：

| 用户意图 | 分析目标 | 优先查阅 |
|----------|----------|----------|
| “现在多少钱” “走势如何” | 快速行情/趋势判断 | `registry/task_playbooks.json` + `docs/stock.md` / `docs/index.md` |
| “技术面怎么样” “支撑压力” | 技术指标与趋势结构 | `registry/task_playbooks.json` + `docs/technical_analysis.md` |
| “基本面如何” “值不值这个估值” | 盈利、成长、估值质量 | `registry/task_playbooks.json` + `docs/fundamental_analysis.md` |
| “最近有什么消息” “情绪热度” | 消息面、热度、资金流 | `registry/task_playbooks.json` + `docs/news_sentiment.md` |
| “综合分析某标的” | 多源证据综合判断 | `registry/task_playbooks.json` + 多个 `docs/*.md` |
| “帮我选股/筛基金” | 条件筛选、排序、候选池 | `registry/task_playbooks.json` + `docs/stock_screening.md` / `docs/fund.md` |
| “大盘/行业怎么走” | 市场环境与风格研判 | `registry/task_playbooks.json` + `docs/index.md` + `docs/macro.md` |
| “画图看看” | 图表辅助说明 | `docs/visualization.md` |

## 查阅顺序

### 第一步：读取结构化 registry

优先读取以下文件，它们是高频任务的第一真源：

| 文件 | 用途 |
|------|------|
| `registry/task_playbooks.json` | 定义高频任务类型、必需证据、推荐接口、输出结构 |
| `registry/interface_catalog.json` | 定义高频接口的场景、参数格式、关键字段、常见坑、回退方案 |

### 第二步：读取 `docs/` 二级文档

当 registry 给出了任务方向后，到 `docs/` 查具体接口说明和示例：

| 文件 | 内容 |
|------|------|
| `docs/stock.md` | A股/港股/美股行情、个股信息、财务数据、资金流向 |
| `docs/fund.md` | 公募基金、ETF、LOF、排行、持仓、规模 |
| `docs/index.md` | 指数行情、历史数据、成份股 |
| `docs/macro.md` | GDP、CPI、PPI、PMI、货币、贸易、就业等 |
| `docs/technical_analysis.md` | 均线、MACD、RSI、KDJ、布林带、量价分析 |
| `docs/fundamental_analysis.md` | 财务指标、三大报表、估值、行业对比 |
| `docs/news_sentiment.md` | 新闻、热度、资金流、概念异动 |
| `docs/stock_screening.md` | 多条件筛选、技术面选股、板块轮动 |
| `docs/visualization.md` | K 线图、指标图、多标的对比图 |

### 第三步：读取 `akshare_docs/` 原始文档

如果需要冷门接口、确认完整字段、核对参数，再查 `akshare_docs/data/`。原始文档很长，应优先用搜索定位接口名，不建议整篇通读。

### 第四步：使用反射验证

当文档与实际接口不一致，或不确定接口是否存在时，直接对 `akshare` 做反射验证：

```python
import akshare as ak
import inspect

print(inspect.signature(ak.stock_zh_a_hist))
print(ak.stock_zh_a_hist.__doc__)

all_funcs = [name for name in dir(ak) if not name.startswith("_")]
print([name for name in all_funcs if "fund" in name.lower()][:30])
```

## 执行流程

1. **定义任务类型**：从 `registry/task_playbooks.json` 选一个最接近的 `task_type`。
2. **列出证据计划**：明确需要哪些维度，例如价格趋势、估值、财务质量、市场热度、宏观环境。
3. **选择接口**：优先使用 `registry/interface_catalog.json` 中的高频接口。
4. **执行一次性 Python 脚本**：脚本负责拉取数据、清洗、计算和输出结构化摘要。
5. **合成结论**：基于结构化摘要写自然语言结论，不把原始表格直接塞给用户。
6. **补充图表**：技术面、趋势对比、行业分布等场景优先生成图表辅助解释。

## 代码规范

### 基本要求

1. **始终使用 `python3` 执行脚本**。
2. **每次使用独立的一次性脚本**，不要依赖上一次运行的状态。
3. **脚本负责证据，不负责长篇叙述**：Python 侧输出结构化摘要，最终文字结论由 AI 组织。
4. **控制调用成本**：优先少量高价值接口，避免全市场逐股深度遍历。
5. **使用 `pandas` 处理数据**，并在输出前压缩成少量关键字段和统计量。
6. **图表统一保存到 `/tmp/`**，并打印图片路径，方便回答时引用。

### 推荐输出格式

优先输出 JSON 风格摘要，解决“数据获取”和“回答组织”冲突：

```python
import json
from datetime import datetime

result = {
    "task_type": "single_stock_decision",
    "symbol": "600519",
    "as_of": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "evidence": {
        "price": {"latest": 0, "pct_chg": 0},
        "trend": {"ma20": 0, "ma60": 0, "macd_dif": 0, "macd_dea": 0},
        "valuation": {"pe_ttm": 0, "pb": 0},
        "fundamental": {"revenue_yoy": 0, "profit_yoy": 0, "roe": 0},
    },
    "bull_points": [],
    "bear_points": [],
    "risks": [],
}
print(json.dumps(result, ensure_ascii=False, default=str))
```

### 推荐辅助函数

```python
import time

def safe_call(func, *args, retries=2, sleep_seconds=1.5, **kwargs):
    for attempt in range(retries + 1):
        try:
            return func(*args, **kwargs)
        except Exception:
            if attempt == retries:
                raise
            time.sleep(sleep_seconds)
```

### Symbol 规范

- A 股行情接口常用 `600519` 这类纯数字代码。
- 东财部分财务接口常用 `SH600519` / `SZ000001`。
- 不确定时先查 registry 中的 `symbol_format`，再对照文档。

## 证据标准

### 个股判断

当用户问“值得买吗”“该不该持有”“要不要减仓”时，默认至少覆盖以下 4 个维度中的 2 个；若用户要求“综合分析”，至少覆盖 3 个维度：

1. **价格与趋势**：实时行情、历史走势、均线、MACD、相对强弱。
2. **估值**：PE、PB、行业相对位置。
3. **基本面**：营收增速、净利增速、ROE、利润率、现金流或资产负债质量。
4. **消息与资金**：新闻热度、千股千评、板块/主力资金流、公告事件。

### 指数与市场环境

当用户问“大盘怎么看”“当前市场风格如何”时，至少组合以下 3 类中的 2 类：

1. **指数走势**：指数现价、阶段涨跌幅、均线结构。
2. **宏观环境**：GDP、CPI、PMI、LPR、SHIBOR 等。
3. **资金与情绪**：行业资金流、热点板块、市场热度。

### 筛选与排序

当用户问“帮我选股/筛基金”时：

1. 先定义筛选逻辑，再跑数据。
2. 先粗筛，再精选，不要无差别遍历全市场。
3. 输出的不只是名单，还要解释“为什么入选”。
4. 最终结果默认输出 Top 5 到 Top 20，而不是全部。

## 回答协议

默认按以下结构组织回答，除非用户明确只要原始结果：

1. **一句话结论**：直接回答“偏多/偏空/中性”“优先/次优/不建议”“适合观察/适合分批/暂不参与”等。
2. **核心证据**：列出 3 到 5 条数字化证据，说明时间范围。
3. **反方证据**：至少给出 1 到 2 个削弱结论的因素。
4. **操作建议**：给出条件化建议，例如“若突破某均线可继续观察”“若估值继续抬升需谨慎”。
5. **置信度**：高 / 中 / 低，并说明为什么。
6. **风险与失效条件**：说明哪些数据变化会让结论失效。

### 回答示例骨架

```text
结论：当前更偏向“可继续观察、但不宜追高”，置信度中等。

核心证据：
1. 近 60 个交易日累计上涨 18%，但最新价仅高于 MA20 约 2%，短期安全边际有限。
2. 动态 PE 为 28 倍，高于行业中位数 21 倍，估值不便宜。
3. 最近一期营收同比增长 24%，净利润同比增长 31%，基本面仍然较强。

反方证据：
1. 近 5 日主力资金净流出。
2. 财务数据对应的是上一个报告期，存在滞后。

操作建议：
- 如果是空仓：更适合等回踩关键均线或估值回落后再看。
- 如果已持有：趋势未破坏前可继续跟踪，但要关注量能和资金流。
```

## 数据质量与常见坑

| 场景 | 问题 | 处理方式 |
|------|------|----------|
| 复权选择 | 不复权数据在除权日出现跳空，收益率和技术指标失真 | 涉及收益率、均线、MACD 等计算时优先使用前复权 `adjust="qfq"` |
| 非交易日 | 周末和节假日无数据 | 使用交易日范围，不要按自然日逐日遍历 |
| 财务滞后 | 财务数据按报告期披露，不代表实时经营状态 | 在回答里明确报告期，避免把历史财务当成当前现实 |
| 盘中快照 | 实时行情在盘中会持续变化 | 标注数据时间，避免把盘中数据说成收盘定论 |
| ST/退市股 | 涨跌停制度和流动性特征不同 | 筛选场景默认排除 `ST|退` |
| 新股/次新股 | 上市时间短，均线和历史统计不稳定 | 计算长周期指标前先确认样本长度 |

## 限流与性能

1. 循环请求时加入 `time.sleep(0.3 ~ 0.8)`。
2. 单次脚本尽量控制在 20 次以内 API 调用。
3. 优先“快照粗筛 + 少量深挖”，不要先遍历全市场再逐个取历史。
4. 批量任务时先想办法用单接口取全量快照，而不是用 100 个单标的接口拼起来。

## 降级策略

### 接口不存在或命名变更

1. 先用 `inspect.signature()` 和 `dir(ak)` 检查接口是否存在。
2. 在同主题文档中搜索候选替代接口。
3. 如果找到替代接口，说明“已降级为相近口径的数据源”。
4. 如果找不到，仍应尽可能基于已拿到的数据给出局部结论，并说明缺失维度。

### 数据为空

依次检查：

1. 日期是否为交易日。
2. `symbol` 格式是否匹配接口要求。
3. 当前市场是否休市。
4. 是否因筛选条件过严导致结果为空。

### 环境缺失

如果缺少依赖：

```bash
pip install akshare pandas
```

## 图表规则

技术分析、趋势对比、行业分布、资金流向等场景推荐配图，遵循：

1. `matplotlib.use("Agg")`
2. 图片保存在 `/tmp/`
3. 生成后打印图片路径
4. 重要图表包括时间范围、标题和关键指标标注
5. 最终回答引用图表时要解释图表，不要只贴图片

## 文件说明

| 文件 | 作用 |
|------|------|
| `registry/task_playbooks.json` | 高优先级任务剧本 |
| `registry/interface_catalog.json` | 高频接口目录 |
| `docs/*.md` | 主题文档 |
| `akshare_docs/data/**/*.md` | 上游原始文档 |
| `scripts/validate_skill_docs.py` | registry 与接口可用性校验脚本 |

## 最重要的行为要求

1. 不要把“风险提示”写成“拒绝分析”。
2. 不要把“展示数据”误当成“完成任务”。
3. 不要在证据不足时假装确定，但也不要因为不完美就不给判断。
4. 优先产出“可执行、可解释、可复核”的结论。
