<p align="center"><a href="README.md">English</a> · <strong>简体中文</strong></p>
<p align="center">
  <img src="assets/rethink.png" width="132" height="132" alt="rethink 标志：抬起一边眉毛的黄色机器人，头顶天线弯成回头箭头">
</p>
<h1 align="center">rethink</h1>
<p align="center"><strong>不再当毫无灵魂的机器人——发送消息加上 <code>rethink</code>，让 AI 主动替你思考！</strong></p>

---

**你是否已经厌倦了 GPT、Codex 只会机械执行你的命令，却从不懂主动替你思考的痛苦？** 😤

你随手发去一个初步想法，它头也不回地按字面照搬执行——不问你真正想解决什么问题，不帮你查漏补缺，明知道方案有坑也闷头硬写，最后还一本正经地回你一句「已完成 ✅」。

**直接使用 `rethink` skill！** ⚡

下次发消息时，顺手加上 `$rethink`（或 `rethink`），让 Codex、Claude、Cursor 瞬间摆脱「毫无灵魂的执行机器」模式，变成一个**对结果负责、主动替你把关出谋划策的资深搭档**！

```text
帮我给这个接口加个内存缓存提速 $rethink
```

消息已经发出去了？直接再单独补一条 `$rethink`，它会立刻回头审视你刚才的需求和进展，帮你把没想周全的地方补齐。

## 🧠 加上 `rethink` 后，它会怎么替你思考？

收到你的需求后，它不会急着按字面埋头动手，而是按四步先帮你把事想透：

1. **🎯 先核实上下文，再复盘真实目标** —— 先查对话、代码、文件里能验证的事实，用一两句话锚定你本质上要解决什么问题、交付物怎么用、做到什么程度才算好。
2. **🔍 跳出字面要求，查漏补缺、出谋划策** —— 把「最终目的 / 硬约束」和「初步做法」分开看：*做法对不对路？有没有关键遗漏？往后看一步会不会卡住？*（如果原方案已经很周全，直接认可并采用，绝不为了显得在思考而强行挑刺。）
3. **🤝 能自己把关就先做好，涉及关键取舍先商量** —— 意图明确、改动低风险可逆时，说明补上的关键考虑后直接完善交付；遇到重大歧义、前提有隐患或高返工代价时，先停下来带着推荐方案和利弊对比找你拍板。
4. **✅ 按你想要的形态收尾** —— 要讨论就给清晰判断，要整理需求就给可直接落地的计划，要办事就直接落完并对照你的真实目标核对。

> 📄 **阅读完整技能说明：** [原版 `SKILL.md`（中文）](skills/rethink/SKILL.md) · [English Translation（逐条忠实英文译本）](skills/rethink/references/en.md)
>
> *仓库里的 `skills/rethink/SKILL.md` 与作者本机自用原版一字不差，同时提供逐条忠实翻译的英文参考版 `skills/rethink/references/en.md`。*

## 💬 看看加上 `rethink` 的真实区别

### 1. 直接替你完善并交付

> 把实验报告压成一页，明天要决定要不要继续跑 `$rethink`

- **🤖 毫无灵魂的机器人：** 机械删减字数，硬凑成一页压缩版流水账，看完还是不知道明天该怎么拍板。
- **💡 加上 `rethink` 后：** 守住「一页」的硬限制，但围绕「明天能拍板」彻底重构——先给继续/暂停建议与核心支撑数据，再补上哪条缺失证据可能翻转决定。

### 2. 提前踩刹车，带着方案来商量

> 帮我给这个接口加个内存缓存提速 `$rethink`

- **🤖 毫无灵魂的机器人：** 二话不说直接上单机内存缓存，等到上线才发现多实例之间全是脏读。
- **💡 加上 `rethink` 后：** 先查代码发现服务是多实例部署且要求强一致，不急着动手写代码——先指出单机内存缓存会带来节点间脏读，推荐改用现有 Redis 加短 TTL 的方案，讲清两者差异，等你拍板后再改。

## 🚀 安装与调用

### Codex

在 Codex 对话框中直接发送下面这行完成安装：

```text
$skill-installer https://github.com/dingangui/rethink/tree/main/skills/rethink
```

安装后，发需求时顺手加上 `$rethink`；也可以在聊了几轮后单独发一条 `$rethink`，让它回头帮你重新审视方案。

### Claude Code

在终端运行下面这行（需要 Claude Code 2.1.275 或更新版本）；如果你已经在 Claude Code 对话里，可直接输入 `/plugin install rethink --marketplace dingangui/rethink` 并确认安装：

```sh
claude plugin install rethink --marketplace dingangui/rethink
```

打开新会话，使用 `/rethink:rethink 你的需求` 调用；想让它回看刚才的讨论，直接单独发 `/rethink:rethink`。[Claude Code 插件安装说明](https://code.claude.com/docs/en/plugins/install)

### Cursor

在要使用的项目根目录运行（需要 Node.js 22.20 或更新版本）：

```sh
npx skills add dingangui/rethink --skill rethink -a cursor --copy -y
```

重新打开项目，在 Agent 聊天框输入 `/` 并选中 `rethink`，再写下你的需求。也可以在 Cursor 的 **Customize → From GitHub Repository** 中粘贴 `https://github.com/dingangui/rethink` 安装 `rethink`。[Cursor 技能说明](https://cursor.com/docs/skills) · [skills CLI](https://github.com/vercel-labs/skills)

### Claude 网页版

1. 在 Claude 设置中开启 **Create and edit files**（旧界面叫 **Code execution and file creation**）。
2. 下载 [rethink.zip](https://raw.githubusercontent.com/dingangui/rethink/main/dist/rethink.zip)。
3. 打开 **Customize → Skills → + → Create skill → Upload a skill**，上传 ZIP 并启用 `rethink`。
4. 在对话里直接说「用 rethink 帮我重新审视一下刚才的方案」。[Claude 自定义技能说明](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

如果你在本地修改了技能文件，在仓库根目录运行 `python scripts/package_skill.py` 即可重新打包 `dist/rethink.zip`。

## 📄 许可证

本项目采用 [MIT 许可证](LICENSE)。
