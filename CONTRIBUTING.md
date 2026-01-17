# Contributing to LumaireJ

## Issue Workflow

### Creating Issues for Fixes and Improvements

**Rule**: Every fix, improvement, or new feature MUST start with a GitHub issue on the project board before any code changes.

### Required Steps

1. **Create the Issue**
   - Use the appropriate template from `.github/ISSUE_TEMPLATE/`:
     - `bug_report.md` - For defects and errors
     - `feature_request.md` - For new functionality
     - `refactor.md` - For code improvements without behavior changes
     - `architecture_task.md` - For infrastructure/architectural changes
   - Follow the template structure completely

2. **Fill Out Required Fields**

   | Field | Value | Notes |
   |-------|-------|-------|
   | **Assignees** | `darliaro` | Always assign to project owner |
   | **Labels** | Select appropriate | See [Labels](#labels) section |
   | **Projects** | LumaireJ Board | Status: `Backlog` |
   | **Priority** | Critical/High/Medium/Low | Based on impact |
   | **Size** | XS/S/M/L/XL | Based on effort |

3. **Add to Project Board**
   ```bash
   gh project item-add 1 --owner darliaro --url <issue-url>
   ```

4. **Set Project Fields**
   - Status: `Backlog` (initial state)
   - Priority: Based on urgency and impact
   - Size: Based on estimated effort

### Labels

| Label | Use For |
|-------|---------|
| `bug` | Defects, errors, unexpected behavior |
| `feature` | New functionality |
| `improvement` | Enhancements to existing behavior |
| `refactor` | Code restructure without behavior change |
| `BACKEND` | API, database, services |
| `FRONTEND` | UI, views, interactions |
| `CONFIG` | Environment, settings |
| `TEST` | Test coverage, frameworks |
| `DB` | Schema, migrations |
| `DEVOPS` | CI/CD, deployment |

### Priority Guidelines

| Priority | When to Use |
|----------|-------------|
| **Critical** | Production is broken, security vulnerability |
| **High** | Core feature broken, blocks other work |
| **Medium** | Important improvement, non-blocking bug |
| **Low** | Nice to have, tech debt, minor enhancement |

### Size Guidelines

| Size | Description | Example |
|------|-------------|---------|
| **XS** | < 1 hour, single file, trivial change | Fix typo, add constant |
| **S** | 1-2 hours, 1-3 files, simple change | Add config option, small refactor |
| **M** | Half day, multiple files, moderate complexity | New endpoint, component update |
| **L** | Full day, significant changes | New feature, major refactor |
| **XL** | Multiple days, architectural impact | New system, migration |

### Board Columns

| Column | Meaning |
|--------|---------|
| `Backlog` | Accepted, waiting to be picked up |
| `To Do` | Planned for current sprint/cycle |
| `In Progress` | Actively being worked on |
| `Ready for Test` | Code complete, awaiting QA |
| `QA` | Being tested |
| `Done` | Verified and complete |
| `Close` | Closed (won't do, duplicate, etc.) |

## Development Workflow

### Starting Work on an Issue

1. **Pick an issue** from `Backlog` or `To Do` column
2. **Move to `In Progress`** on the project board (BEFORE creating branch)
3. **Create a branch** using type-prefixed naming:
   ```bash
   git checkout -b <type>/<issue-number>-<short-description>
   ```

### Branch Naming Convention

| Issue Type | Branch Prefix | Example |
|------------|---------------|---------|
| `[ARCH]` | `arch/` | `arch/51-cors-config-extraction` |
| `[REFACTOR]` | `refactor/` | `refactor/52-validation-constants` |
| `[FEAT]` | `feat/` | `feat/36-landing-page` |
| `[FIX]` / Bug | `fix/` | `fix/42-login-error` |

### Implementation Steps

4. **Make changes** following project conventions
5. **Run linter**: `pdm run lint`
6. **Run tests**: `pdm run pytest -sv tests/`
7. **Commit** with format: `[TYPE #issue] Description`
   ```bash
   git commit -m "[ARCH #51] Extract CORS config to Settings"
   ```
8. **Push and create PR** referencing the issue
9. **Move issue to `Ready for Test`** after PR is ready

## Code Style

- Use `ruff` for linting and formatting
- Run `pdm run format` before committing
- Follow existing patterns in the codebase
- Keep functions small and focused
- Add tests for new functionality

## Commit Messages

Follow conventional commits:
- `feat:` - New feature
- `fix:` - Bug fix
- `refactor:` - Code change without behavior change
- `docs:` - Documentation only
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks
