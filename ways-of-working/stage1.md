# Claude Code Setup — Getting Started

This is not a tool course. It is a mindset course that happens to use tools.

Everyone's role is different. But the underlying tasks are remarkably similar across jobs: making sense of information, moving work forward, communicating clearly, keeping context across conversations and meetings. And the same approaches apply to all of them.

The goal is a different way of working. AI handles the synthesis: pulling information together, surfacing context, drafting, summarising, tracking what was said and decided. That frees you for thinking. And thinking is not one thing:

1. Framing the right problem.
2. Judgment — making the call when the data doesn't decide for you.
3. Evaluation — interrogating whether something is actually true or just sounds true.
4. Empathy — modeling how other people will experience what you're building.
5. Systems reasoning — tracing second and third-order effects before you act.
6. Perspective-shifting — deliberately seeing through a lens that isn't yours.
7. Sense-making — the step between having all the information and knowing what it means.

Synthesis is the cost of entry. Thinking is the value creation. That is what this course is trying to give you more of.

Getting there does not mean installing everything or following a fixed path. It means developing judgment about what fits how you work, and applying it to the tasks already in front of you.

---

## Step 1: Get Claude Code installed

Install Claude Code via your terminal:

```
npm install -g @anthropic-ai/claude-code
```

Once installed, run:
```
claude
```

That's it. You're in.

---

## Step 2: Set up your folder

Create a folder on your computer. Call it `vault` or anything you want. Inside it:

```
vault/
├── meetings/         <- one file per meeting, named Person1-Person2_YYYY-MM-DD.md
├── projects/         <- one file per active project or initiative
├── strategy/         <- thinking docs, not project docs
├── team/             <- notes about people you work with regularly
└── CLAUDE.md         <- tell Claude who you are (see Step 4)
```

This is just folders and text files. Nothing special required.

**Obsidian (optional but recommended)**
Obsidian is a free app that renders these files nicely and syncs across devices for ~$5/month. Install it and point it at this folder. Two plugins worth adding: **Dataview** and **Templater**. Everything works without it too. A plain folder works.

---

## Step 3: Start writing meeting notes

Every meeting gets a file. Use this format:

**Filename:** `You-Them_YYYY-MM-DD.md`

**Contents:**
```markdown
---
date: YYYY-MM-DD
participants: [Your Name, Their Name]
topic: what you talked about
---

## What we covered

## Decisions

## Actions
- [ ] You:
- [ ] Them:

## Open questions
```

Fill in as much or as little as you want. Rough notes work. Over time, Claude Code uses these to surface context and action items without you having to remember everything.

**Transcript shortcut:** Record meetings with MacWhisper (or any transcription app), drop the .txt into your meetings folder, then ask Claude Code: *"Turn [filename] into a structured meeting note."*

---

## Step 4: Create your CLAUDE.md

This file is read at the start of every Claude Code session. It's how Claude knows who you are, what you're working on, and how to help you. Start simple.

Create `vault/CLAUDE.md`:

```markdown
# About

[Your name], [your role] at Contentful.
[One sentence on what you work on.]

## What I'm focused on right now

- [Current initiative or project]
- [What you're learning or building]
- [Who you're supporting or working with]

## Folder structure

- meetings/    <- meeting notes, named Person1-Person2_YYYY-MM-DD.md
- projects/    <- active project files
- strategy/    <- strategic thinking
- team/        <- notes on people

## How I work

[One or two sentences on how you operate: what helps you do your best work,
what context Claude should carry into every session.]
```

Update this as things change. It doesn't need to be long — just accurate.

---

## Step 5: Try it

With your folder set up and CLAUDE.md in place, open your terminal, navigate to your vault folder, and run `claude`. Then try:

- *"What meetings do I have notes from this week?"*
- *"What are my open action items?"*
- *"Draft a Slack message to [name] about [topic]."*
- *"I'm meeting with [person] tomorrow — what's our history?"*

---

Once you've done all five steps, you're ready for Stage 2.
