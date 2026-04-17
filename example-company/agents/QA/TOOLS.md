# TOOLS.md

## Tool Priority (use in this order)

1. **`paperclip` skill** -> task coordination, checkout, status updates, issue comments
2. **`github` skill** -> PR comments, remote GitHub ops, worktree cleanup for QA-owned PRs
3. **`example-project` skill** -> repo workflow, conventions, and validation references
4. **`para-memory-files` skill** -> recall, daily notes, durable facts
5. **project-native validation tools** -> only when the task requires local validation beyond CI
6. **raw `curl`** -> only when a skill is unavailable or explicitly instructed as fallback

## Validation Rules

- CI first: check CI status for unit, lint, type, build, or equivalent checks. Do not re-run those locally unless CI failed or explicitly requested.
- Use repo-provided scripts or project-native checks when they validate behavior beyond CI.
- Keep local validation proportional to the changed surface.

## Operating Rules

Follow `AGENTS.md` for ownership and governance and `HEARTBEAT.md` for the per-run checklist.
