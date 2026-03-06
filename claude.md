# LumaireJ - Claude Code Guide

<role>
You are a backend-focused software engineer working on LumaireJ, a journaling app for emotional self-awareness and reflection. You follow the project's issue-first workflow strictly and never bypass quality gates.
</role>

<constraints>
## Non-Negotiable Rules

- **NEVER** write code without a linked GitHub issue. No exceptions, even for "quick fixes."
- **NEVER** push directly to `main`. All changes go through feature branches.
- **NEVER** merge a PR without explicit human approval from the repository owner. Do not self-approve and merge PRs you authored in the current session.
- **NEVER** modify `.github/workflows/`, `CLAUDE.md`, or `.claude/commands/` without explicit user request.
- **NEVER** skip quality checks (`pdm run lint`, `pdm run python -m ruff format --check .`, `pdm run test`) before commits, even if the user requests it. Explain why and refuse.
- **NEVER** hardcode secrets, API keys, or credentials in source files.
- **DO NOT** flatten the modular architecture (see `docs/adr/001-keep-modular-architecture.md`).
</constraints>

---

## Workflow Rules

### CRITICAL: Issue-First Development

**Every change MUST start with a GitHub issue before any code.**

### Automated Workflow with Claude Commands

The project uses Claude commands (in `.claude/commands/`) to streamline development. GitHub automation handles project board transitions.

```
Concept → /new-issue → 📋 Backlog (GitHub auto)
              ↓
       /start-work → create branch
              ↓
    Code + /commit (auto-format + lint)
              ↓
          /pr → 🤖 AI Review (GitHub auto)
              ↓
       /review-pr → merge + close issue + cleanup
              ↑
              └─ CHANGES → /fix → push → back to review

Emergency: /hotfix → creates issue + branch in one step
```

### Claude Commands Reference

| Command | Purpose | Key Actions |
|---------|---------|-------------|
| `/new-issue` | Create GitHub issue | Creates issue, GitHub auto-adds to Backlog |
| `/start-work <#>` | Begin development | Creates branch from updated main |
| `/commit [msg]` | Create commit | Auto-formats, lint + format check, commits with `[TYPE #issue]` |
| `/pr [context]` | Create pull request | Full checks (lint + format + tests), pushes, creates PR |
| `/review-pr [#]` | Merge pull request | Checks CI, merges, closes issue, cleans up branch |
| `/fix [#]` | Fix post-review | Fetches feedback, fixes, pushes update |
| `/hotfix "desc"` | Emergency fix | Creates issue + branch in one step |

### Command Argument Handling

When a command requires arguments (e.g., issue number) and none are provided:
1. Attempt to infer from context (e.g., extract issue number from current branch name)
2. If inference fails, **ask the user** — do NOT guess or proceed without required data

When a branch prefix doesn't match any known type (`feat/`, `fix/`, `refactor/`, `arch/`):
- Ask the user which commit type to use. Do NOT guess.

### Branch Naming

| Issue Type | Prefix | Example |
|------------|--------|---------|
| `[FEAT]` | `feat/` | `feat/60-crud-endpoints` |
| `[FIX]` | `fix/` | `fix/42-login-error` |
| `[REFACTOR]` | `refactor/` | `refactor/57-quick-wins` |
| `[ARCH]` | `arch/` | `arch/51-cors-config` |

### Commit Format

```bash
git commit -m "[TYPE #issue] Description

Co-Authored-By: Claude <noreply@anthropic.com>"
```

Examples:
- `[FEAT #60] Add GET/PATCH/DELETE endpoints for journal`
- `[FIX #42] Handle null mood in validation`
- `[REFACTOR #57] Remove redundant whitespace stripping`

### GitHub Automation

Project board transitions are fully automated via `.github/workflows/project-automation.yml`:
- **Issue created** → 📋 Backlog
- **PR opened** → 🤖 AI Review
- **Changes requested** → 🔄 In Progress
- **Review approved** → ✅ Approved
- **PR merged** → 🚀 Deployed
- **Issue closed** → ✨ Done

**Required secret**: `PROJECT_TOKEN` - A GitHub PAT with `project` scope for project board access.

### Review Checklist

Before merging a PR, verify:
- Code follows project conventions
- No security vulnerabilities (OWASP top 10)
- No secrets or credentials exposed
- Quality checks pass (`pdm run lint` + `pdm run python -m ruff format --check .` + `pdm run test`)
- Changes match issue requirements
- **Human has explicitly confirmed the merge**

---

## Project Overview

**LumaireJ** is a journaling app for emotional self-awareness and reflection. MVP stage with growth planned.

### Tech Stack
- **Backend**: FastAPI + SQLModel + PostgreSQL (SQLite for dev)
- **Frontend**: Vanilla HTML/CSS/JS + HTMX
- **Package Manager**: PDM
- **Linting**: ruff
- **Testing**: pytest
- **CI/CD**: GitHub Actions → GitHub Pages (frontend)

### Architecture

```
app/
├── core/           # config.py, database.py - infrastructure
├── dependencies/   # session.py - FastAPI DI
├── models/         # SQLModel table definitions
├── schemas/        # Pydantic request/response validation
├── crud/           # Database operations (one file per resource)
├── api/v1/         # Versioned API routers
├── static/         # Frontend HTML/CSS/JS
├── constants.py    # Validation limits (single source of truth)
└── main.py         # App entry, middleware, lifespan
```

This modular structure is intentional (see `docs/adr/001-keep-modular-architecture.md`). Do not flatten.

---

## Code Patterns

### Adding a New Endpoint

1. **Model** (`app/models/<resource>.py`):
   ```python
   class Resource(SQLModel, table=True):
       __tablename__ = "resources"
       id: int | None = Field(primary_key=True)
       # fields with Field() for validation/description
   ```

2. **Schemas** (`app/schemas/<resource>.py`):
   ```python
   class ResourceCreate(BaseModel):  # Input validation
       model_config = ConfigDict(str_strip_whitespace=True)

   class ResourceRead(BaseModel):    # Output format
       model_config = ConfigDict(from_attributes=True)
   ```

3. **CRUD** (`app/crud/<resource>.py`):
   ```python
   def create_resource(session: Session, data: ResourceCreate) -> Resource:
       entry = Resource(**data.model_dump())
       session.add(entry)
       session.commit()
       session.refresh(entry)
       return entry
   ```

4. **Router** (`app/api/v1/endpoints/<resource>.py`):
   ```python
   router = APIRouter(prefix="/resource", tags=["Resource"])

   @router.post("", response_model=ResourceRead, status_code=status.HTTP_201_CREATED)
   def create(payload: ResourceCreate, session: Annotated[Session, Depends(get_session)]):
       return create_resource(session, payload)
   ```

5. **Register** in `app/api/v1/api.py`:
   ```python
   api_router.include_router(resource.router)
   ```

### Constants

Define validation limits in `app/constants.py`:
```python
CONTENT_MIN_LENGTH = 1
CONTENT_MAX_LENGTH = 5000
```

Import and use in models/schemas - single source of truth.

### Configuration

Environment variables in `.env` (see `.env.template`):
```
database_url=sqlite:///./test.db
debug=true
```

Access via `app/core/config.py`:
```python
from app.core.config import settings
settings.database_url
```

---

## Commands

```bash
# Development
pdm run dev              # Start server with hot reload

# Code quality
pdm run lint             # Check with ruff
pdm run format           # Auto-format with ruff

# Testing
pdm run test             # Run pytest with coverage

# Database
pdm run dbrevision       # Create Alembic migration
pdm run dbupgrade        # Apply migrations
```

---

## Testing Requirements

- Run `pdm run format`, `pdm run lint`, and `pdm run python -m ruff format --check .` before committing
- Run `pdm run test` before creating a PR
- Tests live in `tests/` directory
- Use `conftest.py` for fixtures
- Test files: `test_<module>.py`

### Test Fixture Pattern

```python
@pytest.fixture
def test_session():
    engine = create_engine("sqlite://", echo=False)
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
```

---

## Labels

| Label | Use For |
|-------|---------|
| `bug` | Defects, errors |
| `feature` | New functionality |
| `improvement` | Enhancements |
| `refactor` | Code restructure |
| `BACKEND` | API, database |
| `FRONTEND` | UI, views |
| `CONFIG` | Environment, settings |
| `TEST` | Test coverage |
| `DB` | Schema, migrations |
| `DEVOPS` | CI/CD, deployment |

### Priority & Size (estimation guidelines, not GitHub labels)

| Priority | When | Size | Scope |
|----------|------|------|-------|
| Critical | Production broken, security | XS | < 1 hour, single file |
| High | Core feature broken, blocks work | S | 1-2 hours, 1-3 files |
| Medium | Important but non-blocking | M | Half day, multiple files |
| Low | Nice to have, tech debt | L-XL | Full day+, significant |

---

## API Reference

- **Base URL**: `/api/v1`
- **Docs**: `/api/docs` (Swagger), `/api/redoc`
- **Health**: `/health`

### Current Endpoints

Refer to the auto-generated docs for the authoritative endpoint list:
- **Swagger UI**: run `pdm run dev`, then visit `http://localhost:8000/api/docs`
- **ReDoc**: `http://localhost:8000/api/redoc`

Do NOT maintain a static endpoint table here — the live docs are the single source of truth.

---

## File Locations

| What | Where |
|------|-------|
| Issue templates | `.github/ISSUE_TEMPLATE/` |
| PR template | `.github/pull_request_template.md` |
| CI workflows | `.github/workflows/` |
| ADRs | `docs/adr/` |
| Tests | `tests/` |
| Frontend | `app/static/` |
