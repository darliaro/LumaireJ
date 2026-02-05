# Create Commit

Create a commit following project conventions.

## Arguments
- `$ARGUMENTS` - (Optional) Commit message or description of changes

## Instructions

1. **Check current status**:
   ```bash
   git status
   git diff --staged
   ```
   - If there are no staged changes AND no unstaged changes, inform the user: "Nothing to commit." and stop.
   - If there are unstaged changes but nothing staged, show the changed files and ask what to stage.

2. **Extract issue number** from current branch name (e.g., `feat/42-description` → `42`):
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

4. **Stage relevant changes** if not already staged:
   ```bash
   git add <files>
   ```

5. **Create commit** with proper format:
   ```bash
   git commit -m "[TYPE #issue] Description

   Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"
   ```

6. **Verify commit** was created successfully:
   ```bash
   git log -1
   ```
   If the commit failed (e.g., pre-commit hook rejection), report the specific error and offer to fix it. Do NOT retry with `--no-verify`.

## Commit Description
$ARGUMENTS
