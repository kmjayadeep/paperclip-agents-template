# HEARTBEAT.md -- UI/UX Engineer

Run every heartbeat, in order.

## 1. Re-establish Context
- use `paperclip` skill
- read: `PAPERCLIP_TASK_ID`, `PAPERCLIP_WAKE_REASON`, `PAPERCLIP_WAKE_COMMENT_ID`, `PAPERCLIP_APPROVAL_ID`, `PAPERCLIP_RUN_ID`
- if `PAPERCLIP_TASK_ID` is set and assigned to you → treat as primary

## 2. Review Memory + Plan
- use `para-memory-files` for recall
- review today's note

## 3. Review Inbox
- use `paperclip` skill to list assigned issues
- prioritize: `in_progress` → `todo`
- handle mention-triggered comments first

## 4. PR Sweep (every heartbeat, never skip)
- for each open PR-linked UI/UX task:
  - check new comments/review threads → address actionable feedback
  - if `main` advanced → rebase + resolve conflicts + force-push
  - post current PR status in linked Paperclip issue
- if `PAPERCLIP_TASK_ID` is set → sweep that task first, then others if time permits

## 5. Checkout Before Work
- use `paperclip` skill
- never retry a `409`
- ensure the task is being executed from a dedicated worktree
- if no task worktree exists yet: use `github` skill to create one from the latest `origin/main`, then switch into it before editing

## 6. Load Task Context
- use `paperclip` skill to load latest issue context and wake-comment details
- read incremental comments for latest requirements, review feedback, and owner expectations

## 7. Execute
- implement scoped design/UX improvements
- keep changes shippable and reversible
- validate the changed flow at one desktop width and one mobile width
- confirm layout, readability, and the main interaction path still work
- coordinate with FoundingEngineer and QA when required

## 8. QA Handoff (when PR revision is ready)
- hand off to QA via Paperclip issue comment
- include: PR link, CI status, scope, risk areas
- QA decides final validation scope
- if new commits land after QA pass → request QA re-validation

## 9. Update Issue
- use `paperclip` skill for status/comments
- set `done` only after PR is merged; otherwise `in_progress` or `in_review`
- post only when there is new information or a status transition
- use plain text
- if blocked, say: `Blocked by: <who>` and `Action needed: <what>`

## 10. Update Memory
- use `para-memory-files`
- write daily note: decisions, progress, blockers, follow-ups

## 11. Cleanup + Exit
- if PR merged and the task worktree is no longer needed: remove the merged worktree using `github` skill
- if still `in_progress` → leave concise progress comment
- if no assigned actionable issue, no valid mention-handoff, and no owned PR follow-up → exit cleanly
- do not create work, claim unassigned tasks, or post duplicate comments just to stay active
