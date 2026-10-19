# Git Conventions Protocol

> Universal git workflow, commit conventions, and branching strategies for AI-assisted development.

**Applies to:** All projects using Git
**Last Updated:** 2026-08-10
**Version:** 1.3

---

## Table of Contents

- [When to put something under git](#when-to-put-something-under-git)
- [Commit Messages](#commit-messages)
- [Branching Strategy](#branching-strategy)
- [Pull Request Workflow](#pull-request-workflow)
- [Git Configuration](#git-configuration)
- [Common Operations](#common-operations)
- [MCP Integration](#mcp-integration)
- [Security Rules](#security-rules)

---

## When to put something under git

**Default: yes, as a local repo.** `git init` plus a `.gitignore` is a one-time cost; diff, blame and rollback are worth more than that on anything hand-authored. Remote is a **separate, later** decision — the absence of a good reason to *push* is not a reason to skip git entirely. That conflation is the usual way content ends up unversioned.

This applies well beyond code: instruction layers, ops workspaces, config directories and curated notes all qualify. Each has a failure mode — a silent edit, a stale fact, an accidental overwrite — that a diff catches and nothing else does.

**The one real reason not to: something else already versions the same content.** Two histories over one set of files is worse than none — you get ambiguity about which is authoritative and no reliable answer to "what changed, when, by whom". Worked example: the ERS Brain retired git on 2026-06-29 in favour of an append-only hosted revision store already providing history, actor attribution and recovery; `01_ers-brain/AGENTS.md` now explicitly forbids re-introducing a git workflow there.

**Three conditions on the default — not exceptions to it:**

- **Whitelist the `.gitignore` wherever runtime state dominates.** `*` first, then explicit `!` re-admits. A blacklist silently begins tracking whatever the next release of a tool drops into the directory. Verify with `git add -A --dry-run` and *read the list* before the first commit. Worked example: `~/.claude` wraps ~1.7 GB of session transcripts around a handful of config files; a whitelist stages only the config and the curated memory files, in tens of milliseconds.
- **Local git is not backup.** It buys diff, blame, rollback, audit. Disaster recovery is a separate mechanism — Time Machine, a hosted store, or a remote — and should be named explicitly rather than assumed.
- **No value over binary or database content.** Keychains, sqlite, leveldb, media: no meaningful diff and the repo bloats.

Cloud-synced working trees are **not** an exception — see [Cloud-synced working trees](#cloud-synced-working-trees-onedrive--dropbox--sharepoint) for the two one-time disciplines that make them safe.

### Remote is a separate decision

Gate it on two questions; both must be yes.

1. **Is the content safe to host?** Identifying personal content, employer context, account structure and preferences argue for local-only, even on a private remote.
2. **Is there a real cross-machine or collaboration need?** Single-machine, single-user content does not acquire one merely by being in git.

Deliberate no's in practice: `claude-ops` and `~/.claude` are both git-backed locally with **no remote**. When you decline a remote, **record that decision in the repo** (a `README` section is enough) — otherwise a future session reads the missing remote as an oversight and "fixes" it.

---

## Commit Messages

### Format

```
type(scope): description

[optional body]

[optional footer]
Co-Authored-By: Claude <noreply@anthropic.com>
```

### Types

| Type | Use For |
|------|---------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `style` | Formatting, no code change |
| `refactor` | Code restructuring |
| `test` | Adding/updating tests |
| `chore` | Build, dependencies, tooling |
| `perf` | Performance improvements |

### Scope Examples

| Scope | Meaning |
|-------|---------|
| `api` | API routes/endpoints |
| `db` | Database changes |
| `ui` | User interface |
| `auth` | Authentication |
| `edge` | Edge Functions |
| `lambda` | AWS Lambda |

### Examples

```bash
# Feature
feat(api): add user preferences endpoint

# Bug fix
fix(auth): resolve session expiration race condition

# Documentation
docs(readme): update installation instructions

# Database
feat(db): add analytics table with RLS policies

# Edge Function
feat(edge): add TTS generation function
```

### Commit Message Rules

1. **Imperative mood**: "add feature" not "added feature"
2. **No period** at end of subject line
3. **Max 72 characters** for subject line
4. **Blank line** between subject and body
5. **Body explains "why"**, not "what" (code shows what)

---

## Branching Strategy

### Main Branches

| Branch | Purpose | Deploys To |
|--------|---------|------------|
| `main` | Production code | Production |
| `develop` | Integration branch (optional) | Staging |

### Feature Branches

```bash
# Create feature branch
git checkout -b feat/user-preferences

# Create fix branch
git checkout -b fix/login-redirect

# Create refactor branch
git checkout -b refactor/api-structure
```

### Branch Naming

```
type/description-in-kebab-case

# Examples
feat/add-dark-mode
fix/memory-leak-in-player
refactor/extract-auth-service
docs/update-api-reference
```

---

## Pull Request Workflow

### Creating a PR

```bash
# 1. Ensure branch is up to date
git fetch origin
git rebase origin/main

# 2. Push branch
git push -u origin feat/my-feature

# 3. Create PR via GitHub CLI
gh pr create --title "feat: add my feature" --body "## Summary
- Added X
- Fixed Y

## Test Plan
- [ ] Test A
- [ ] Test B"
```

### PR Title Format

Same as commit message format:
```
type(scope): description
```

### PR Body Template

```markdown
## Summary
Brief description of changes

## Changes
- Change 1
- Change 2

## Test Plan
- [ ] Manual testing step 1
- [ ] Manual testing step 2

## Screenshots (if UI changes)
[Add screenshots here]
```

### Review Process

1. **Self-review**: Check diff before requesting review
2. **CI passes**: All checks must pass
3. **Reviewer approval**: At least one approval required
4. **Squash merge**: Keep history clean

---

## Git Configuration

### Required Setup

```bash
# Set identity (use for all projects)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Per-project override (if needed)
git config user.name "Project Name"
git config user.email "project@example.com"
```

### Recommended Settings

```bash
# Default branch name
git config --global init.defaultBranch main

# Rebase on pull (cleaner history)
git config --global pull.rebase true

# Auto-prune on fetch
git config --global fetch.prune true

# Better diff algorithm
git config --global diff.algorithm histogram
```

---

## Cloud-synced working trees (OneDrive / Dropbox / SharePoint)

Git repos are increasingly checked out inside a cloud-synced folder. Git works there, but on-demand sync (Files-On-Demand and equivalents) is hostile to `.git` internals. Set two disciplines once, then forget:

- **Set the repo folder to "always keep on this device."** On-demand sync dehydrates `.git` objects into cloud placeholders; git then can't read them and the working copy corrupts. Pinning the folder fully on-device removes the root cause — a one-time, per-machine setting. **With it set, routine git operations (commit, push, pull, stage, branch) run normally with sync on; no pausing.**
- **Never bulk-move a live working tree through the sync client mid-sync.** Relocating a repo? Re-clone at the destination and remove the old copy rather than moving the live tree — a folder move races the sync and corrupts `.git`. Do structural folder ops through the provider's own tooling where possible, never through a tool blind to `.git`.

The committed history is always safe on the remote; this is about not corrupting the *local* working copy. (An ERS deployment adds a service-specific version — OneDrive/SharePoint + the M365 MCP — in its protocol mirror.)

## Common Operations

### Daily Workflow

```bash
# Start of day: update main
git checkout main
git pull origin main

# Create feature branch
git checkout -b feat/my-feature

# Work on feature...
git add specific-file.ts
git commit -m "feat: add initial implementation"

# Push and create PR
git push -u origin feat/my-feature
gh pr create
```

### Updating Feature Branch

```bash
# Fetch latest main
git fetch origin main

# Rebase onto main (preferred)
git rebase origin/main

# Or merge main into feature branch
git merge origin/main
```

### Fixing Commits

```bash
# Amend last commit (before push)
git commit --amend -m "corrected message"

# Interactive rebase (before push, use carefully)
git rebase -i HEAD~3

# Add forgotten file to last commit
git add forgotten-file.ts
git commit --amend --no-edit
```

### Undoing Changes

```bash
# Discard uncommitted changes to a file
git checkout -- path/to/file

# Unstage a file
git reset HEAD path/to/file

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes) - DANGEROUS
git reset --hard HEAD~1
```

---

## MCP Integration

### GitHub MCP Server

When using Claude Code with the GitHub MCP server, these operations are handled by MCP tools:

| Operation | MCP Tool | Local Git |
|-----------|----------|-----------|
| Create PR | `mcp__github__create_pull_request` | `gh pr create` |
| List PRs | `mcp__github__list_pull_requests` | `gh pr list` |
| Get PR diff | `mcp__github__pull_request_read` | `gh pr diff` |
| Create branch | `mcp__github__create_branch` | `git checkout -b` |
| Push files | `mcp__github__push_files` | `git push` |

### When to Use Which

| Use MCP | Use Local Git |
|---------|---------------|
| Creating PRs | Local commits |
| Reviewing PRs | Branch switching |
| GitHub API operations | Rebasing |
| Cross-repo operations | Amending commits |

### Local Operations Still Required

MCP handles GitHub remote operations, but local git commands are still needed for:

- `git add` - Staging files
- `git commit` - Creating commits
- `git checkout` - Switching branches locally
- `git rebase` - Rewriting history
- `git stash` - Temporary storage

---

## Security Rules

### Never Commit

- `.env` files with real secrets
- API keys or tokens
- Database credentials
- Private keys
- `node_modules/` (use .gitignore)

### Safe Practices

```bash
# Use specific file adds, not blanket add
git add specific-file.ts  # ✅ Good
git add .                 # ❌ Risky
git add -A                # ❌ Risky

# Check what you're committing
git diff --staged         # Review before commit

# Use .gitignore
echo ".env" >> .gitignore
echo "*.pem" >> .gitignore
```

### Runtime State and Daemons

Before enabling a local daemon, sync agent, OAuth smoke flow, desktop launcher, or any other process that writes inside the repo, add its runtime directory/files to `.gitignore`.

Common examples:

- OAuth token caches and refresh-token files
- daemon logs, pid files, lock files, and health files
- generated local latency snapshots or telemetry caches
- sync cursors, local mirrors, and machine-specific state
- smoke/canary artifacts created only to exercise a hosted or local service

If a runtime state file is already tracked, do **not** delete the local file to make git clean. Stop tracking it while preserving the local state:

```bash
git rm --cached path/to/runtime-state.json
```

Then add the containing runtime directory or exact generated files to `.gitignore`, verify with `git check-ignore -v`, and commit the ignore/update separately from unrelated product changes.

### If Secrets Are Committed

1. **Immediately rotate the secret** (most important)
2. Remove from history (optional, complex):
   ```bash
   git filter-branch --force --index-filter \
     "git rm --cached --ignore-unmatch path/to/secret" \
     --prune-empty --tag-name-filter cat -- --all
   ```
3. Force push (coordinate with team)
4. Contact GitHub to clear caches

---

## Deployment Integration

### Auto-Deploy Triggers

| Platform | Trigger | Branch |
|----------|---------|--------|
| Vercel | Push to main | `main` |
| Render | Push to main | `main` |
| Replit | Auto-sync | `main` |
| Supabase | GitHub integration | `main` |

### Pre-Push Checklist

- [ ] All tests pass locally
- [ ] No console.logs or debug code
- [ ] No hardcoded secrets
- [ ] Commit message follows convention
- [ ] PR description is complete

---

## Quick Reference

```bash
# Status
git status
git log --oneline -10

# Branching
git checkout -b feat/name    # Create branch
git checkout main            # Switch to main
git branch -d feat/name      # Delete local branch

# Committing
git add file.ts              # Stage file
git commit -m "type: msg"    # Commit
git commit --amend           # Fix last commit

# Syncing
git fetch origin             # Get remote changes
git pull --rebase            # Update with rebase
git push origin branch       # Push branch

# PRs (GitHub CLI)
gh pr create                 # Create PR
gh pr list                   # List PRs
gh pr merge                  # Merge PR
```

---

**Protocol Version**: 1.2
**Last Updated**: 2026-06-22
**Sources**: Fizbit-dm, statarb-platform, TeachMeIn5-FullApp; brain-mcp-server / ai-brain-jem hosted Brain runtime-state hygiene fix 2026-06-22
