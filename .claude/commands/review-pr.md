# Review & Merge Pull Request

Check CI, review changes, merge, and clean up. Designed for solo-developer workflow.

## Arguments
- `$ARGUMENTS` - PR number (optional -- inferred from current branch if omitted)

<validation>
If `$ARGUMENTS` is empty:
1. Infer PR from the current branch:
   ```bash
   gh pr list --head "$(git branch --show-current)" --json number --jq '.[0].number'
   ```
2. If no PR found, ask the user: "Which PR number should I review?"
</validation>

## Instructions

1. **Fetch PR details**:
   ```bash
   gh pr view <pr-number>
   gh pr diff <pr-number>
   ```

2. **Check CI status**:
   ```bash
   gh pr checks <pr-number>
   ```
   - If checks are still running, wait: `gh pr checks <pr-number> --watch`
   - If checks failed, report the failures and guide user to `/fix`. Do NOT merge.

3. **Quick review** -- verify:
   - [ ] No secrets or credentials exposed
   - [ ] No obvious security issues
   - [ ] Changes match the linked issue requirements

4. **Present findings** and ask: "PR #X passes all checks. Merge?"

   **Do NOT merge without the user's explicit confirmation.**

5. **On confirmation -- merge**:
   ```bash
   gh pr merge <pr-number> --squash --delete-branch
   ```
   If merge is blocked by branch protection while checks are green, inform the user and suggest `--admin`.

6. **Close the linked issue** (squash merges may not trigger auto-close):
   Extract issue number from the PR branch name or body, then:
   ```bash
   gh issue close <issue-number>
   ```

7. **Local cleanup**:
   ```bash
   git checkout main
   git pull origin main
   git branch -d <branch-name> 2>/dev/null || true
   git remote prune origin
   ```

8. **Confirm**: "Merged, issue closed, cleaned up. Ready for next issue."

## PR Number
$ARGUMENTS
