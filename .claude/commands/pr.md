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
   Fix any issues before proceeding.

2. **Get branch and issue info**:
   ```bash
   git branch --show-current
   git log main..HEAD --oneline
   git diff main...HEAD --stat
   ```

3. **Extract issue number** from branch name (e.g., `feat/42-description` → `42`)

4. **Determine PR type** from branch prefix:
   | Branch Prefix | PR Type |
   |---------------|---------|
   | `feat/` | `FEAT` |
   | `fix/` | `FIX` |
   | `refactor/` | `REFACTOR` |
   | `arch/` | `ARCH` |

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
