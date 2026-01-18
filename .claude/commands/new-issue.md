# Create New GitHub Issue

Create a new GitHub issue following project conventions.

## Arguments
- `$ARGUMENTS` - Issue description or title

## Instructions

1. **Determine issue type** by analyzing the request:
   - `[FEAT]` - New functionality
   - `[FIX]` - Bug or defect
   - `[REFACTOR]` - Code improvement (no behavior change)
   - `[ARCH]` - Infrastructure/architecture changes

2. **Select appropriate labels** from:
   - Type: `bug`, `feature`, `improvement`, `refactor`
   - Area: `BACKEND`, `FRONTEND`, `CONFIG`, `TEST`, `DB`, `DEVOPS`
   - Priority: `Critical`, `High`, `Medium`, `Low`
   - Size: `XS`, `S`, `M`, `L`, `XL`

3. **Create the issue** with proper formatting:
   ```bash
   gh issue create --title "[TYPE] Description" \
     --body "Description and acceptance criteria" \
     --label "labels" \
     --assignee darliaro
   ```
   Note: GitHub automation will automatically add the issue to the 📋 Backlog column.

4. **Report the issue number and URL** to the user.

## User Request
$ARGUMENTS
