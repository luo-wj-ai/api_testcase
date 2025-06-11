# Fuzz Testing Framework v1.0

字段规则驱动的接口模糊测试框架

---

## 📌 项目简介

本框架基于 **字段级规则** 自动生成接口正向 & 反向用例，结合 Allure 测试报告，快速实现接口健壮性、边界值、异常场景的自动化覆盖。

- ✅ 完全字段规则驱动
- ✅ 支持每个接口自定义业务码断言
- ✅ 支持反向用例多轮执行
- ✅ Allure 报告集成，一键执行 + 报告生成
- ✅ 框架与接口解耦，易维护、易扩展

---

## 📂 目录结构

```
fuzz_test/
  ├── config/             # 每个接口的字段规则配置
  ├── core/               # 框架核心逻辑 (规则/用例生成/执行器)
  ├── tests/              # 各接口测试入口
  ├── run_all.py          # 一键执行入口
  ├── results/            # pytest执行结果 (自动生成)
  └── report/             # allure报告 (自动生成)
```

---

## ⚙️ 安装依赖

请先安装以下依赖：

```bash
pip install requests pytest allure-pytest
```

> 如果没有 Allure 命令行工具，请安装：

- Windows: `choco install allure`
- MacOS: `brew install allure`

---

## 🚀 一键运行测试

在项目根目录下执行：

```bash
python run_all.py
```

- 自动清理旧结果；
- 自动运行所有用例；
- 自动生成并打开最新 Allure HTML 报告。

---

## 🧠 核心配置说明（重点）

### 1️⃣ 字段规则定义 (FieldRule)

```python
FieldRule(
    name="字段名",
    required=True,                 # 是否必填
    data_type="string",            # 支持 string / int / float
    enum=["可选值1", "可选值2"],    # 合法枚举值 (可选)
    custom_invalid=["非法值1", ""], # 自定义非法值 (可选)
    invalid_code_map={             # 各种异常场景对应业务状态码 (核心)
        "missing": "业务码1",
        "type_error": "业务码2",
        "enum_error": "业务码3",
        "custom_非法值1": "业务码4",
        "custom_empty": "业务码5"
    }
)
```

> **注意：每个接口都单独在 config/ 下新建对应的配置文件。**

---

### 2️⃣ 正向用例

在 `VALID_DATA` 内维护一份合法入参作为正向用例，框架自动执行。

---

### 3️⃣ 反向用例自动生成逻辑

框架根据 `FieldRule`：

- 缺失
- 类型错误
- 枚举非法
- 自定义非法值

自动生成反向用例，并绑定对应业务码用于断言。

---

### 4️⃣ 断言逻辑统一化

无需再手动编写断言逻辑，框架已内置统一断言：

```python
actual_code = result["response"]["header"]["status"]
assert actual_code == case["expected_biz_code"]
```

---

## ✨ 扩展新接口示例流程

1️⃣ 在 `config/` 新建新接口配置文件  
2️⃣ 按照 `create_order_config.py` 模板编写规则  
3️⃣ 在 `tests/` 新建测试入口文件  
4️⃣ 无需修改框架逻辑，可直接运行

---

## 🧩 典型应用场景

- 接口参数健壮性自动化验证
- 字段级异常场景批量验证
- 模糊测试覆盖
- 接口健壮性回归测试

---

## 🔥 未来可扩展方向

- 字段级依赖关系建模
- 并发性能 fuzz 测试
- 智能边界值探索
- RSA 加密/签名字段支持
- 批量接口批次执行平台化

---

## 📞 技术支持

如需长期复用、二次封装、平台化，可联系框架作者进行深度定制升级。

---

🎯 **当前已具备交付生产使用能力。**
