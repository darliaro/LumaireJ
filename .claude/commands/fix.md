# Fix Post-Review Changes

Handle requested changes after PR review.

## Arguments
- `$ARGUMENTS` - (Optional) PR number or additional context

## Instructions

1. **Determine PR number**:
   - If `$ARGUMENTS` contains a PR number, use it.
   - Otherwise, infer from the current branch:
     ```bash
     gh pr list --head "$(git branch --show-current)" --json number --jq '.[0].number'
     ```
   - If no PR can be found, ask the user for the PR number.

2. **Fetch latest review feedback**:
   ```bash
   gh pr view <pr-number>
   gh pr checks <pr-number>
   ```

3. **Display requested changes** from the review to user clearly.

4. **Implement the fixes**:
   - Analyze the review feedback and identify required code changes
   - Make the code changes directly to address each piece of feedback
   - If a feedback item is ambiguous or requires a design decision, ask the user for clarification before proceeding

5. **Run quality checks**:
   ```bash
   pdm run lint
   pdm run test
   ```
   - If lint fails, run `pdm run format` and re-check. If issues persist, fix them manually.
   - If tests fail, analyze and fix. If failures are unrelated to the review changes, inform the user.
   - Do NOT push if quality checks fail.

6. **Create fix commit**:
   - Extract issue number from branch
   - Determine commit type from branch prefix
   - Create commit with descriptive message:
     ```bash
     git add <changed-files>
     git commit -m "[TYPE #issue] Fix: Address review feedback

     Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"
     ```

7. **Push changes**:
   ```bash
   git push
   ```
   Note: This automatically updates the PR. GitHub automation keeps PR in 🔄 In Progress.

8. **Notify reviewer** (optional):
   ```bash
   gh pr comment <pr-number> --body "Changes addressed and pushed. Ready for re-review."
   ```

9. **Report** to user: "Changes pushed successfully. PR updated and ready for re-review."

## PR or Context
$ARGUMENTS
