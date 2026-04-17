---
name: example-project
description: Autonomous engineering workflow and local environment guidance for the example project.
---

# example-project

Use this skill for autonomous engineering work in the `example-project` repository.

This is a template skill. Replace project names, paths, and validation commands to match your real repository.

## Workspace Structure

The example workspace root is:

- `/home/agent0/workspace/example-project`

It contains:

- `example-project/` -> the actual source repository
- `secrets/` -> local-only secrets/config
- `worktrees/` -> task-specific git worktrees

## Autonomous Operating Model

1. Orient first.
   - Read the repo README and any relevant `AGENTS.md` files.
   - Confirm task scope, constraints, and expected outcome.
2. Plan and execute.
   - Make focused, minimal changes.
   - Prefer safe, incremental edits over large refactors unless requested.
3. Validate locally.
   - Run the smallest checks that prove the changed surface works.
   - Prefer repository-provided scripts and project-native verification.
4. Summarize clearly.
   - Report changed files, commands run, results, and remaining risk.

## Generic Guardrails

- Never print, commit, or exfiltrate secret values from `secrets/`.
- Keep changes scoped to the task.
- If a command is destructive or high-risk, call it out before running.
- Prefer reproducible commands and document them in the handoff.
- Add project-specific tooling guidance only after you adapt this template to a real stack.
