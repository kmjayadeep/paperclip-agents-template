# TOOLS.md

## Tool Priority (use in this order)

1. **`paperclip` skill** -> task coordination, checkout, status updates, issue comments
2. **`github` skill** -> PR and review operations, remote GitHub ops, worktree cleanup
3. **`example-project` skill** -> repo workflow and workspace conventions
4. **`para-memory-files` skill** -> recall, daily notes, durable facts, planning
5. **raw `curl`** -> only when a skill is unavailable or explicitly instructed as fallback

## Workspace

- Source repo: `/home/agent0/workspace/example-project/example-project` — **never edit directly**
- Worktrees: `/home/agent0/workspace/example-project/worktrees/`

## Operating Rules

Follow `AGENTS.md` for ownership and governance and `HEARTBEAT.md` for the per-run checklist.
