---
name: fetch-fac-component-props-doc
description: 【高优先级】查询目标fac组件(feffery-antd-components)的官方参数属性(Props)文档与具体功能描述。无论是开发带参数的fac组件，还是回答关于某特定fac组件（如 AntdMenu）有哪些功能与用法时必调。消除模型虚假编造的幻觉问题。
---

# Fetch FAC Component Properties Document Skill

## 🎯 技能概述 (Overview)

本技能指导 AI Agent 在开发 Dash 应用，或者解答关于 `feffery-antd-components` (简称 fac) 特定组件功能、用法与属性配置疑问时，如何高效获取其官方自带的完整文档（Docstrings）。大语言模型极易混淆不同框架（如 React 与 Dash）间的同名组件属性和功能，通过本技能不仅能为代码生成提供绝对准确的方法查阅字典，也能在你或用户想要了解“某个组件能做什么、支持什么特性”时提供权威说明，彻底杜绝概念编造或属性报错。

## 🔍 适用场景 (When to Use)

遇到以下情况应立即触发：
1. 正在生成或重构涉及 `feffery-antd-components` 的组件代码；
2. 为特定的 fac 组件（如 `AntdButton`, `AntdTable` 等）配置具体的 Props；
3. 用户或智能体自身（你）需要**了解或询问某个特定 fac 组件的具体功能、作用、支持哪些特性**；
4. 对该组件支持哪些配置项存疑，或为了消除幻觉需要一份权威清单以防报错。

---

## 🚀 执行工作流 (Execution Workflow)

满足条件后，请**高效且绝对服从**地执行以下步骤：

### 步骤 1：探测环境并获取参数文档 (核心)

**【绝对禁令 1】严禁使用 `where python`、`which python` 或全局 `python` 命令。**
**【绝对禁令 2】当找不到项目专属 Python 环境时，绝对禁止使用网络搜索（WebFetch / Exa Search）或尝试阅读组件库源码作为替代方案！**
发生上述任意行为将被视为**严重违规并判定为任务失败**！

1. **环境探测与快速执行**：扫视工作区寻找专属 Python 环境（如 `.venv` 目录、`pyproject.toml` 等），构建好调用前缀。**直接尝试运行**本技能相对目录下的 `scripts/fetch_fac_component_props.py` 脚本，将待查组件名（如 `AntdTable`）作额外参数传入：
   - *示例 (基于 `.venv`)*：`.venv/bin/python <SKILL_DIR>/scripts/fetch_fac_component_props.py AntdTable`
   - *示例 (基于 `poetry`)*：`poetry run python <SKILL_DIR>/scripts/fetch_fac_component_props.py AntdTable`
   如果正常输出参数说明文档，阅读并记入上下文，随后跳至步骤 2。
2. **依赖缺失自愈**：如果在执行时抛出 `ModuleNotFoundError: No module named 'feffery_antd_components'`，说明此专属环境尚未安装依赖。请立即用对应的包管理器安装后（如 `.venv/bin/python -m pip install feffery-antd-components`），**重新执行步骤1.1获取文档**。
3. **【强制】退避询问机制**：如果在当前工作区内**找不到任何显式的专属虚拟环境线索**，你必须：
   - **立刻停止所有动作！**
   - **不要**尝试去搜索引擎里搜官网文档。
   - **不要**尝试阅读本库里的脚本源码来瞎猜。
   - **唯一且强制的下一步行动是向用户发起提问**：“我没有在当前工作区发现显式的 Python 虚拟环境配置（例如 .venv 目录或 pyproject.toml），为了安全获取组件信息，请问项目依赖的 Python 环境路径是什么？（例如某个 conda 环境名称，或是系统上其他位置的 venv 绝对路径）”，**然后等待用户回答**。只有得到明确的环境后，才能继续回去执行获取脚本。

### 步骤 2：应用获取的参数生成代码

- 核对或获取文档后，只有在文档中明确列出的参数项及符合类型的前提下，才可将其用于 Dash 布局或回调的代码组装。
- 脚本若提示警告（找不到该组件），表示你虚构或写错了组件名，**必须立刻停止按该名称生成代码**。
