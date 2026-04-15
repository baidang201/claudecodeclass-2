这份讲义旨在为开发者提供 **Claude Code** 进阶能力的深度指南。从基础的 Skill 扩展到复杂的多 Agent 协作框架，涵盖了从个人效率到团队生产力的全路径。

-----

# 终端超级大脑 Claude Code (中) —— 命令行里的 Agent 智能体

## 课程简介

在掌握了 Claude Code 的基础交互后，本阶段将深入探讨如何通过 **Skill**、**MCP** 以及 **多 Agent 框架** 将其从一个“对话式编程助手”升级为能够自主处理复杂工程任务的“终端智能体”。

-----

## 一、 扩展能力：Skill 与 MCP

### 1\. Skill 简介

**Skill**是可复用的说明、知识、工作流，通常包含一个 SKILL.md 以及可运行脚本、资源文件。

### 2\. SkillHub 资源网站

  * **Vercel Lab 出品的 skill 排行榜**:[Vercel Lab 出品的 skill 排行榜](https://skills.sh/)
  * **Anthropic 官方 Skills 仓库**: [Anthropic 官方 Skills 仓库](https://github.com/anthropics/skills)。

### 3\. 常用 Skill 推荐

•查找skill的 skill：
```
npx skills add https://github.com/vercel-labs/skills --skill find-skills
```
•创建 skill 的 skill
```
npx skills add https://github.com/anthropics/skills --skill skill-creator
```
• 产品需求头脑风暴规划
```
npx skills add https://github.com/obra/superpowers --skill brainstorming
```
• 前端开发 React 编码规范 skill
```
npx skills add https://github.com/vercel-labs/agent-skills --skill vercel-react-best-practices
```

• 前端开发 UI/UX 美化
```
npx skills add https://github.com/nextlevelbuilder/ui-ux-pro-max-skill --skill ui-ux-pro-max
```
• 浏览器自动化 skill
```
npx skills add https://github.com/vercel-labs/agent-browser --skill agent-browser
```

### 4\. 安装 Skill 教程与实战

  * **安装命令**: 通常使用 `npx skills add <skill-name>` 安装
  * 或手动放置在全局skills目录 `~/.claude/skills` 目录 或者 项目的skills目录`./.claude/skills`。
  * **实战**: 尝试编写一个简单的 `weather-skill`，让 Claude 能在终端告诉你当前城市的天气。

-----

## 二、 协议标准：MCP (Model Context Protocol)

### 5\. MCP 简介

**MCP** 是由 Anthropic 推出的开放协议，旨在标准化 AI 模型与外部数据源、工具之间的连接。

### 6\. MCPHub 资源网站
  * **mcpso**: [mcpso](https://mcp.so/)
  * **smithery**  [smithery](https://smithery.ai/) 
  * **pulsemcp** [pulsemcp](https://www.pulsemcp.com/)

-----

## 三、 命令与钩子：控制权的精细化

### 7\. 斜杠命令 (Command) 简介

在 Claude Code 交互界面中，`/` 命令可以快速触发特定功能：

  * `/compact`: 压缩上下文，保留关键信息。
  * `/review`: 对当前暂存区的代码进行评审。

### 8\. Hook 简介

**Hook** 允许在特定事件（如代码提交前、命令执行后）自动触发动作。

  * **Pre-commit Hook**: 在你 Git commit 之前，让 Claude 检查是否存在潜在的 Security Issue。

-----

## 四、 进阶流：多 Agent 协作

### 9\. Agent 简介

这里的 Agent 指的是具有特定角色、上下文和工具集的 Claude 实例。打开一个claude窗口就是一个主Agent

### 10\. 多 Agent 非直接业务多窗口操作

通过 `--worktree` 参数实现并行开发：

  * **窗口 A (开发)**: 执行主逻辑编写。
  * **窗口 B (测试与 Review)**: 执行 `claude --worktree` 在另一个分支或目录进行测试覆盖率检查和代码质量评审。

### 11\. Agent Teams

**Agent Teams** 概念允许你同时调动多个智能体。例如：

  * **Coordinator**: 负责分发任务。
  * **Coder**: 负责写代码。
  * **QA**: 负责写测试。
    AI 会根据任务复杂度自动协调内部工作流。

-----

## 五、 插件与框架对比

### 12\. Plugins 插件简介

Plugins 是集合了 Skill、Command、Hook 的高级封装包。

  * **典型代表**: **Superpowers**。它不仅是工具集，更是一套增强版的交互逻辑。

### 13\. 高星多 Agent 框架对比

| 框架名称 | 核心特点 | 适用场景 |
| :--- | :--- | :--- |
| **Superpowers** | 极简、个人增强、开箱即用 | **个人开发者** |
| **BMAD** | 针对企业级业务逻辑、强规则约束 | **大团队/企业** |
| **GStack** | 侧重于全栈开发自动化 | 中小团队 |
| **SpecKit / OpenSpec** | 专注于规格说明书驱动开发 (SDD) | 规范化团队 |
| **Get Shit Done** | 极速交付、任务导向 | 自由职业者 |

> **总结推荐：**
>
>   * **个人**: 推荐 **Superpowers**，上手快，功能覆盖全。
>   * **小团队**: 推荐 **GStack** 或 **SpecKit**，兼顾效率与规范。
>   * **大团队**: 推荐 **BMAD**，适合处理复杂业务逻辑与合规性要求。

-----

## 六、 实战演练

### 14\. 个人框架 Superpowers 实战

1.  安装 Superpowers 插件。
2.  演示如何通过一个指令完成从“需求分析”到“代码实现”的全过程。

### 15\. 团队框架 BMAD 实战

### **方案A：简化版完整流程（推荐）**
如果想展示从零开始的完整流程但不过于复杂：

1. **`/bmad-create-product-brief`**
   - 快速创建产品简报，定义核心价值主张
   - 产出：`product-brief.md`

2. **`/bmad-bmm-create-prd`**
   - 展示AI如何将简报转化为结构化PRD
   - 产出：`PRD.md`（包含用户旅程、功能需求、验收标准）

3. **`/quick-spec`**
   - 基于PRD生成技术规格
   - 展示AI如何分析需求并制定技术方案

4. **`/dev-story`**
   - 实现第一个用户故事
   - 展示TDD开发流程

5. **`/code-review`**：
   - 展示质量审查过程
   - 强调"对抗式"审查的价值

**总时长**：覆盖了**需求→规划→技术设计→实现→审查**的完整闭环。

-----

## 七、 课后作业

**目标**: 使用 **Superpowers** 框架完成一个单网页应用（SPA）。
**功能需求**:
1.  **接种提醒**: 根据用户输入的出生日期，给出“适合打和快要打的疫苗”提示。
2.  **疫苗记录**: 填写打的疫苗和接种日期
3.  **UI要求**: 简洁、现代。

> **提示**: 尝试用 `/ask` 让 Claude 帮你设计数据结构，然后用 Superpowers 的自动构建能力生成 HTML/JS/CSS。

-----

本讲义旨在构建你对 Claude Code 进阶生态的认知。通过从单一工具到多 Agent 协作的转变，你将体验到“一个人就是一个技术部”的高效开发模式。
