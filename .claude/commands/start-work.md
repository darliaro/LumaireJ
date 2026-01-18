# Start Work on Issue

Create a branch and begin work on a GitHub issue.

## Arguments
- `$ARGUMENTS` - Issue number (e.g., "42" or "#42")

## Instructions

1. **Fetch issue details**:
   ```bash
   gh issue view <issue-number>
   ```

2. **Determine branch prefix** from issue title:
   | Issue Type | Branch Prefix |
   |------------|---------------|
   | `[FEAT]` | `feat/` |
   | `[FIX]` | `fix/` |
   | `[REFACTOR]` | `refactor/` |
   | `[ARCH]` | `arch/` |

3. **Ensure main is up to date**:
   ```bash
   git checkout main && git pull origin main
   ```

4. **Create and checkout branch**:
   ```bash
   git checkout -b <prefix>/<issue-number>-<short-description>
   ```
   Example: `feat/42-user-authentication`

5. **Move issue to In Progress** on the project board:
   ```bash
   # Get issue node ID
   ISSUE_NODE_ID=$(gh issue view <issue-number> --json id --jq '.id')

   # Get project item ID (add to project if not already there)
   ITEM_ID=$(gh api graphql -f query='
     mutation($project: ID!, $content: ID!) {
       addProjectV2ItemById(input: {projectId: $project, contentId: $content}) {
         item { id }
       }
     }' -f project="PVT_kwHODR8J4s4A9wbx" -f content="$ISSUE_NODE_ID" --jq '.data.addProjectV2ItemById.item.id')

   # Move to In Progress
   gh api graphql -f query='
     mutation($project: ID!, $item: ID!, $field: ID!, $value: String!) {
       updateProjectV2ItemFieldValue(input: {projectId: $project, itemId: $item, fieldId: $field, value: {singleSelectOptionId: $value}}) {
         projectV2Item { id }
       }
     }' -f project="PVT_kwHODR8J4s4A9wbx" -f item="$ITEM_ID" -f field="PVTSSF_lAHODR8J4s4A9wbxzgxXTgM" -f value="47fc9ee4"
   ```

6. **Confirm** the branch is ready, issue moved to 🔄 In Progress, and summarize the issue.

## Issue Number
$ARGUMENTS
