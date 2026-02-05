# Start Work on Issue

Create a branch and begin work on a GitHub issue.

## Arguments
- `$ARGUMENTS` - Issue number (REQUIRED, e.g., "42" or "#42")

## Validation
If `$ARGUMENTS` is empty or not a valid issue number:
- Ask the user: "Which issue number should I start work on?"
- Do NOT proceed without a valid issue number.

## Instructions

1. **Pre-flight check** — verify clean working tree:
   ```bash
   git status --porcelain
   ```
   - If there are uncommitted changes, **stop** and ask the user:
     "You have uncommitted changes. Stash them, commit them, or discard before switching branches?"
   - Do NOT proceed until the working tree is clean.

2. **Fetch issue details**:
   ```bash
   gh issue view <issue-number>
   ```
   If the issue doesn't exist or is already closed, inform the user and stop.

3. **Determine branch prefix** from issue title:
   | Issue Type | Branch Prefix |
   |------------|---------------|
   | `[FEAT]` | `feat/` |
   | `[FIX]` | `fix/` |
   | `[REFACTOR]` | `refactor/` |
   | `[ARCH]` | `arch/` |

   If the issue title doesn't match any type, ask the user which prefix to use. Do NOT guess.

4. **Ensure main is up to date**:
   ```bash
   git checkout main && git pull origin main
   ```
   - If `git pull` fails due to merge conflicts, **stop** and inform the user:
     "Merge conflicts on main. Please resolve manually before starting new work."
   - Do NOT force-pull or discard changes.

5. **Create and checkout branch**:
   ```bash
   git checkout -b <prefix>/<issue-number>-<short-description>
   ```
   Example: `feat/42-user-authentication`

6. **Move issue to In Progress** on the project board:
   ```bash
   # Get issue node ID
   ISSUE_NODE_ID=$(gh issue view <issue-number> --json id --jq '.id')

   # Add issue to project (returns item ID even if already added)
   ITEM_ID=$(gh api graphql -f query='
     mutation($project: ID!, $content: ID!) {
       addProjectV2ItemById(input: {projectId: $project, contentId: $content}) {
         item { id }
       }
     }' -f project="PVT_kwHODR8J4s4A9wbx" -f content="$ISSUE_NODE_ID" --jq '.data.addProjectV2ItemById.item.id')

   # Dynamically look up the "Status" field and "In Progress" option
   PROJECT_DATA=$(gh api graphql -f query='
     query($project: ID!) {
       node(id: $project) {
         ... on ProjectV2 {
           field(name: "Status") {
             ... on ProjectV2SingleSelectField {
               id
               options { id name }
             }
           }
         }
       }
     }' -f project="PVT_kwHODR8J4s4A9wbx")

   FIELD_ID=$(echo "$PROJECT_DATA" | jq -r '.data.node.field.id')
   OPTION_ID=$(echo "$PROJECT_DATA" | jq -r '.data.node.field.options[] | select(.name == "In Progress") | .id')

   # Move to In Progress
   gh api graphql -f query='
     mutation($project: ID!, $item: ID!, $field: ID!, $value: String!) {
       updateProjectV2ItemFieldValue(input: {projectId: $project, itemId: $item, fieldId: $field, value: {singleSelectOptionId: $value}}) {
         projectV2Item { id }
       }
     }' -f project="PVT_kwHODR8J4s4A9wbx" -f item="$ITEM_ID" -f field="$FIELD_ID" -f value="$OPTION_ID"
   ```
   Note: The project ID `PVT_kwHODR8J4s4A9wbx` is stable. Field and option IDs are looked up dynamically so the command survives project board reconfiguration.

   If the GraphQL calls fail (e.g., permission error, project not found), warn the user but continue — the branch is still usable. Project board status can be updated manually.

7. **Confirm** the branch is ready, issue moved to 🔄 In Progress, and summarize the issue.

## Issue Number
$ARGUMENTS
