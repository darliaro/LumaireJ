# Complete Issue

Clean up local environment after PR is merged.

## Arguments
- `$ARGUMENTS` - Issue number

## Instructions

1. **Verify PR is merged**:
   ```bash
   gh issue view <issue-number>
   gh pr list --state merged --search "<issue-number>"
   ```
   Note: GitHub automation automatically:
   - Moves PR to 🚀 Deployed when merged
   - Closes the linked issue
   - Moves issue to ✨ Done

2. **Switch to main branch**:
   ```bash
   git checkout main
   ```

3. **Pull latest changes**:
   ```bash
   git pull origin main
   ```

4. **Delete local feature branch**:
   ```bash
   git branch -d <branch-name>
   ```

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
