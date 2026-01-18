# Fix Post-Review Changes

Handle requested changes after PR review.

## Arguments
- `$ARGUMENTS` - (Optional) PR number or additional context

## Instructions

1. **Fetch latest review feedback**:
   ```bash
   gh pr view <pr-number>
   gh pr checks <pr-number>
   ```

2. **Display requested changes** from the review to user clearly.

3. **Guide through fix workflow**:
   - Instruct user: "Make the necessary code changes to address the feedback"
   - Wait for user confirmation that changes are made

4. **Run quality checks**:
   ```bash
   pdm run lint
   pdm run test
   ```
   If errors found, offer to run `pdm run format` to auto-fix linting issues.

5. **Create fix commit**:
   - Extract issue number from branch
   - Determine commit type from branch prefix
   - Create commit with descriptive message:
     ```bash
     git add <changed-files>
     git commit -m "[TYPE #issue] Fix: Address review feedback

     Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"
     ```

6. **Push changes**:
   ```bash
   git push
   ```
   Note: This automatically updates the PR. GitHub automation keeps PR in 🔄 In Progress.

7. **Notify reviewer** (optional):
   ```bash
   gh pr comment <pr-number> --body "Changes addressed and pushed. Ready for re-review."
   ```

8. **Report** to user: "Changes pushed successfully. PR updated and ready for re-review."

## PR or Context
$ARGUMENTS
