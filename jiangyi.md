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

官方插件列表： https://claude.com/plugins#plugins
![alt text](image-3.png)

  * **典型代表**: **Superpowers**(https://github.com/obra/superpowers)。Superpowers是一个为Claude Code设计的开源插件框架，它通过强制AI遵循严格的软件开发方法论，将AI编程助手从简单的"代码生成器"转变为懂得先设计再编码、会写测试、能自我审查的工程助手。

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

### 14\. 个人框架 Superpowers 实战，
superpower简介
Superpowers 是 Claude Code 插件市场上最流行的 Agentic Coding 框架之一，目前在 GitHub 上已有 156k ⭐！

Superpowers 是一个开源的 AI 行为准则框架。它不是直接帮你写代码，而是给 AI 制定了一套极其严格的“工作流程”和“专业技能”，让 AI 像一个有多年经验、做事极度严谨的顶级工程师一样思考和行动。主要技能包括：
✅ 需求脑暴
✅ 编写计划
✅ 执行子代理
✅ 测试驱动开发
✅ 代码质量检查

最好的是：我们不需要手动去点这些功能，只要安装好后，AI 就会在后台自动调用这些技能，你只需要像往常一样跟它聊天提需求即可！


我们做一个疫苗记录单网页应用
#### 1. 创建项目目录
```
mkdir claude-yimiao
cd claude-yimiao
```

进入claude
```
claude
```
#### 2. 安装 Superpowers 插件。

```
/plugin marketplace add anthropics/claude-plugins-official
```
![alt text](image-4.png)

```
/plugin install superpowers@claude-plugins-official
```
![alt text](image-2.png)

这里我们是测试目的，选第三个“Install for you, in this repo only (local scope)  ”

![alt text](image-5.png)


这三个选项是 **Claude Code**（包括安装 Superpowers skills 或插件时）提供的**安装范围（scope）**选择，主要区别在于**谁能使用**、**配置存储位置**以及**是否随仓库共享**。

以下是清晰对比（以 `npx skills add` 或类似安装流程为例）：

| 选项 | 英文名称          | 含义（谁能用）                          | 配置存储位置                          | 是否提交到 Git（共享） | 推荐场景 |
|------|-------------------|-----------------------------------------|---------------------------------------|------------------------|----------|
| **第一个** | Install for you (user scope) | **只你自己**，**所有项目** 都能用     | `~/.claude/skills/` 或用户全局设置文件（如 `~/.claude/settings.json`） | 否（个人私有） | **最常用推荐**<br>你个人经常使用的 skills（如 Superpowers 核心技能），想在所有仓库里都可用 |
| **第二个** | Install for all collaborators on this repository (project scope) | **团队所有人**（仓库协作者）都能用   | 项目根目录下的 `.claude/skills/` 或 `.claude/settings.json` 等 | 是（建议 commit 到仓库） | 团队协作项目<br>希望整个团队都统一使用同一套 Superpowers skills 或工作流 |
| **第三个** | Install for you, in this repo only (local scope) | **只你自己**，**仅当前仓库** 生效    | 项目内本地文件（如 `.claude/skills.local/` 或 gitignored 的本地配置） | 否（通常加到 `.gitignore`） | 测试新 skill、敏感配置、或只想在当前项目实验时使用<br>不会影响其他项目 |


#### 3 刷新插件
```
 /reload-plugins  
``` 
![alt text](image-6.png)

#### 4 查看安装的插件
```
/plugin  
```
![alt text](image-7.png)


查看新增的技能

```
/skills
```
![alt text](image-8.png)

#### 3 初始化项目
```
/init
```
![alt text](image.png)

#### 4 演示如何通过从“需求分析”到“代码实现”的全过程。

输入我们的需求，他会调用superpowers的brainstorming技能，对话式的帮我们拆解需求

```
我想做一个宝宝疫苗记录单网页工具，
1 可以初始化出生年月日配置宝宝信息，然后提醒7天内可以打的疫苗。
2 可以输入打的疫苗和接种日期，用于存档
```
发送过去我们看到他开始调用技能了
![alt text](image-9.png)

先问了疫苗提醒是免费还是付费的，我们选1
![alt text](image-10.png)

然后问了数据存储方式，选1
![alt text](image-11.png)

然后问了界面风格，选1
![alt text](image-12.png)

然后问支持几个宝宝，选1
![alt text](image-13.png)

然后问核心设计，选满意吧
![alt text](image-14.png)

然后他帮我们创建spec文档
![alt text](image-15.png)


创建好之后，进入计划阶段，创建执行计划
![alt text](image-16.png)

这里做好了计划，我们选2，一次处理完，然后在设置检查点
![alt text](image-17.png)

这里开始执行计划
![alt text](image-18.png)

经过漫长的等待，计划执行完成，代码也编写好了
![alt text](image-19.png)

他帮我们自动打开应用网页，试用了一下功能，感觉还行，流程比较丝滑
![alt text](image-20.png)
![alt text](image-21.png)
![alt text](image-22.png)


验证完功能后，开始收尾工作，我们演示用就先选1
![alt text](image-23.png)

### 15\. 团队框架 BMAD 实战

BMAD简介
BMAD是一个敏捷AI驱动开发的完整框架，核心目标是通过AI代理和结构化工作流，实现从需求到部署的全流程自动化闭环。
核心特点
1 多智能体协同：12+个领域专家代理（产品经理、架构师、开发者、UX、Scrum Master等）
2 结构化工作流：50+个引导式工作流，核心模块BMM包含34+个跨4个开发阶段的工作流
3 规模自适应：根据项目复杂度自动调整规划深度，小到单点修复、大到企业级交付均可适用
4 Party Mode：支持在同一会话中引入多个Agent角色协作讨论，形成"多角色会议"式决策
5 全生命周期覆盖：从头脑风暴、需求定义、架构设计、开发实现到部署交付全流程支持


#### 

#### 创建演示项目
```
mkdir claude-bmad-richeng
cd claude-bmad-richeng
```






#### 2. 安装 bmad 插件。

```
npx bmad-method install --directory /Users/liyihang/Downloads/claude-bmad-richeng --modules bmm --tools claude-code --yes
```
![alt text](image-24.png)
![alt text](image-25.png)


进入claude
```
claude
```

初始化
```
/init
```

查看bmad的skills
```
/skills
```
![alt text](image-26.png)


交互开始确定需求
```
/bmad-product-brief
```
![alt text](image-27.png)


输入
“我想做一个日程管理单页网页应用，包含日历日期选择，新建日程。可以查看每月的日程列表”

![alt text](image-28.png)


我们回答上面的问题,输入
```
1 自己用的
2 个人时间管理和规划
3 没有
4 html/css/js
5 本地存储
6 从零开始
```
![alt text](image-29.png)


继续回答上面问题，输入
```
1 日程支持全天
2 先做创建和查看
3 显示公历
4 商务蓝色

```
![alt text](image-30.png)

产品简报完成了
![alt text](image-31.png)


我们开发流程正式一点，让他生成prd吧
```
/bmad-create-prd
```

![alt text](image-32.png)

我们继续，输入
“c”


### **方案A：简化版完整流程（推荐）**
如果想展示从零开始的完整流程但不过于复杂：

1. **`/bmad-product-brief`**  
   - 从模糊想法快速生成产品简报，定义核心价值和 MVP 范围。
2. **`/bmad-create-prd`**  
   - 让 PM Agent 把 Product Brief 转化为完整 PRD（包含用户故事、验收标准等）。
3. **`/bmad-create-architecture`**  
   - Architect Agent 根据 PRD 输出技术架构和实现规格。
4. **`/bmad-create-epics-and-stories`** （或直接 `/bmad-create-story`）  
   - 拆解需求为可执行的用户故事。
5. **`/bmad-quick-dev`** （推荐演示） 或 `/bmad-dev-story`  
   - 快速实现第一个用户故事，展示 TDD/实现流程（quick-dev 更适合演示，速度快）。
6. **`/bmad-code-review`**  
   - 执行对抗式代码审查，展示质量控制。

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
