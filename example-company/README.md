# example-company

This folder is an example Paperclip company.

It is a template company, not a real one. Replace `example-company` with your own org name, and replace `example-project` with the real project this company should operate on.

## Contents

- `agents/` -> agent homes and role instructions
- `skills/` -> shared skills for this company
- `workspaces/` -> workspace skeletons and local secret placeholders
- `.gitignore` -> ignores local-only secret files in the example workspace

## Intended Runtime Layout

A typical deployment shape is:

- `/home/agent0/paperclip-agents/example-company` -> this company folder
- `/home/agent0/workspace/example-project/example-project` -> the actual source repository
- `/home/agent0/workspace/example-project/worktrees` -> task-specific worktrees
- `/home/agent0/workspace/example-project/secrets` -> local-only secrets/config

These paths are examples only.

## Bootstrap

To adapt this template:

1. Copy the company folder into your Paperclip agent repo.
2. Create the matching project workspace separately.
3. Add your own local secret files under `workspaces/example-project/secrets/`.
4. Update any role prompts, skills, or workspace conventions that depend on your stack.
5. Clear or leave empty all `memory/` and `life/` folders until your own agents start using them.

## Notes

This template intentionally avoids stack-specific instructions. Add project-specific setup only in your derived version rather than in the public base template.
