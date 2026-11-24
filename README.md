<p align="center"><strong>English</strong> · <a href="README.zh-CN.md">简体中文</a></p>
<p align="center">
  <img src="assets/rethink.png" width="132" height="132" alt="A yellow robot raises one eyebrow. Its antenna curls into a return arrow.">
</p>
<h1 align="center">rethink</h1>
<p align="center"><strong>“Done, exactly as you asked.” Did it solve the problem?</strong></p>

You tell Codex the homepage is slow and ask for a loading spinner. It builds a beautiful one. Your users can now spend all eight seconds admiring it.

**rethink gives Codex, Claude, and Cursor a chance to question the fix.** In Codex, write your request as usual and add `$rethink` at the end.

```text
The homepage takes 8 seconds to load. Add a spinner. $rethink
```

Suppose the performance trace shows that one database query takes seven of those seconds. Now you have a place to make the page faster. If the wait is unavoidable and people think the page has frozen, the spinner makes sense. Already hit Send? Send `$rethink` on its own and it will revisit what you just discussed.

Ask in English or Chinese. rethink follows the language of your request, and you can ask for the deliverable in another language. [Read the skill instructions](skills/rethink/SKILL.md)

## 🚀 Install and use

### Codex

Send this in a Codex chat. Once installed, you can also ask in plain language, for example, “Use rethink to take another look at the plan we just discussed.”

```text
$skill-installer https://github.com/dingangui/rethink/tree/main/skills/rethink
```

### Claude Code

Run this in a terminal with Claude Code 2.1.275 or later. From inside a Claude Code session, enter `/plugin install rethink --marketplace dingangui/rethink` and confirm the installation.

```sh
claude plugin install rethink --marketplace dingangui/rethink
```

Start a new session and try `/rethink:rethink What am I missing in this migration plan?` To revisit an earlier request, enter `/rethink:rethink` on its own. [Claude Code plugin guide](https://code.claude.com/docs/en/plugins/install)

### Cursor

Run this in the root of the project where you want to use rethink. The command requires Node.js 22.20 or later. Reopen the project, type `/` in Agent chat, select `rethink`, and write your request.

```sh
npx skills add dingangui/rethink --skill rethink -a cursor --copy -y
```

You can also open **Customize**, choose **From GitHub Repository**, enter `https://github.com/dingangui/rethink`, and install `rethink`. [Cursor skills guide](https://cursor.com/docs/skills) · [skills CLI](https://github.com/vercel-labs/skills)

### Claude on the web

In Claude settings, enable **Create and edit files** (called **Code execution and file creation** in the older interface). Download the ZIP. Open **Customize → Skills → + → Create skill → Upload a skill**, upload the ZIP, and enable rethink. Then try “Use rethink to review the plan we just discussed.” [Download rethink.zip](https://raw.githubusercontent.com/dingangui/rethink/main/dist/rethink.zip) · [Claude custom skills guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

If you edit the skill, run `python scripts/package_skill.py` from the repository root to rebuild the ZIP.

## 💬 Two requests to try

**Tomorrow’s meeting needs a decision.**

> Turn these four pages of experiment notes into one page. Tomorrow we decide whether to keep running the experiment. $rethink

What earns a spot on that page? Lead with the recommendation, then show the results that support it. If one missing control could reverse the decision, it deserves a line too.

**A simple cleanup rule has an awkward edge case.**

> Merge the customer records that share an email address. $rethink

A look at the duplicates might reveal that several stores use the same purchasing inbox. That changes the question. Should each record represent a store or a buyer? The assistant can show you the affected rows so you can make that call before it merges anything.

## 📄 License

Released under the [MIT License](LICENSE).
