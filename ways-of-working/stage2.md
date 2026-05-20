# Claude Code Stage 2 — Connecting Your Tools

You've got the folder, the notes, the CLAUDE.md. Stage 2 is connecting Claude Code to the systems you actually live in.

This guide shows you how I set up my own workflow: what I tried, what works, and where there are real choices to make. Your setup will probably look different. That's the point. And whenever you get stuck on any of this, ask Claude directly. That's what it's there for.

Before you start connecting things, read **[The Approach](approach.md)**. It's short and it'll save you a lot of cleanup.

---

## What MCPs are (short version)

MCP stands for Model Context Protocol. It's a connector — a way for Claude Code to read and write to external tools. Once it's set up, you talk to Jira or Glean the same way you talk to your notes. You don't need to understand how it works. You need to know what it lets you do.

Before you start adding MCPs and skills, read **[Skills, Slash Commands, and MCPs](skills-mcps-reference.md)**. It explains what each thing costs and when adding something actually helps vs. just bloating your setup.

---

## Connecting Jira

The question isn't whether you can automate your Jira workflow. You can. The question is which approach fits how you work. Here are the two options.


### Option 1: Jira MCP (plug-and-play, if you find one that works)

Some teams run a Jira MCP server — a pre-built connector that wires Claude Code directly into Jira without any manual API work. If your setup has one, it's faster. You add a few lines to your `.mcp.json` and it works.

I don't use this. There isn't a reliable, maintained Jira MCP I've found worth recommending. If that changes, the setup is: add the server config to `.mcp.json`, restart Claude Code, and you're connected.

### Option 2: REST API + 1Password (how I actually do it)

This is more setup upfront but gives you complete control. Claude Code talks to Jira directly through the REST API — the same API Jira exposes to any developer. Your credentials live in 1Password and get pulled on demand. No tokens sitting in config files, no copy-pasting secrets.

**How it works:**

1. Your Jira API token is stored in 1Password as a Secure Note
2. When Claude needs to hit Jira, it runs `op read` to pull the token without hardcoding credentials anywhere
3. It makes a `curl` call to Jira's REST API with your email and token as basic auth

**What this looks like in practice:**

```bash
# Pull the token from 1Password
TOKEN=$(op read "op://Employee/<your-item-id>/notesPlain")

# Search your open issues
curl -s -u "you@contentful.com:$TOKEN" \
  -H "Content-Type: application/json" \
  -X POST "https://contentful.atlassian.net/rest/api/3/search/jql" \
  -d '{"jql":"assignee = currentUser() AND resolution = Unresolved","fields":["key","summary","status"]}'
```

You don't write this yourself — Claude does. But knowing it's happening this way helps you understand why 1Password needs to be running and why the token matters.

**What opens up once it's working:**

- *"What's on my plate this week?"*
- *"Summarize open items on [project]."*
- *"I just finished [task] — update the ticket."*
- *"Take my notes from this meeting and create action items as Jira tickets."*

**To get started:** You'll need to create a Jira API token at `id.atlassian.net`, store it in 1Password, and get the item reference. Ask Claude to walk you through it step by step — tell it you want to connect Jira to Claude Code using 1Password and a REST API token, and it'll guide you from there.

**Stuck on something?** Describe what you're trying to do to Claude and ask how to do it. It knows the API.

---

## Connecting Glean

Before adding this, ask yourself: do I search Glean often enough that having it always wired in is worth the overhead? For most people in this role, yes. This one earns its place. Connecting it to Claude Code means you can search the company knowledge base, pull agent details, and reference internal docs, all without leaving your terminal.

**Setup:** You'll need a Glean API token and an `.mcp.json` config block. Ask Claude to walk you through it — tell it you want to connect Glean to Claude Code via MCP and it'll figure out the right config with you.

**What opens up:**

- *"What agents exist for [team or use case]?"*
- *"Pull the knowledge base for [agent] and tell me what's missing."*
- *"Search for anything we have on [topic]."*
- *"What did [person] share in Glean about [topic]?"*

**Stuck on something?** Ask Claude. If you can describe what you want to find or do in Glean, it can help you figure out the right query or approach.

---

## Add skills (slash commands)

Skills are where the "how, not if" mindset pays off most directly. Processing meeting notes, creating stakeholder visuals, running standups: each can become a single command. The question isn't whether you can build that. It's which friction points are real enough to be worth it.

Add a skill when you've hit the same friction three or more times. Not before.

Claude Code ships with basic capabilities, but you can extend it with skills: slash commands that give Claude a specialized behavior on demand. There are several worth knowing about. You can find them, try them, and add the ones that fit how you work.

**How to find what's available:**

Ask directly:

- *"What skills or slash commands are available in this setup?"*
- *"Show me what /visual-explainer does."*

**One to start with — `/visual-explainer`:**

Describe anything — a plan, an agent architecture, a set of options — and this skill turns it into a clean HTML diagram you can open in a browser or drop into a doc. If you've ever been in a stakeholder conversation trying to explain how a Glean agent works and wished you had something to point at, this is that thing.

Try it. Describe an agent you're working on and run `/visual-explainer`. See what comes out.

The output is an HTML file. You can open it in a browser, drop it into a doc — or push it to a GitHub repo and have it live as a real URL you can share with anyone. That's how the [Ways of Working journey diagram](https://charlie-fuller.github.io/diagrams/tyler/tyler-journey.html) was made and published. One Claude session, one skill, a GitHub push — shareable link.

**How to add a skill:**

Skills live in a `.claude/agents/` or skills directory. Drop the file in and it's available. No code required.

Once you've run visual-explainer, ask Claude which other skills exist and what they do — it can show you what's available and help you decide what's worth adding.

---

## Try it all together

This is where the approach pays off. A lean setup — two connections, a skill or two, tools you actually use — does more than a sprawling one. The leverage comes from combining your context with live data, not from having the most tools installed.

Once Jira and Glean are both connected:

- *"I'm meeting with [team lead] tomorrow about their Glean adoption. Pull their tickets and any relevant Glean content and give me a brief."*
- *"Take the action items from my meeting note today and create Jira tickets."*
- *"What open Jira items are connected to [initiative]?"*

---

Get Glean running first. It's the faster win. Jira takes a bit more setup but changes how you work once it's there. And at any point, if you don't know how to do something, ask Claude. That's the whole skill — learning to ask.
