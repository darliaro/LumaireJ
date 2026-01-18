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

2. **Extract issue number** from current branch name (e.g., `feat/42-description` → `42`)

3. **Determine commit type** from branch prefix:
   | Branch Prefix | Commit Type |
   |---------------|-------------|
   | `feat/` | `FEAT` |
   | `fix/` | `FIX` |
   | `refactor/` | `REFACTOR` |
   | `arch/` | `ARCH` |

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

## Commit Description
$ARGUMENTS
