# Complete Issue

Clean up local environment after PR is merged.

## Arguments
- `$ARGUMENTS` - Issue number (REQUIRED)

## Validation
If `$ARGUMENTS` is empty or not a valid issue number:
1. Check the current branch name for an issue number (e.g., `feat/42-desc` → `42`)
2. If no issue number can be inferred, ask the user: "Which issue number should I complete?"
3. Do NOT proceed without a valid issue number.

## Instructions

1. **Verify PR is merged**:
   ```bash
   gh issue view <issue-number>
   gh pr list --state merged --search "<issue-number>"
   ```
   - If the PR is NOT merged, **stop** and inform the user:
     "PR for issue #X is not merged yet. Complete the review/merge process first."
   - Do NOT proceed with cleanup if the PR is still open.

   Note: GitHub automation automatically:
   - Moves PR to 🚀 Deployed when merged
   - Closes the linked issue
   - Moves issue to ✨ Done

2. **Switch to main branch**:
   ```bash
   git checkout main
   ```
   If checkout fails due to uncommitted changes, inform the user and stop.

3. **Pull latest changes**:
   ```bash
   git pull origin main
   ```

4. **Delete local feature branch**:
   ```bash
   git branch -d <branch-name>
   ```
   - If the branch doesn't exist locally, skip this step (it may have already been deleted).
   - If `-d` fails because the branch is not fully merged, warn the user and ask before using `-D`.

5. **Verify remote branch is deleted** (should be auto-deleted by merge):
   ```bash
   git remote prune origin
   ```

6. **Confirm cleanup complete** and report:
   - Local branch deleted
   - Main branch updated
   - Ready to start next issue

## Issue Number
$ARGUMENTS
