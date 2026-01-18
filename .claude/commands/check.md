# Pre-Push Check

Run linting and tests before pushing.

## Arguments
- `$ARGUMENTS` - (Optional) Specific test path or flags

## Instructions

1. **Run linting**:
   ```bash
   pdm run lint
   ```
   If errors found, offer to run `pdm run format` to auto-fix.

2. **Run tests**:
   ```bash
   pdm run test
   ```

3. **Report results**:
   - If all pass: "Ready to push"
   - If failures: List specific issues and offer to fix them

4. **Show git status** for awareness:
   ```bash
   git status
   git diff --stat
   ```

## Test Arguments
$ARGUMENTS
