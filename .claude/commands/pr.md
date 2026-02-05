# Create Pull Request

Create a pull request following project conventions.

## Arguments
- `$ARGUMENTS` - (Optional) Additional context for PR description

## Instructions

1. **Ensure code quality** before creating PR:
   ```bash
   pdm run lint
   pdm run test
   ```
   - If lint fails, run `pdm run format` and re-check. If issues persist after formatting, fix them manually.
   - If tests fail, analyze and fix the failures before proceeding.
   - If failures cannot be resolved, **stop** and report the specific errors to the user. Do NOT create a PR with failing checks.

2. **Get branch and issue info**:
   ```bash
   git branch --show-current
   git log main..HEAD --oneline
   git diff main...HEAD --stat
   ```
   - If on `main`, **stop**: "You are on main. Create a feature branch first using `/start-work`."
   - If there are no commits ahead of main, **stop**: "No changes to create a PR for."

3. **Extract issue number** from branch name (e.g., `feat/42-description` → `42`):
   - If no issue number can be extracted, ask the user which issue this PR addresses.

4. **Determine PR type** from branch prefix:
   | Branch Prefix | PR Type |
   |---------------|---------|
   | `feat/` | `FEAT` |
   | `fix/` | `FIX` |
   | `refactor/` | `REFACTOR` |
   | `arch/` | `ARCH` |

   If the branch prefix doesn't match, ask the user which type to use.

5. **Push branch** if not already pushed:
   ```bash
   git push -u origin <branch-name>
   ```

6. **Create PR** with proper format:
   ```bash
   gh pr create --title "[TYPE #issue] Description" \
     --body "## Summary
   - Key change 1
   - Key change 2

   ## Test Plan
   - [ ] Tests pass locally
   - [ ] Manual testing completed

   Closes #<issue-number>" \
     --assignee darliaro \
     --reviewer darliaro \
     --label "labels"
   ```
   Note: GitHub automation will automatically move the PR to 🤖 AI Review column.

7. **Report PR URL** to user.

## Additional Context
$ARGUMENTS
