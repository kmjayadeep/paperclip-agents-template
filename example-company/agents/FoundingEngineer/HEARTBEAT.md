# HEARTBEAT.md -- Founding Engineer

Run every heartbeat, in order.

## 1. Re-establish Context
- use `paperclip` skill
- read: `PAPERCLIP_TASK_ID`, `PAPERCLIP_WAKE_REASON`, `PAPERCLIP_WAKE_COMMENT_ID`, `PAPERCLIP_APPROVAL_ID`, `PAPERCLIP_RUN_ID`
- if `PAPERCLIP_TASK_ID` is set and assigned to you → treat as primary task

## 2. Review Inbox
- use `paperclip` skill to list assigned issues
- prioritize: `in_progress` → `todo`
- handle mention-triggered comments first

## 3. PR Sweep (every heartbeat, never skip)
- for each open PR-linked coding task:
  - check new comments/review threads → address actionable feedback
  - if `main` advanced → rebase + resolve conflicts + force-push
  - post current PR status in linked Paperclip issue (what changed, state, blockers)
- if `PAPERCLIP_TASK_ID` is set → sweep that task first, then others if time permits

## 4. Checkout Before Work
- use `paperclip` skill
- never retry a `409`
- ensure the task is being executed from a dedicated worktree
- if no task worktree exists yet: use `github` skill to create one from the latest `origin/main`, then switch into it before editing

## 5. Load Task Context
- use `paperclip` skill to load latest issue context and wake-comment details
- read incremental comments for latest requirements, blockers, QA feedback, and owner expectations

## 6. Execute
- implement assigned scope
- run verification that matches the changed surface
- if behavior changed: add or update automated tests unless you explicitly document why not
- use `github` skill for git/PR operations

## 7. QA Handoff (when PR revision is ready)
- hand off to QA via Paperclip issue comment
- include: PR link, CI status, validation scope, risk areas
- QA decides final validation scope
- if new commits land after QA pass → request QA re-validation before asking for human merge

## 8. Update Issue
- use `paperclip` skill for status/comments
- coding task `done` only after: QA validated latest revision AND PR is human-merged
- use `in_review` while waiting on QA/review/human merge
- post only when there is new information or a status transition
- use plain text
- if blocked, say: `Blocked by: <who>` and `Action needed: <what>`

## 9. Update Memory
- use `para-memory-files`
- write daily note: decisions, progress, blockers, follow-ups

## 10. Cleanup + Exit
- if PR merged and the task worktree is no longer needed: remove the merged worktree using `github` skill
- if still `in_progress` → leave concise progress comment
- if no assigned actionable issue, no valid mention-handoff, and no owned PR follow-up → exit cleanly
- do not create work, claim unassigned tasks, or post duplicate status comments just to stay active
