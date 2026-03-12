---
name: dash-native-html-integration
description: 将基于原生HTML/JS/CSS的复杂或定制化网页功能（如图表、地图、特殊交互等）无缝且规范地嵌入到Dash应用指定的容器中。
---

# Dash Native HTML Integration Skill

## 🎯 技能概述 (Overview)

本技能指导 AI Agent 如何在 Dash 应用中规范、稳定地集成纯原生的前端技术栈（HTML/CSS/JavaScript）。
**核心机制**：摈弃在 Python 侧寻找 Dash 生态的替代组件，转而利用 `dash_clientside` 回调，将原生的前端渲染逻辑直接注入并接管 Dash 页面中预设的空容器组件（指定 ID 的 `div` 等）。

## 🔍 适用场景 (When to Use)

当面临以下需求时，应主动采用本技能工作流：

1. 项目需要接入复杂的纯前端库（如 ECharts, Leaflet, D3.js 等，需可通过独立 CDN 或 UMD 形式直接引入）。
2. 需要实现非标准、高度自定义的网页视觉动态效果或复杂交互链。
3. 现有的 Dash 组件无法满足深度定制需求，或存在性能瓶颈。
4. 用户明确要求“用原生前端技术实现，并集成到当前 Dash 项目中”。

## 📋 前置必要信息 (Prerequisites)

执行本技能前，必须首先明确以下上下文信息。如果缺失，**必须主动向用户提问**，待收集完整后再继续：

- [ ] **目标功能需求**：所需实现的前端功能细节及拟采用的具体技术栈/资源库。
- [ ] **目标容器 ID**：Dash 页面布局中，专门预留用于挂载当前功能的组件 `id`。
- [ ] **目标布局文件**：包含上述目标容器代码的 `.py` 文件路径。
- [ ] **回调注册文件**：指定要把 `clientside_callback`（浏览器端回调）逻辑写入哪个目标 `.py` 文件中。

---

## 🚀 执行工作流 (Execution Workflow)

在执行过程中，严格遵守以下分步工作流：

### 阶段一：需求对齐与技术规划 (Planning)

1. 分析所需功能，明确需要的外部 CDN 依赖（JS/CSS）。
2. 向用户简要汇报实现方案及即将执行的步骤。
3. **阻塞步骤**：等待用户确认方案无误后，再推进下一步代码生成。

### 阶段二：原生形态预构建与验证 (Prototyping)

不要急于修改 Dash 项目文件。首先，在系统外侧（或临时目录）生成一个纯净运行的 `HTML` 演示文件，确保底层前端逻辑可用且正确。

1. **生成临时 HTML**：创建一个包含完整 HTML/CSS/JS 的独立文件。
2. **规范约束**：
   - 所有的功能渲染必须被限制在一个 `<div id="temp-target-container"></div>` 内。
   - **防冲突机制**：所有元素的 `class` 和 `id` 必须足够特殊或带有前缀，绝不能污染当前 Dash 应用原有的样式。
   - **幂等与生命周期**：JS 的主渲染逻辑必须封装入一个独立函数中。**最关键的是**：函数开始时必须先执行**容器销毁/清理操作**（如清空容器 `innerHTML` 或调用第三方库的 `dispose()` 方法），确保该函数可被重复安全调用，不会发生 DOM 堆叠或内存泄露。

### 阶段三：Dash 深度集成 (Integration)

在临时 HTML 验证无误后，将其核心逻辑拆解并工程化地融入到 Dash 项目中。

#### 1. 外部依赖注入 (External Resources)

若 HTML 依赖外部 CDN 资源：

- 找到初始化 `app = dash.Dash(...)` 的入口文件。
- 将必须的外部 JS 和 CSS 链接，分别注入到其 `external_scripts` 和 `external_stylesheets` 参数中。

#### 2. 样式表抽离 (CSS)

- 提取内联样式。
- 在 Dash 项目的 `assets/css/` 目录下创建一个专门负责当前组件样式的独立 `.css` 文件。**选择器限制在目标容器环境内**。

#### 3. 浏览器端逻辑封装 (JavaScript)

- 提取核心 JS 逻辑。
- 在 Dash 项目的 `assets/js/` 目录下新建一个独立的 `.js` 文件，使用标准 Clientside API 封装：

```javascript
// 假设命名空间为 native_renderer，函数名为 render_my_feature
window.dash_clientside = Object.assign({}, window.dash_clientside, {
  native_renderer: {
    render_my_feature: function (targetId) {
      // 设置轻微延时，确保 Dash DOM 完全渲染并挂载到文档流
      setTimeout(() => {
        const container = document.getElementById(targetId);
        if (!container) return;

        // ⚠️ 步骤 1：严格的清理动作，防止热重载或回调重复触发导致 DOM 叠加
        // 例如：container.innerHTML = ''; 或者 instance.dispose();

        // 🚀 步骤 2：植入从临时 HTML 提取来的原生渲染逻辑
        // 将原有的 '#temp-target-container' 替换为传入的 container 对象
      }, 200);

      // 阻止 Dash 后端刷新此组件内容
      return window.dash_clientside.no_update;
    },
  },
});
```

#### 4. Python 回调注册 (Callback Registration)

- 定位到用户指定的**回调注册文件**。
- 将上述 JS 函数与目标容器绑定。通过监听目标容器的 `id`（页面初次渲染时触发）来单次启动 JS 函数：

```python
from dash.dependencies import Input, Output, ClientsideFunction
# 若上文缺失 app 引用，需全局搜索定义位置并正确导入（如 from server import app）

app.clientside_callback(
    ClientsideFunction(
        namespace='native_renderer',      # 对应 JS 中的命名空间
        function_name='render_my_feature' # 对应 JS 中的函数名
    ),
    Output('<目标组件ID>', 'children'),
    Input('<目标组件ID>', 'id')           # 核心机制：以自身 ID 为 Input，实现初次加载触发
)
```

### 阶段四：自检与收尾 (Verification & Cleanup)

1. **执行自检**：
   - [ ] 检查客户端 JS 中是否包含了旧 DOM/实例的清理逻辑。
   - [ ] 检查 `app` 实例是否已正确引入到了回调注册文件中（避免导包错漏）。
   - [ ] 检查生成的 ID 和 CSS class 是否带有命名空间，确保不会污染原有应用样式。
2. **环境清理**：若确认原生代码已成功集成且无需再调整，向用户提问是否清理或删除之前生成的临时 `HTML` 文件原型。

---

## 🚫 核心禁忌 (Strict Anti-Patterns)

- ❌ **禁止在容器内继续嵌套 Dash 组件**：接管的目标容器其内部 DOM 树将完全由前端客户端 JS 把控，Dash 不应再通过 Python 试图向其内部排布组件，否则将引发不可预测的虚拟 DOM 渲染异常和状态覆盖。
- ❌ **禁止将回调函数跨域随意注册**：`clientside_callback` 必须且只能写在用户事前指定的回调管理文件内。
- ❌ **严禁省略销毁逻辑**：不执行清理逻辑而直接叠加新 DOM 是导致内存泄漏和重复渲染灾难的首要原因，AI 必须要处理。
