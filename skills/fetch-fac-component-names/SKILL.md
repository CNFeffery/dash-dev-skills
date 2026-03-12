---
name: fetch-fac-component-names
description: 【最高优先级】获取Dash fac库(feffery-antd-components)全部有效组件名称列表。当用户要求生成Dash代码且涉及fac时必调，用于消除AI虚构组件名的严重幻觉。
---

# Fetch FAC Component Names Skill

## 🎯 技能概述 (Overview)

本技能指导 AI Agent 在开发 Dash 应用并且涉及到使用 `feffery-antd-components` (简称 fac) 时，如何自动获取最新有效的内部全部组件名称列表。由于大语言模型在预训练数据中可能对该库存在细节盲区，常常会产生幻觉自行杜撰组件名。通过主动获取实际环境中的合法组件名称，可以彻底消除此类幻觉。

## 🔍 适用场景 (When to Use)

当满足以下条件时必须触发：
1. 用户要求生成 Dash 应用代码；
2. 明确提到“**要使用fac来实现功能**”、“**使用 feffery-antd-components**”或相似诉求；
3. 为防代码因杜撰组件报错，需核实正确组件标识时。

---

## 🚀 执行工作流 (Execution Workflow)

触发后不可跳过，请**高效且绝对服从**地执行以下步骤：

### 步骤 1：探测环境并直接获取数据 (核心)

**【绝对禁令 1】严禁使用 `where python`、`which python` 或全局 `python` 命令。**
**【绝对禁令 2】当找不到项目专属 Python 环境时，绝对禁止使用网络搜索（WebFetch / Exa Search）或尝试阅读组件库源码作为替代方案！**
发生上述任意行为将被视为**严重违规并判定为任务失败**！

1. **环境探测与快速执行**：快速扫描工作区识别专属虚拟环境（如 `.venv`, `venv` 目录）或包管理器（如 `pyproject.toml`, `Pipfile`），并**直接尝试运行**数据获取脚本 `scripts/fetch_fac_components.py`（根据本 skill 的物理路径动态拼接）：
   - *示例 (基于 `.venv`)*：`.venv/bin/python <SKILL_DIR>/scripts/fetch_fac_components.py` (Windows: `.venv\Scripts\python.exe`)
   - *示例 (基于 `poetry`)*：`poetry run python <SKILL_DIR>/scripts/fetch_fac_components.py`
   如果成功打印出 JSON 数组形式的组件名列表，立刻将其读入上下文，进入步骤 2。
2. **依赖缺失自愈**：如执行报错 `ModuleNotFoundError: No module named 'feffery_antd_components'`，请立即在**该专属环境**内安装 fac（如 `.venv/bin/python -m pip install feffery-antd-components`），安装完毕后**重新执行步骤1.1获取结果**。
3. **【强制】退避询问机制**：如果在当前工作区内**找不到任何显式的专属虚拟环境线索**，你必须：
   - **立刻停止所有动作！**
   - **不要**尝试去搜索引擎或外网查组件列表。
   - **不要**尝试阅读本库里的脚本源码来瞎猜。
   - **唯一且强制的下一步行动是向用户发起提问**：“我没有在当前工作区发现显式的 Python 虚拟环境配置（例如 .venv 目录或 pyproject.toml），为了安全获取组件信息，请问项目依赖的 Python 环境路径是什么？（例如某个 conda 环境名称，或是系统上其他位置的 venv 绝对路径）”，**然后等待用户回答**。只有得到明确的环境后，才能继续回去执行获取脚本。

### 步骤 2：应用知识生成代码或强制触发属性查询

获取到有效的 fac 组件名称列表后，根据当前任务目标执行以下**严格逻辑**：

**分支 A：如果是直接生成/修改代码应用**
- 在本次任务后续涉及利用 `fac` 编写 Dash 应用时，严格且仅限于使用名单中存在的组件。
- 绝不编造或臆测名单以外的任何组件名。

**分支 B（关键强制点）：如果用户是为了解、询问组件功能/用法/参数（如：“fac的按钮组件怎么监听点击事件？”）**
- 你在获得“全部组件名称”以**精准定位到特定组件名**（如定位到 `AntdButton`）之后，**【必须、立刻、毫无例外地】作为下一步工作流去调用 `fetch-fac-component-props-doc` 技能**查阅该特定组件的详情文档。
- **严禁**在此步骤仅拿到名字后就直接凭历史知识或外部搜索作答。必须由 `fetch-fac-component-props-doc` 提取到的 `__doc__` 作为你回答的绝对权威依据！
