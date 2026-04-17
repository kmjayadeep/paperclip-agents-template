# AGENTS.md

This repository is a public template for a Paperclip company definition.

It is not an application source repository. It is the operating layer for a role-based agent org: agent prompts, heartbeat routines, memory structure, shared skills, and workspace/bootstrap guidance.

## Template Scope

The checked-in company is intentionally generic:

- `example-company/` is the company root
- `example-company/agents/` contains one home directory per agent role
- `example-company/skills/` contains shared skills used by the company
- `example-company/workspaces/` contains workspace placeholders and secret skeletons

Placeholder names like `example-company` and `example-project` are examples only. Replace them when adapting the template.

## Operating Model

The default model is a small org chart with explicit ownership:

1. CEO receives work, triages it, and assigns an owner.
2. Specialist agents execute in their domain.
3. QA validates the changed surface.
4. The PR owner responds to QA feedback.
5. A human or repo owner merges.

Important properties:

- the CEO defaults to management and delegation, not implementation
- execution agents can use lighter or lower-cost models when appropriate
- role prompts, checklists, and workflows should be refined when repeated mistakes show a system gap
- this structure is meant to create a feedback loop across routing, execution, validation, and instruction updates

## What Belongs In This Repo

Use this repo for:

- company structure
- agent instructions
- role boundaries and governance
- workflow rules and checklists
- workspace/bootstrap scaffolding
- empty memory/life directory structure

Do not treat it as the application repo unless you are changing the company operating system itself.

## Working Rules

- Keep role instructions clear, minimal, and role-specific.
- Preserve the boundary between company instructions and the real product/source repository.
- Do not commit secrets, personal memory, or private operational history.
- If you publish a derived version of this template, replace placeholder names and remove any organization-specific residue.
