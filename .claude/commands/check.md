# Pre-Push Check

Run linting and tests before pushing.

## Arguments
- `$ARGUMENTS` - (Optional) Specific test path or flags

## Instructions

1. **Run linting**:
   ```bash
   pdm run lint
   ```
   - If errors found, run `pdm run format` to auto-fix.
   - Re-run `pdm run lint` to verify. If issues persist after formatting, list them and fix manually.

2. **Run tests**:
   ```bash
   pdm run test
   ```

3. **Report results**:
   - If all pass: "Ready to push."
   - If lint failures remain after auto-fix: list the specific issues and offer to fix them.
   - If test failures: list the failing tests with error output and offer to investigate.
   - Do NOT report "ready to push" if any check is failing.

4. **Show git status** for awareness:
   ```bash
   git status
   git diff --stat
   ```

## Test Arguments
$ARGUMENTS
