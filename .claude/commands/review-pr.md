# Review Pull Request

Review a pull request following project conventions.

## Arguments
- `$ARGUMENTS` - PR number or URL

## Instructions

1. **Fetch PR details**:
   ```bash
   gh pr view <pr-number>
   gh pr diff <pr-number>
   gh pr checks <pr-number>
   ```

2. **Review checklist** (from CLAUDE.md):
   - [ ] Code follows project conventions
   - [ ] No security vulnerabilities (OWASP top 10)
   - [ ] No secrets or credentials exposed
   - [ ] Linting passes
   - [ ] Tests pass
   - [ ] Changes match issue requirements

3. **Check related issue**:
   ```bash
   gh issue view <linked-issue-number>
   ```

4. **Analyze the changes**:
   - Read modified files
   - Check for code quality issues
   - Verify tests cover new functionality
   - Look for potential bugs

5. **Make decision** based on review:

   **If APPROVED:**
   - Submit approval:
     ```bash
     gh pr review <pr-number> --approve --body "LGTM - changes look good"
     ```
   - Auto-merge the PR:
     ```bash
     gh pr merge <pr-number> --squash --delete-branch
     ```
     Note: GitHub automation will move PR to ✅ Approved → 🚀 Deployed
   - Automatically trigger cleanup by running `/complete-issue <issue-number>`

   **If CHANGES NEEDED:**
   - Submit review with specific feedback:
     ```bash
     gh pr review <pr-number> --request-changes --body "Please address:
     - Issue 1
     - Issue 2"
     ```
     Note: GitHub automation will move PR to 🔄 In Progress
   - Guide user to use `/fix` command to address the requested changes

## PR to Review
$ARGUMENTS
