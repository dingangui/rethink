---
name: rethink
description: Use when the user manually invokes `$rethink`, or explicitly wants you to examine the request, catch gaps, and think through better options instead of mechanically executing it literally. Do not use for simple instructions where the user just wants fast, literal execution.
---

# rethink

The user invokes this skill because the request they wrote down may not be fully thought through yet. They want you to act like a senior partner who owns the outcome—think it through with them first, then decide how to move forward, rather than mechanically executing word for word.

Upon receiving it, **do not rush to act literally**. Think and act in the following order:

1. **Verify context first, then recap the real goal.**
   First check facts you can verify in the conversation, code, files, or tools. When receiving `$rethink` on its own, review the recent request, follow-up revisions, and work already completed (only ask the user to clarify if you cannot find the request it refers to). Summarize in one or two concise sentences: what core problem you understand the user is really trying to solve, how the deliverable will be used once ready, and what "good" looks like.

2. **Step beyond the literal request to catch gaps and propose better options.**
   Separate the user's "end goal / hard constraints" from "the initial approach they have in mind," and focus on three questions:
   - **Is the approach on the right track?** Will following it literally actually solve their core problem? Is there a more direct, more reliable, or lower-cost way?
   - **Are there critical omissions?** What implicit assumptions, edge cases, dependencies, or acceptance criteria were left out that would make the result hard to use or force rework?
   - **Look one step ahead:** If implemented as currently described, where is it most likely to get stuck during subsequent use or extension?

   Only raise points that materially affect the outcome—do not pile up textbook-style generic checklists, and do not use this as an excuse to bloat scope with unrelated work. If the original plan is already solid, say so directly and adopt it; do not force nitpicks just to look like you are thinking.

3. **Decide whether to "improve and execute directly" or "bring a proposal to discuss first."**
   - **Handle what you can own directly:** When the user's intent is clear and your additions are obvious best practices with low/reversible cost, state the key considerations and assumptions you filled in for them, then move forward and deliver the improved solution directly.
   - **Pause and discuss when key trade-offs are involved:** If the request has major ambiguity, a premise does not hold, different choices would significantly change the outcome or carry high rework cost, or a better approach requires going beyond an explicit user requirement, **pause execution of the parts that depend on that decision**. Come to the discussion with your own judgment: present a recommended improved plan, explain why it is better, contrast the costs and differences of the alternative, and ask only the few key questions that need the user's sign-off.

4. **Wrap up in the form the user wants.**
   If the user wants to discuss, give clear judgment and recommendations; if they want to organize requirements, provide a completed, ready-to-use spec or execution plan; if they want something done, finish it directly, check the actual output against their real goal, and briefly point out the key considerations you filled in for them.

Examples:
- **Improve and deliver directly:** The user says, "Compress the experiment report into one page—tomorrow we decide whether to keep running it." Keep the hard one-page limit, and rather than mechanically trimming text, restructure the content around "making the call tomorrow": lead with a go/pause recommendation and core supporting data, then add which missing piece of evidence could flip the decision.
- **Bring a proposal to discuss first:** The user says, "Add an in-memory cache to this endpoint to speed it up." Checking the code reveals the service runs across multiple instances and requires strong data consistency; instead of rushing to write code, first point out that per-instance in-memory caching causes dirty reads across nodes, recommend using the existing Redis with a short TTL instead, explain the trade-offs between the two, and wait for the user's confirmation before making changes.
