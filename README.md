# paperclip-agents-template

A public template for building a role-based Paperclip company around a real project.

This repository is intentionally generic. It is meant to be copied and adapted, not used as-is. Everywhere you see names like `example-company` or `example-project`, replace them with your own company and project identifiers.

Paperclip docs: https://docs.paperclip.ing/start/what-is-paperclip

## Customize This Template

When you adapt this repo:

1. Rename `example-company` to your Paperclip company name.
2. Rename `example-project` to your real repo and workspace name.
3. Replace placeholder paths, repository names, and auth details.
4. Add project-specific setup only in your derived repo.

## What This Template Contains

This repo models a Paperclip company with:

- a `CEO` agent that handles routing, prioritization, approvals, and process improvement
- specialist execution agents such as `FoundingEngineer`, `DocumentationEngineer`, `UIUXEngineer`, and `QA`
- per-agent instruction files for role boundaries, tone, recurring heartbeat routines, and tool usage
- a shared company directory that contains skills and workspace bootstrap placeholders

The intended loop is:

1. The CEO receives or reviews work.
2. The CEO assigns the correct owner.
3. Specialists execute in dedicated worktrees against the real source repository.
4. QA validates the changed surface.
5. The PR owner follows up on QA feedback.
6. A human or repo owner merges.

That gives you a reusable starting point for a self-correcting agent org: management, execution, QA, memory, and prompt/process refinement.

## Template Naming

This template uses placeholder names on purpose:

- `example-company` -> your Paperclip company folder
- `example-project` -> your real source repository and workspace name

You should rename both when adapting the template. The current names are examples only.

## Repository Layout

```text
.
├── README.md
└── example-company/
    ├── README.md
    ├── agents/
    │   ├── CEO/
    │   ├── FoundingEngineer/
    │   ├── DocumentationEngineer/
    │   ├── UIUXEngineer/
    │   └── QA/
    ├── skills/
    │   ├── example-project/
    │   └── github/
    └── workspaces/
        └── example-project/
```

Each agent home typically contains role instructions, judgment guidance, recurring heartbeat checklists, tool priorities, and optional `memory/` or `life/` folders for persistent context.

This public template keeps the folder structure but does not include real company memory or history.

## Runtime Layout

A typical runtime layout looks like this:

- `/home/agent0/paperclip-agents` -> this company/instruction repo
- `/home/agent0/workspace/example-project/example-project` -> the actual source repository
- `/home/agent0/workspace/example-project/worktrees` -> task-specific git worktrees
- `/home/agent0/workspace/example-project/secrets` -> local-only secrets and config

The exact paths are examples. Adjust them to your own environment if needed.

## How To Use This Template

1. Clone this repo.
2. Rename `example-company` and `example-project` to match your setup.
3. Replace placeholder paths, repository names, and secret/bootstrap instructions.
4. Tune the role prompts to match your team structure and governance.
5. Remove roles you do not need or add new ones with the same home layout.
6. Point the workspace instructions at your real source repo.

## Bootstrap Notes

The checked-in bootstrap files are generic on purpose. They tell readers where company instructions live, where the real project workspace should live, and where local secrets belong, but they do not assume any specific stack or toolchain.

Add project-specific setup only inside your own derived repo.

## Start Reading Here

- [`example-company/README.md`](example-company/README.md) for company bootstrap and folder conventions
- `example-company/agents/<Role>/` for role-specific instructions

## Privacy and Safety

This template intentionally excludes real memory entries, work history, credentials, and project-specific operational details. Treat any secrets, tokens, or local environment files as private and keep them out of git.
