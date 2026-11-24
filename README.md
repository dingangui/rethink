<p align="center"><strong>English</strong> · <a href="README.zh-CN.md">简体中文</a></p>
<p align="center">
  <img src="assets/rethink.png" width="132" height="132" alt="rethink logo: a curious yellow robot raising one eyebrow with its antenna curling into a return arrow">
</p>
<h1 align="center">rethink</h1>
<p align="center"><strong>Stop settling for a soulless robot. Add <code>rethink</code> and make your AI actually think for you.</strong></p>

---

**Tired of GPT and Codex mechanically executing your commands without ever stopping to think for you?** 😤

You toss over a rough idea, and it charges straight ahead word for word—never asking what you're really trying to solve, never catching the edge cases you missed, walking straight into obvious traps, and proudly reporting *"Done ✅."*

**Just use the `rethink` skill!** ⚡

Add `$rethink` (or `rethink`) to your prompt, and turn Codex, Claude, and Cursor from a **soulless order-taking robot** into a **proactive senior partner** who thinks ahead, catches blind spots, and owns the outcome with you!

```text
Add an in-memory cache to this endpoint to speed it up. $rethink
```

Already hit Send? Just drop `$rethink` on its own in the next message—it will step back, review what you just discussed, and help you think it through before things go off track.

## 🧠 What changes when you add `rethink`?

Instead of blindly executing word for word, your AI follows four sharp steps:

1. **🎯 Verify context & lock onto the real goal** — Checks the conversation, codebase, and files first, then sums up what problem you're *actually* solving and what "good" looks like.
2. **🔍 Think beyond the literal words** — Separates your real goal from your rough initial idea: *Is this approach on the right track? What's missing? Where will it get stuck one step later?* (And if your plan is already solid, it says so—no fake nitpicking.)
3. **🤝 Own the obvious wins, talk through the big trade-offs** — Quietly fills in low-risk, reversible best practices and delivers; pauses with a concrete recommendation when a decision is risky, ambiguous, or costly to undo.
4. **✅ Deliver in the form you need** — Clear judgment for a discussion, a ready-to-use plan for specs, or verified execution checked against your true goal.

> 📄 **Read the full skill:** [English Translation (line-by-line faithful)](skills/rethink/references/en.md) · [Original `SKILL.md` (Chinese)](skills/rethink/SKILL.md)
>
> *`skills/rethink/SKILL.md` preserves the author's exact local prompt verbatim, with a strict line-by-line English translation right beside it in `skills/rethink/references/en.md`. Modern models follow it seamlessly and respond in the language of your conversation.*

## 💬 See the difference in action

### 1. Improve & deliver directly

> Compress the experiment report into one page—tomorrow we decide whether to keep running it. `$rethink`

- **🤖 Without `rethink`:** Mechanically cuts paragraphs until it fits one page, leaving you with a dense summary that doesn't help anyone make a call.
- **💡 With `rethink`:** Respects the hard one-page limit, but restructures around *"making the decision tomorrow"*—leading with a clear go/pause recommendation, the core supporting data, and which missing piece of evidence could flip the call.

### 2. Catch the trap & bring a better plan

> Add an in-memory cache to this endpoint to speed it up. `$rethink`

- **🤖 Without `rethink`:** Immediately writes a local in-memory cache, introducing cross-node dirty reads across your production instances.
- **💡 With `rethink`:** Inspects the codebase first, sees the service runs across multiple instances with strong consistency requirements, stops before coding, flags the dirty-read risk, recommends using the existing Redis with a short TTL instead, explains the trade-offs, and waits for your sign-off.

## 🚀 Install & use

### Codex

Send this in a Codex chat to install:

```text
$skill-installer https://github.com/dingangui/rethink/tree/main/skills/rethink
```

Then just append `$rethink` to any request—or send `$rethink` on its own to review what you just discussed.

### Claude Code

Run in a terminal (Claude Code 2.1.275 or later), or inside a Claude Code session run `/plugin install rethink --marketplace dingangui/rethink`:

```sh
claude plugin install rethink --marketplace dingangui/rethink
```

Start a new session and invoke `/rethink:rethink <your request>`, or send `/rethink:rethink` on its own to revisit the current discussion. [Claude Code plugin guide](https://code.claude.com/docs/en/plugins/install)

### Cursor

Run in your project root (requires Node.js 22.20 or later):

```sh
npx skills add dingangui/rethink --skill rethink -a cursor --copy -y
```

Reopen the project, type `/` in Agent chat, select `rethink`, and write your request. You can also install via **Customize → From GitHub Repository** using `https://github.com/dingangui/rethink`. [Cursor skills guide](https://cursor.com/docs/skills) · [skills CLI](https://github.com/vercel-labs/skills)

### Claude on the web

1. Enable **Create and edit files** (previously **Code execution and file creation**) in Claude settings.
2. Download [rethink.zip](https://raw.githubusercontent.com/dingangui/rethink/main/dist/rethink.zip).
3. Go to **Customize → Skills → + → Create skill → Upload a skill**, upload the ZIP, and enable `rethink`.
4. Say *"Use rethink to review the plan we just discussed."* ([Claude custom skills guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude))

If you modify the skill locally, run `python scripts/package_skill.py` from the repository root to rebuild `dist/rethink.zip`.

## 📄 License

Released under the [MIT License](LICENSE).
