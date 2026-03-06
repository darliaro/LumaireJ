# Create Commit

Auto-format, validate, and commit changes following project conventions.

## Arguments
- `$ARGUMENTS` - (Optional) Commit message or description of changes

## Instructions

1. **Check current status**:
   ```bash
   git status
   git diff
   ```
   - If there are no changes (staged or unstaged), inform the user: "Nothing to commit." and stop.

2. **Extract issue number** from current branch name (e.g., `feat/42-description` -> `42`):
   - If the branch is `main` or has no issue number, ask the user: "Which issue number is this commit for?"
   - Do NOT create a commit without a valid issue number.

3. **Determine commit type** from branch prefix:
   | Branch Prefix | Commit Type |
   |---------------|-------------|
   | `feat/` | `FEAT` |
   | `fix/` | `FIX` |
   | `refactor/` | `REFACTOR` |
   | `arch/` | `ARCH` |

   If the branch prefix doesn't match any known type, ask the user which commit type to use. Do NOT guess.

4. **Auto-format code**:
   ```bash
   pdm run format
   ```

5. **Run quality checks** (mirrors CI):
   ```bash
   pdm run lint
   pdm run python -m ruff format --check .
   ```
   - If lint fails after formatting, fix the issues manually before proceeding.
   - Do NOT commit if quality checks fail.

6. **Stage changes**:
   ```bash
   git add <relevant-files>
   ```
   Stage all modified/new files that are part of the work. Do NOT stage `.env`, credentials, or unrelated files.

7. **Create commit** with proper format:
   ```bash
   git commit -m "[TYPE #issue] Description

   Co-Authored-By: Claude <noreply@anthropic.com>"
   ```

8. **Verify commit** was created successfully:
   ```bash
   git log -1
   ```
   If the commit failed (e.g., pre-commit hook rejection), report the specific error and offer to fix it. Do NOT retry with `--no-verify`.

## Commit Description
$ARGUMENTS
