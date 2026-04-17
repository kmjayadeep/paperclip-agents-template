---
name: github
description: GitHub workflow, authentication, branching, worktree, and pull request rules for the example project.
---

# Github

Use this skill whenever you are dealing with GitHub operations for the `example-project` repository.

This is a template. Replace the placeholder paths, repository details, and authentication method to match your environment.

## Scope

Use for:

- `gh` CLI usage
- authenticated `git fetch`, `git push`, and PR branch updates
- pull request creation and review response flow
- branch/worktree workflow tied to Paperclip issues

## Authentication

Before `gh` or authenticated git operations, export `GITHUB_TOKEN` using the helper script inside this skill directory, or replace this with your preferred auth flow.

```bash
export GITHUB_TOKEN="$(python3 /home/agent0/paperclip-agents/example-company/skills/github/scripts/get-github-token.py)"
```

Then verify auth before push or PR operations:

```bash
gh auth status -h github.com
```

## Source Of Truth

The example main repo lives under `/home/agent0/workspace/example-project/example-project`.

Keep it up to date with upstream:

```bash
cd /home/agent0/workspace/example-project/example-project
git pull origin main
```

Do not make changes directly in this folder.

## Repo And Branch Rules

- Never commit directly to `main`.
- Never push directly to `main`.
- All changes go through pull requests via dedicated branches.
- Use a descriptive branch and commit naming scheme tied to the Paperclip issue id.

## Worktree Flow

Create a dedicated worktree per task:

```bash
cd /home/agent0/workspace/example-project/example-project
git fetch origin
git worktree add -b task-123-short-description ../worktrees/task-123-short-description origin/main
cd ../worktrees/task-123-short-description
```

Worktrees live under `/home/agent0/workspace/example-project/worktrees/`.

After the PR is merged and the worktree is no longer needed, clean it up:

```bash
cd /home/agent0/workspace/example-project/example-project
git worktree remove ../worktrees/task-123-short-description
git branch -d task-123-short-description
```

Only remove the worktree after confirming the PR is merged and no further work is expected.

## PR Flow

Push and open a PR:

```bash
git push -u origin task-123-short-description
```

PR requirements:

- title includes the issue id
- description links the related Paperclip issue
- include an `Authored-by:` line naming the working agent
- keep descriptions plain and readable
- summarize command output instead of pasting large logs

## Sync With Main

When `main` advances, rebase your branch:

```bash
git fetch origin
git rebase origin/main
git push --force-with-lease
```

Never merge `main` into your branch.

## Review And Comment Hygiene

- apply review feedback in the same worktree
- re-push after each change round
- mark review threads resolved after updates
- keep commits atomic
- keep PR comments concise and readable
- include the acting agent name in status and review updates when useful
