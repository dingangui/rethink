<p align="center">
  <img src="assets/rethink.png" width="132" height="132" alt="rethink 的黄色机器人抬起一边眉毛，头顶的天线弯成回头箭头">
</p>
<h1 align="center">rethink</h1>
<p align="center"><strong>「都按你说的做完了。」那我的问题解决了吗？</strong></p>

有没有被 GPT 或 Codex 的一句「已完成 ✅」气到过？你说首页打开太慢，想加个加载动画。它交付了一个漂亮的转圈圈。现在，你的用户可以很优雅地再等八秒了。

**给那个只会说「收到」的机器人装上 rethink。** 下次在 Codex 里照常写需求，末尾加一个 `$rethink`，让它主动替你多想一步。

```text
首页打开要 8 秒，帮我加个加载动画。 $rethink
```

这一次，它会先看手头的性能记录。要是时间都花在一条慢查询上，你就有了缩短等待的切入点。要是耗时暂时省不掉、用户又总以为页面卡死，那个动画就值得做。已经发完需求了？再单独补一条 `$rethink`，它会接着刚才的对话想。

## 🚀 安装与调用

### Codex

在 Codex 对话框里发送下面这行。安装后，除了点名 `$rethink`，也可以用一句自然语言接着聊，比如「用 rethink 重新看看刚才的方案」。

```text
$skill-installer https://github.com/dingangui/rethink/tree/main/skills/rethink
```

### Claude Code

在终端运行下面这行（Claude Code 2.1.275 或更新版本）。如果你已经在 Claude Code 对话里，可以直接发送 `/plugin install rethink --marketplace dingangui/rethink` 并确认安装。

```sh
claude plugin install rethink --marketplace dingangui/rethink
```

打开新会话，用插件的完整命令开头，例如 `/rethink:rethink 帮我看看这个迁移方案漏掉了什么`。想让它回看刚才的讨论，就单独发 `/rethink:rethink`。[Claude Code 插件安装说明](https://code.claude.com/docs/en/plugins/install)

### Cursor

在要使用它的项目根目录运行下面这行，需要 Node.js 22.20 或更新版本。重新打开项目，在 Agent 聊天框键入 `/`，搜索并选中 `rethink`，再写需求。

```sh
npx skills add dingangui/rethink --skill rethink -a cursor --copy -y
```

也可以在 Cursor 的 **Customize** 里选择 **From GitHub Repository**，粘贴 `https://github.com/dingangui/rethink`，然后安装 `rethink`。[Cursor 技能说明](https://cursor.com/docs/skills) · [skills CLI](https://github.com/vercel-labs/skills)

### Claude 网页版

在 Claude 设置里开启 **Create and edit files**（旧界面叫 **Code execution and file creation**）。下载 ZIP 原包，到 **Customize → Skills → + → Create skill → Upload a skill** 上传并启用。随后在对话里试一句「用 rethink 帮我过一遍刚才的计划」。[下载 rethink.zip](https://raw.githubusercontent.com/dingangui/rethink/main/dist/rethink.zip) · [Claude 自定义技能说明](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

如果你改过技能，在仓库根目录运行 `python scripts/package_skill.py` 就能重新生成 ZIP。

## 💬 两个值得试的场景

**明天开会，要决定一个实验还值不值得跑。**

> 把这四页实验记录压成一页，明天要决定还追不追这条线。 $rethink

一页里最该留下什么？它会先写继续或暂停的建议，再挑出支撑判断的数据。如果补一组对照就可能翻转结论，这组对照也值得占一行。

**准备合并重复记录，规则看起来很简单。**

> 客户表里有些邮箱重复了，帮我按邮箱合并。 $rethink

它会先看重复项长什么样。一旦发现几家门店共用同一个采购邮箱，它就有理由先列出待确认的记录，问你按门店还是按采购主体合并。这个决定由你拍板。

## 📄 许可证

本项目采用 [MIT 许可证](LICENSE)。
