# Hotfix

Emergency fix path: creates an issue and branch in one step. Skips backlog — straight to coding.

## Arguments
- `$ARGUMENTS` - Description of the fix (REQUIRED)

<validation>
If `$ARGUMENTS` is empty, ask the user: "What needs to be fixed?"
Do NOT proceed without a description.
</validation>

## Instructions

1. **Pre-flight check** -- verify clean working tree:
   ```bash
   git status --porcelain
   ```
   - If there are uncommitted changes, **stop** and ask the user:
     "You have uncommitted changes. Stash them, commit them, or discard before switching branches?"

2. **Verify labels and create the issue**:
   ```bash
   gh label list --json name --jq '.[].name'
   ```
   Only use labels confirmed to exist. Then:
   ```bash
   gh issue create --title "[FIX] <description>" \
     --body "## Hotfix

   Created via /hotfix command.

   ## Description
   <description>" \
     --label "<verified-labels>" \
     --assignee dariero
   ```
   Extract the issue number from the output.

3. **Update main and create branch**:
   ```bash
   git checkout main && git pull origin main
   git checkout -b fix/<issue-number>-<short-description>
   ```

4. **Confirm**: "Hotfix branch ready for issue #N. Make your fix, then `/commit` and `/pr`."

## Fix Description
$ARGUMENTS
