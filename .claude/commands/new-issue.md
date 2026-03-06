# Create New GitHub Issue

Create a new GitHub issue following project conventions.

## Arguments
- `$ARGUMENTS` - Issue description or title

<validation>
If `$ARGUMENTS` is empty, ask the user: "What should the issue be about?"
Do NOT proceed without a description.
</validation>

## Instructions

1. **Determine issue type** by analyzing the request:
   | Keyword Pattern | Type |
   |----------------|------|
   | New functionality, add, implement | `[FEAT]` |
   | Bug, broken, error, crash, fix | `[FIX]` |
   | Refactor, clean up, restructure | `[REFACTOR]` |
   | Infrastructure, CI, config, architecture | `[ARCH]` |

   If ambiguous, ask the user which type to use. Do NOT guess.

2. **Select labels** — verify available labels first:
   ```bash
   gh label list --json name --jq '.[].name'
   ```
   Only use labels that appear in the output. Do NOT invent or assume labels exist.

3. **Create the issue**:
   ```bash
   gh issue create --title "[TYPE] Description" \
     --body "issue body" \
     --label "labels" \
     --assignee dariero
   ```

4. **Report** the issue number and URL.

## User Request
$ARGUMENTS
