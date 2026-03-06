# Fix Post-Review Changes

Fetch review feedback, implement fixes, and push updates.

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

2. **Fetch all review feedback** (summary, comments, and inline reviews):
   ```bash
   gh pr view <pr-number>
   gh pr view <pr-number> --comments
   gh pr checks <pr-number>
   ```

3. **Display requested changes** clearly to the user.

4. **Implement fixes**:
   - Analyze the review feedback and make code changes directly.
   - If a feedback item is ambiguous, ask the user before proceeding.

5. **Auto-format and run quality checks** (must match CI):
   ```bash
   pdm run format
   pdm run lint
   pdm run python -m ruff format --check .
   pdm run test
   ```
   - If checks fail, fix before pushing. Do NOT push failing code.

6. **Commit fixes**:
   - Extract issue number from branch name.
   - Determine commit type from branch prefix.
   ```bash
   git add <changed-files>
   git commit -m "[TYPE #issue] Address review feedback

   Co-Authored-By: Claude <noreply@anthropic.com>"
   ```

7. **Push and notify**:
   ```bash
   git push
   gh pr comment <pr-number> --body "Review feedback addressed. Ready for re-review."
   ```

8. **Report**: "Changes pushed. PR updated and ready for re-review."

## PR or Context
$ARGUMENTS
