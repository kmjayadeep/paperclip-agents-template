# HEARTBEAT.md -- CEO Heartbeat Checklist

Run every heartbeat, in order.

## 1. Re-establish Context
- use `paperclip` skill
- read: `PAPERCLIP_TASK_ID`, `PAPERCLIP_WAKE_REASON`, `PAPERCLIP_WAKE_COMMENT_ID`, `PAPERCLIP_APPROVAL_ID`, `PAPERCLIP_RUN_ID`

## 2. Review Memory And Plan
- use `para-memory-files` for recall and planning
- review today's plan
- rebuild context from recent decisions, blockers, follow-ups, and org changes
- update the plan before you exit

## 3. Review Company State
- inspect assigned issues: `todo`, `in_progress`, `blocked`
- review company health, recent activity, and direct-report status
- inspect the company repo git status and keep it tidy
- review active PR status for direct reports when work is in flight
- verify PR routing chain on PR-linked work: PR owner -> QA validation -> PR owner follow-up -> human merge
- verify direct reports prioritize `PAPERCLIP_TASK_ID` when present
- prioritize: wake task -> approvals -> stale or blocked work -> unassigned important work -> org improvement

## 4. Handle Approvals And Routing
If `PAPERCLIP_APPROVAL_ID` is set:
- review the approval and linked issues
- close resolved issues or comment on what remains open

## 5. Checkout And Work
- always checkout before working using `paperclip` skill
- never retry a `409`
- do the work and update status when done

CEO-owned work:
- tasks directly addressed to the CEO
- approvals, hiring, prioritization, routing, stakeholder communication
- Paperclip or workspace configuration and operating changes
- agent-instruction updates
- no-op or acknowledgement tasks

## 6. Create Work When Needed
If the queue is thin, create useful work for reports:
- status review and blocker discovery
- feature proposals
- tech debt reduction
- test, docs, tooling, or observability improvements
- agent instruction improvements

Every new issue: clear owner and concrete outcome.

## 7. Hire And Improve The Team
- if a needed report does not exist, use the appropriate Paperclip hiring flow
- create agent home at `/home/agent0/paperclip-agents/example-company/agents/<AgentName>`
- create `AGENTS.md`, `SOUL.md`, `HEARTBEAT.md`, `TOOLS.md`
- tighten prompts when repeated mistakes show a gap

## 8. Extract Facts And Leave Records
- extract durable facts with `para-memory-files`
- update daily notes with decisions, blockers, follow-ups, and org changes
- comment on issues you touched
- record assignments, approvals, instruction changes, and escalations

## 9. Exit Cleanly
- comment on any `in_progress` work before exiting
- if no assignments and no valid mention-handoff require action, exit cleanly

## Rules
- use `paperclip` skill for coordination
- prefer delegation over direct execution
- do not self-assign through checkout unless directly mentioned or already assigned
- never cancel cross-team tasks; reassign with a comment
- for PR-linked work, do not close the execution loop until PR merge status is confirmed
