---
name: rethink
description: Review a proposed approach before acting. Use when the user appends rethink or $rethink to a request, invokes the skill on its own or through their client, or asks for a second look at goals, gaps, and trade-offs.
license: MIT
---

# rethink

[简体中文](references/zh-CN.md)

The user has a goal and may already have a way to reach it in mind. Help them work out whether that approach will deliver what they need. A straightforward request for literal execution can be handled directly.

Reply in the language of the user's request. For a standalone invocation, use the language of the request it refers to. Honor any explicit language choice for the reply or deliverable. Use English when there is no language cue.

1. **Check the context and identify the goal.**
   Look for facts you can verify in the conversation, code, files, or available tools. When the user appends `rethink` or `$rethink`, review that request. When they send only the skill name or a client invocation, look back at the latest request, corrections, and work already completed. Ask for context only if you cannot tell what they mean. Sum up the outcome, how the user will use it, and what success looks like in one or two sentences.

2. **Look for gaps that could change the result.**
   Distinguish the user's goal and firm constraints from their suggested implementation. Consider three questions.
   - Would the proposed approach solve the underlying problem? Is there a simpler, more reliable, or less costly way to get there?
   - Which assumption, edge case, dependency, or acceptance criterion could lead to rework if overlooked?
   - Where might the user run into trouble when they put the result to use or extend it?

   Raise only points that materially affect the outcome. If the original plan holds up, say so briefly and use it.

3. **Act on clear improvements and discuss consequential choices.**
   When the intent is clear and an improvement is low-cost, reversible, and within scope, explain any important assumption and carry it through. If the goal is ambiguous, a premise fails, a decision would be expensive to undo, or a better approach would change an explicit requirement, pause the work that depends on that choice. Recommend an option, explain what makes it preferable and what an alternative would cost, and ask only what the user needs to decide.

4. **Deliver what the user asked for.**
   For a discussion, give a clear judgment and reasoning. For a specification or plan, produce something the user can put to work. For an action, carry it out, check the result against the original goal, and briefly mention any important gap you addressed.

## Examples

- **Make the improvement and deliver.** The user asks for a one-page experiment report because tomorrow's meeting will decide whether to keep running it. Keep the one-page limit. Lead with a recommendation, include the evidence behind it, and identify any missing evidence that could change the decision.
- **Bring the choice back to the user.** The user suggests an in-memory cache to speed up a pricing endpoint. The service runs across multiple instances, and a committed price change must be visible immediately. Local caches can serve old prices. A shared cache with a short TTL still has a window in which a price can be stale. Check the slow query and ask which data, if any, can tolerate a delay before deciding what to cache.
