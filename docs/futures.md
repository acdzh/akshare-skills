# 期货数据

## 期货交易所

| 交易所 | 代码 | 品种举例 |
|--------|------|----------|
| 中国金融期货交易所 | CFFEX | 股指期货(IF/IH/IC/IM)、国债期货(T/TF/TS) |
| 上海期货交易所 | SHFE | 铜cu、铝al、黄金au、白银ag、螺纹钢rb、热卷hc |
| 上海国际能源交易中心 | INE | 原油sc、20号胶nr、国际铜bc |
| 大连商品交易所 | DCE | 铁矿石i、焦炭j、焦煤jm、豆粕m、玉米c |
| 郑州商品交易所 | CZCE | 甲醇MA、纯碱SA、玻璃FG、棉花CF、白糖SR |
| 广州期货交易所 | GFEX | 工业硅SI、碳酸锂LC |

---

## 国内期货实时行情

### futures_zh_spot

描述：新浪-国内期货实时行情数据

输入参数：无

输出参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| 代码 | object | 合约代码 |
| 名称 | object | - |
| 最新价 | float64 | - |
| 涨跌额 | float64 | - |
| 涨跌幅 | float64 | - |
| 买价 | float64 | - |
| 卖价 | float64 | - |
| 昨结 | float64 | - |
| 持仓量 | float64 | - |
| 成交量 | float64 | - |

```python
import akshare as ak
df = ak.futures_zh_spot()
```

---

## 期货历史行情

### futures_zh_daily_sina

描述：新浪-期货历史行情（日线）

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 合约代码，如 "RB2501"(螺纹钢2501)、"AU2412"(黄金2412) |

输出参数：date, open, high, low, close, volume, hold

```python
import akshare as ak
df = ak.futures_zh_daily_sina(symbol="RB2501")
```

### futures_main_sina

描述：新浪-期货主力连续合约历史数据

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 品种代码，如 "RB0"(螺纹钢主力)、"AU0"(黄金主力)、"I0"(铁矿石主力) |
| start_date | str | "20240101" |
| end_date | str | "20241231" |

输出参数：date, open, high, low, close, volume, hold

```python
import akshare as ak
df = ak.futures_main_sina(symbol="RB0", start_date="20240101", end_date="20241231")
```

### futures_hist_em

描述：东方财富-期货历史行情

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 合约代码 |
| period | str | "daily"/"weekly"/"monthly" |
| start_date | str | "20240101" |
| end_date | str | "20241231" |

```python
import akshare as ak
df = ak.futures_hist_em(symbol="RB2501", period="daily", start_date="20240101", end_date="20241231")
```

---

## 期货分钟数据

### futures_zh_minute_sina

描述：新浪-期货分钟数据

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 合约代码，如 "RB2501" |
| period | str | "1"/"5"/"15"/"30"/"60" |

```python
import akshare as ak
df = ak.futures_zh_minute_sina(symbol="RB2501", period="5")
```

---

## 合约信息

### futures_contract_detail

描述：期货合约详情（含合约乘数、最小变动等）

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 合约代码 |

```python
import akshare as ak
df = ak.futures_contract_detail(symbol="RB2501")
```

---

## 持仓排名

### futures_dce_position_rank

描述：大商所持仓排名

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| date | str | 日期，如 "20241220" |
| symbol | str | 品种代码，如 "i"(铁矿石) |

```python
import akshare as ak
df = ak.futures_dce_position_rank(date="20241220", symbol="i")
```

---

## 库存数据

### futures_inventory_em

描述：东方财富-期货库存数据

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 品种，如 "铜"、"螺纹钢" |
| exchange | str | 交易所代码 |

```python
import akshare as ak
df = ak.futures_inventory_em(symbol="铜")
```

---

## 手续费

### futures_fees_info

描述：期货手续费信息

输入参数：无

```python
import akshare as ak
df = ak.futures_fees_info()
```

---

## 国际期货

### futures_foreign_commodity_realtime

描述：国际期货品种实时行情

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 品种分类 |

```python
import akshare as ak
df = ak.futures_foreign_commodity_realtime(symbol="全部")
```

### futures_foreign_hist

描述：国际期货历史行情

输入参数：

| 名称 | 类型 | 描述 |
|------|------|------|
| symbol | str | 品种代码 |

```python
import akshare as ak
df = ak.futures_foreign_hist(symbol="LME铜")
```

---

## 全球期货

### futures_global_spot_em

描述：东方财富-全球期货实时行情

输入参数：无

```python
import akshare as ak
df = ak.futures_global_spot_em()
```
