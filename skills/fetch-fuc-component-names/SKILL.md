---
name: fetch-fuc-component-names
description: 【最高优先级·Dash开发必调】凡涉及 Dash 应用开发的任务（功能实现、组件选型、布局、交互、回调等），无论用户是否明确提到 fuc，都必须将本 skill 作为第一步立即执行，获取 feffery-utils-components 全部合法组件名称，再联动调用 fetch-fuc-component-props-doc 查参数，最后才开始写代码。禁止跳过直接生成代码。
---

# Fetch FUC Component Names Skill

## 🎯 技能概述

本技能帮助 AI Agent 在 Dash 应用开发中，从本地 Python 环境实时获取 `feffery-utils-components`（简称 fuc）的全部合法组件名称列表，从根源杜绝 AI 编造不存在组件名的幻觉问题。

---

## 🔍 适用场景（When to Use）

满足以下**任意一项**，立即触发，**无需用户明确说明**：

1. 用户提出任何 Dash 应用开发需求（页面功能、UI 组件、布局、交互、回调等）
2. 用户明确提到 fuc / feffery-utils-components，或代码中已有 fuc 的 import
3. 需要从 fuc 中挑选组件实现某项功能时

> ⚡ **强制联动**：获取到组件列表并确认合适组件后，**下一步必须立即调用 `fetch-fuc-component-props-doc`** 获取参数文档，再开始编写代码。两个 skill 必须串联执行，不可跳过任何一步。

---

## 🚀 执行工作流

### ⛔ 铁律禁令（违反即判定任务失败）

- **禁令 1**：严禁使用 `python`、`python3`、`where python`、`which python` 等任何形式的系统默认 Python 命令
- **禁令 2**：严禁在系统全局环境（包括 conda base、系统 site-packages）中安装任何包
- **禁令 3**：严禁通过网络搜索、WebFetch、查看源码等方式绕过本地脚本执行来获取组件信息
- **禁令 4**：严禁在未获得用户明确授权的 Python 环境下执行任何命令

---

### 步骤 1：询问用户 Python 环境路径（强制首步，不可跳过）

**在执行任何命令之前，必须先向用户明确询问：**

> "为了从本地环境准确获取 fuc 组件信息（避免 AI 幻觉），我需要使用您项目所用的 Python 解释器来运行获取脚本。请提供您项目使用的 Python 环境路径，例如：
> - conda 环境名称：`conda run -n your_env_name python`
> - venv/virtualenv 绝对路径：`C:\project\.venv\Scripts\python.exe`
> - 其他任意可执行的 Python 路径"

⚠️ **在用户给出明确答复之前，禁止进行任何后续步骤。**

> **例外情况**：若在当前对话上下文中，用户已经在此次任务中明确提供过 Python 环境路径（例如之前的消息中已说明），则可直接使用，无需重复询问。

---

### 步骤 2：使用指定环境运行获取脚本

使用用户提供的 Python 路径运行本 skill 目录下的脚本 `scripts/fetch_fuc_components.py`（根据本 SKILL.md 的物理路径拼接绝对路径）：

```
# 示例（按用户提供的环境替换前缀）
conda run -n myenv python <SKILL_DIR>/scripts/fetch_fuc_components.py
C:\.venv\Scripts\python.exe <SKILL_DIR>/scripts/fetch_fuc_components.py
```

- 脚本成功输出 JSON 数组形式的组件名列表后，读入上下文，进入步骤 3。
- 若报错 `ModuleNotFoundError: No module named 'feffery_utils_components'`：
  - 告知用户："目标环境中尚未安装 fuc，是否允许我在该环境中执行安装？"
  - **必须等待用户同意后**，方可执行安装命令（使用用户提供的 Python 路径，不得使用其他路径）：
    ```
    # 使用用户提供的 Python 路径（非全局命令）
    C:\.venv\Scripts\python.exe -m pip install feffery-utils-components
    ```
  - 安装完成后重新执行本步骤。

---

### 步骤 3：应用组件名称，强制联动查参数

获取到合法组件名称列表后：

**分支 A — 开发代码**：在名称列表中确认将要使用的组件，**立即调用 `fetch-fuc-component-props-doc` skill** 获取对应组件的参数文档，再组织代码。严禁使用列表中不存在的组件名。

**分支 B — 答疑解惑**：用户询问某 fuc 组件功能/用法/参数时，从列表中精确定位组件名后，**立即调用 `fetch-fuc-component-props-doc` skill** 查阅文档，以文档内容为唯一权威依据作答。严禁凭历史知识直接回答。
