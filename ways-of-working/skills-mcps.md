# Skills, Slash Commands, and MCPs — What They Are and When to Add Them

Before you start adding things, read this. It'll save you a lot of cleanup later.

---

## The three things

**Slash commands** and **skills** are the same thing. A skill is a slash command with instructions attached: type `/visual-explainer` and Claude loads those instructions and runs them. The terms get used interchangeably. Don't let that confuse you.

**MCPs** (Model Context Protocol servers) are different. A skill lives in a file on your machine and gets loaded when you call it. An MCP is a running service — a connector between Claude Code and an external tool like Jira, Glean, or a database. It's always on, always present, whether you use it in a given session or not.

That distinction matters a lot.

---

## The cost of adding things you don't use

Every time you start a Claude Code session, it loads context. That context has a token budget, and everything you've added takes a slice before you've typed a word.

**MCPs are the expensive part.** Each MCP server loads its full list of available tools into context at the start of every session. You don't need to use them. They load anyway. An MCP with 20 tools costs you the tokens to describe all 20 tools, every session, whether you touched any of them or not. Add five MCPs and you've burned a significant chunk of your context budget on overhead before the conversation starts. That means:

- Slower responses (more to process upfront)
- Less room for the actual work in a long session
- The model has more noise to reason through before getting to your question

**Skills are cheaper but not free.** A skill only loads when you call it, so idle skills don't cost you anything. But a long list of available skills still creates a kind of decision overhead — Claude has to reason about which skill applies when you're working. More isn't better. A focused set of skills you actually reach for beats a sprawling library you mostly ignore.

---

## When to add a skill

One test: have you done this thing manually three or more times and wished it worked differently?

If yes, a skill might be worth building or adding. If no, just ask Claude directly — you don't need a skill for a one-off task. The value of a skill is repeatability and consistency, not novelty.

Good reasons to add a skill:
- You do the same type of thing regularly and want Claude to approach it the same way every time
- The instructions for doing it well are long enough that you don't want to re-explain them each session
- You want a shorthand — `/standup` is faster than explaining your standup format from scratch

Bad reasons to add a skill:
- It seems like it might be useful someday
- Someone else has it and it looks cool
- You want to explore what it does (just ask Claude about it instead)

---

## When to add an MCP

Same test, higher bar. MCPs are heavier than skills, so the question is: do you connect to this tool regularly enough that having it always wired in is worth the constant overhead?

Good reasons to add an MCP:
- You use this tool in most sessions
- The alternative (REST API calls, manual lookup) is slow enough that you're avoiding the tool because of the friction
- The tool has enough complexity that Claude benefits from native access rather than you describing the API

Bad reasons to add an MCP:
- The tool exists and you might need it
- Someone shared a config and it was easy to paste in
- You want to try it once to see what happens

Try the tool manually first. Ask Claude to help you hit the API directly. If you find yourself doing that repeatedly and wishing it were faster, that's when an MCP earns its place.

---

## The rule

**Add things in response to friction, not in anticipation of it.**

A lean setup with three tools you use every day will outperform a loaded setup with fifteen tools you added because they seemed useful. The overhead is real and it compounds. Every session you start with a bloated config is a session where you're paying for things you didn't need.

Start minimal. Add when something repeatedly slows you down. Remove things that aren't pulling their weight.

---

*For setup instructions on specific MCPs and skills, see the Stage 2 guide.*
