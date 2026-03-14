---
name: fetch-fac-component-props-doc
description: 【高优先级·联动必调】fetch-fac-component-names 确认目标组件后，必须立即调用本 skill 获取该 fac 组件的官方参数（Props）文档，再开始写代码。也适用于用户直接询问某 fac 组件的功能、参数或用法时。严禁用 AI 记忆替代本 skill，必须以文档为准。
---

# Fetch FAC Component Properties Document Skill

## 🎯 技能概述

本技能帮助 AI Agent 从本地 Python 环境实时获取 `feffery-antd-components`（简称 fac）指定组件的官方参数文档（Docstrings），以权威文档为唯一依据生成代码或回答咨询，彻底消除 AI 编造参数/属性的幻觉。

---

## 🔍 适用场景（When to Use）

满足以下**任意一项**，立即触发：

1. **联动触发（最常见）**：`fetch-fac-component-names` 已定位到目标组件，下一步必须立即调用本 skill
2. **代码开发**：需要为特定 fac 组件配置 Props 参数，在写代码之前
3. **功能咨询**：用户询问某个 fac 组件支持哪些功能、属性、参数或用法时

> ⚠️ **即使你认为自己了解该组件的参数，也必须通过本 skill 获取文档，不得凭 AI 记忆直接配置参数。**

---

## 🚀 执行工作流

### ⛔ 铁律禁令（违反即判定任务失败）

- **禁令 1**：严禁使用 `python`、`python3`、`where python`、`which python` 等任何形式的系统默认 Python 命令
- **禁令 2**：严禁在系统全局环境（包括 conda base、系统 site-packages）中安装任何包
- **禁令 3**：严禁通过网络搜索、WebFetch、查看源码等方式替代本地脚本执行来获取文档
- **禁令 4**：严禁在未获得用户明确授权的 Python 环境下执行任何命令

---

### 步骤 1：确认 Python 环境路径（强制首步，不可跳过）

**在执行任何命令之前，必须先确认用户提供了 Python 环境路径。**

- 若在本次对话中，用户（或上游 `fetch-fac-component-names` 步骤）已明确提供 Python 环境路径，直接使用，跳至步骤 2。
- 若尚未获得明确路径，**立即询问用户：**

> "需要您提供项目使用的 Python 解释器路径，才能获取 fac 组件文档，例如：
> - conda 环境：`conda run -n your_env_name python`
> - venv 绝对路径：`C:\project\.venv\Scripts\python.exe`"

⚠️ **在用户回复之前，禁止进行任何后续步骤。**

---

### 步骤 2：使用指定环境运行文档获取脚本

使用用户提供的 Python 路径运行本 skill 目录下的脚本 `scripts/fetch_fac_component_props.py`，并将目标组件名作为参数传入（根据本 SKILL.md 的物理路径拼接绝对路径）：

```
# 示例（按用户提供的环境替换前缀）
conda run -n myenv python <SKILL_DIR>/scripts/fetch_fac_component_props.py AntdTable
C:\.venv\Scripts\python.exe <SKILL_DIR>/scripts/fetch_fac_component_props.py AntdTable
```

- 脚本成功输出参数文档后，读入上下文，进入步骤 3。
- 若报错 `ModuleNotFoundError: No module named 'feffery_antd_components'`：
  - 告知用户："目标环境中尚未安装 fac，是否允许我在该环境中执行安装？"
  - **必须等待用户同意后**，方可执行安装命令（严格使用用户提供的 Python 路径）：
    ```
    C:\.venv\Scripts\python.exe -m pip install feffery-antd-components
    ```
  - 安装完成后重新执行本步骤。
- 若脚本输出"未找到该组件"警告：说明组件名有误，**立即停止后续操作**，返回调用 `fetch-fac-component-names` 重新确认正确的组件名。

---

### 步骤 3：严格依照文档生成代码

- 仅使用文档中明确列出的参数名及合法类型，组织 Dash 布局或回调代码。
- 文档未记载的参数，一律视为不存在，严禁自行补充或猜测。
