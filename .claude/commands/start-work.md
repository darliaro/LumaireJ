# Start Work on Issue

Create a branch and begin work on a GitHub issue.

## Arguments
- `$ARGUMENTS` - Issue number (e.g., "42" or "#42")

## Instructions

1. **Fetch issue details**:
   ```bash
   gh issue view <issue-number>
   ```

2. **Determine branch prefix** from issue title:
   | Issue Type | Branch Prefix |
   |------------|---------------|
   | `[FEAT]` | `feat/` |
   | `[FIX]` | `fix/` |
   | `[REFACTOR]` | `refactor/` |
   | `[ARCH]` | `arch/` |

3. **Ensure main is up to date**:
   ```bash
   git checkout main && git pull origin main
   ```

4. **Create and checkout branch**:
   ```bash
   git checkout -b <prefix>/<issue-number>-<short-description>
   ```
   Example: `feat/42-user-authentication`

5. **Remind user** to manually move the issue from 📋 Backlog to 🔄 In Progress on the project board.

6. **Confirm** the branch is ready and summarize the issue.

## Issue Number
$ARGUMENTS
