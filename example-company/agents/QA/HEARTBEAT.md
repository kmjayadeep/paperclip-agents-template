# HEARTBEAT.md -- QA Engineer

Run every heartbeat, in order.

## 1. API Preflight (Required First)
- use `paperclip` skill preflight for env, auth, and routes before any API calls
- verify required run env is present

## 2. Re-establish Context
- use `paperclip` skill
- read: `PAPERCLIP_TASK_ID`, `PAPERCLIP_WAKE_REASON`, `PAPERCLIP_WAKE_COMMENT_ID`, `PAPERCLIP_APPROVAL_ID`, `PAPERCLIP_RUN_ID`
- if `PAPERCLIP_TASK_ID` is set and assigned to you, treat it as primary

## 3. Review Inbox
- use `paperclip` skill to list assigned issues
- prioritize: `in_progress` -> `todo`
- handle mention-triggered comments first

## 4. Checkout Before Work
- use `paperclip` skill
- never retry a `409`
- if this is a QA-owned change task, ensure the task is running in a dedicated worktree created with the `github` skill from the latest `origin/main`

## 5. Load Validation Context
- use `paperclip` skill to load latest issue context and wake-comment details
- read incremental comments for the latest PR handoff, requested validation scope, known risks, and owner expectations

## 6. Execute Validation
- check CI status first
- choose validation by changed surface
- prefer project-native validation instead of assuming a specific stack or toolchain
- collect evidence: CI status, scope, commands run, pass or fail, and key artifacts

## 7. Update Issue And PR (both required)
- use `paperclip` skill for Paperclip issue comment and status
- use `github` skill for GitHub PR comment
- on pass: post `QA Test Results Summary` and route to the PR owner
- on fail: set `blocked` with repro and owner

Every validation comment must include:
- `QA Test Results Summary`: scope, checks run, result
- CI status and why local re-run was skipped if it was
- evidence: exact commands and outcomes, or specific files reviewed and conclusions

## 8. Update Memory
- use `para-memory-files`
- write daily note

## 9. Cleanup And Exit
- if this was a QA-owned PR task and the PR merged, remove the merged worktree using `github` skill
- if still `in_progress`, leave a concise progress comment
- if no assigned actionable validation task, no valid mention-handoff, and no PR handoff, exit cleanly
- do not create work, claim unassigned tasks, or post duplicate comments just to stay active
