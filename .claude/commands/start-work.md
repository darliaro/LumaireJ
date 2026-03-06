# Start Work on Issue

Create a branch and begin work on a GitHub issue.

## Arguments
- `$ARGUMENTS` - Issue number (REQUIRED, e.g., "42" or "#42")

<validation>
If `$ARGUMENTS` is empty or not a valid issue number:
- Ask the user: "Which issue number should I start work on?"
- Do NOT proceed without a valid issue number.
</validation>

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
   | Issue Title Prefix | Branch Prefix |
   |-------------------|---------------|
   | `[FEAT]` | `feat/` |
   | `[FIX]` | `fix/` |
   | `[REFACTOR]` | `refactor/` |
   | `[ARCH]` | `arch/` |

   If the issue title doesn't match any type, ask the user which prefix to use. Do NOT guess.

4. **Update main and create branch**:
   ```bash
   git checkout main && git pull origin main
   git checkout -b <prefix>/<issue-number>-<short-description>
   ```
   - If `git pull` fails due to merge conflicts, **stop** and inform the user:
     "Merge conflicts on main. Please resolve manually before starting new work."
   - Do NOT force-pull or discard changes.

5. **Confirm** the branch is ready and summarize the issue (title, acceptance criteria, key files).

## Issue Number
$ARGUMENTS
