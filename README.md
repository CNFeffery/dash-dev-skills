<p align="center">
  <img src="./imgs/logo.jpg" height="300" alt="Dash Dev Skills Logo" />
</p>

<h1 align="center">Dash Dev Skills</h1>

<div align="center">
适用于Dash应用开发的AI Agent技能库，旨在优化Vibe Coding+Dash应用代码生成质量，减少幻觉、提升效率🚀
</div>

## 目录

- [1 简介](#1-简介)
- [2 现有skills](#2-现有skills)
- [3 安装方式](#3-安装方式)
- [4 更多应用开发教程](#4-更多应用开发教程)

## 1 简介

包含一系列Dash应用开发实用Prompt Skills，可在Claude Code、OpenCode、Codex、Trae、Antigravity等主流AI编程助手中无缝调用，专门优化Dash应用代码的AI生成质量。

## 2 现有skills

|                                                          Skill名称                                                           |                   功能说明                    |
| :--------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------: |
|  [dash-native-html-integration](https://github.com/CNFeffery/dash-dev-skills/tree/main/skills/dash-native-html-integration)  |  规范嵌入原生HTML/JS/CSS等复杂定制化网页功能  |
|     [fetch-fac-component-names](https://github.com/CNFeffery/dash-dev-skills/tree/main/skills/fetch-fac-component-names)     |  获取有效的fac组件名，避免AI编造不存在的组件  |
| [fetch-fac-component-props-doc](https://github.com/CNFeffery/dash-dev-skills/tree/main/skills/fetch-fac-component-props-doc) | 精准获取指定fac组件的官方参数文档，以供AI查阅 |

## 3 安装方式

本项目的所有skills均位于仓库`skills`目录下，每个skill为一个独立子文件夹。

### 方式一：手动安装

1. 克隆或下载本仓库：
   ```bash
   git clone https://github.com/CNFeffery/dash-dev-skills.git
   ```
2. 将`skills/`目录下所需的skill文件夹，复制到你的项目中AI工具约定的skills目录，各工具对应路径参考如下：

   | AI 工具     | Skills 目录路径     |
   | ----------- | ------------------- |
   | Antigravity | `.agents/skills/`   |
   | Claude Code | `.claude/skills/`   |
   | OpenCode    | `.opencode/skills/` |
   | Trae        | `.trae/skills/`     |

   > 如使用其他工具，请参考其官方文档确认skills的存放位置。

3. 重启AI工具或重新加载配置，即可在对话中调用对应skill。

### 方式二：让AI自动安装

直接在对话框中向AI发送以下指令，由AI自动完成获取与配置：

> "请前往`https://github.com/CNFeffery/dash-dev-skills`仓库下的`skills`目录，将各个skill文件夹及其脚本获取并配置到当前项目中，以供你后续调用。"

## 4 更多应用开发教程

> 微信公众号「玩转 Dash」，欢迎扫码关注 👇

<p align="center">
  <img src="./imgs/公众号.png" height=220 />
</p>

> 「玩转 Dash」知识星球，海量教程案例模板资源，专业的答疑咨询服务，欢迎扫码加入👇

<p align="center">
  <img src="./imgs/知识星球.jpg" height=220 />
</p>
