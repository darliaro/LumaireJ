# Create Pull Request

Run full quality checks, push, and create a pull request.

## Arguments
- `$ARGUMENTS` - (Optional) Additional context for PR description

## Instructions

1. **Full quality checks** (must match CI exactly):
   ```bash
   pdm run format
   pdm run lint
   pdm run python -m ruff format --check .
   pdm run test
   ```
   - If lint fails after formatting, fix manually.
   - If tests fail, analyze and fix before proceeding.
   - If failures cannot be resolved, **stop** and report. Do NOT create a PR with failing checks.
   - If formatting changed any files, stage and commit them before proceeding.

2. **Validate branch state**:
   ```bash
   git branch --show-current
   git log main..HEAD --oneline
   git diff main...HEAD --stat
   ```
   - If on `main`, **stop**: "You are on main. Create a feature branch first using `/start-work`."
   - If there are no commits ahead of main, **stop**: "No changes to create a PR for."

3. **Extract issue number** from branch name (e.g., `feat/42-description` -> `42`).
   If no issue number can be extracted, ask the user.

4. **Determine PR type** from branch prefix:
   | Branch Prefix | PR Type |
   |---------------|---------|
   | `feat/` | `FEAT` |
   | `fix/` | `FIX` |
   | `refactor/` | `REFACTOR` |
   | `arch/` | `ARCH` |

   If the branch prefix doesn't match, ask the user which type to use.

5. **Push branch**:
   ```bash
   git push -u origin <branch-name>
   ```

6. **Create PR**:
   ```bash
   gh pr create --title "[TYPE #issue] Description" \
     --body "## Summary
   - Change 1
   - Change 2

   ## Test Plan
   - [ ] Tests pass locally
   - [ ] Manual testing completed

   Closes #<issue-number>" \
     --assignee dariero \
     --reviewer dariero \
     --label "labels"
   ```

7. **Report PR URL** to user.

## Additional Context
$ARGUMENTS
