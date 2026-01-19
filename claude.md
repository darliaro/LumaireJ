# LumaireJ - Claude Code Guide

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

## Workflow Rules

### CRITICAL: Issue-First Development

**Every change MUST start with a GitHub issue before any code.**

### Automated Workflow with Claude Commands

The project uses Claude commands (in `.claude/commands/`) to streamline development. GitHub automation handles project board transitions.

```
Concept → /new-issue → 📋 Backlog (GitHub auto)
              ↓
       /start-work → 🔄 In Progress (auto)
              ↓
    Code + /check + /commit (repeat)
              ↓
          /pr → 🤖 AI Review (GitHub auto)
              ↓
       /review-pr → Decision:
              ├─ APPROVED → auto-merge → ✅ Approved → 🚀 Deployed (GitHub auto)
              │                              ↓
              │                         /complete → ✨ Done (GitHub auto)
              │
              └─ CHANGES → 🔄 In Progress (GitHub auto)
                     ↓
                  /fix → push → back to review
```

### Claude Commands Reference

| Command | Purpose | Key Actions |
|---------|---------|-------------|
| `/new-issue` | Create GitHub issue | Creates issue, GitHub auto-adds to 📋 Backlog |
| `/start-work <#>` | Begin development | Creates branch, auto-moves issue to 🔄 In Progress |
| `/check` | Pre-commit validation | Runs lint + tests |
| `/commit [msg]` | Create commit | Formats with `[TYPE #issue]` + Co-Authored-By |
| `/pr [context]` | Create pull request | Runs checks, creates PR, GitHub auto-moves to 🤖 AI Review |
| `/review-pr <#>` | Review and decide | Approves + auto-merges OR requests changes |
| `/fix` | Fix post-review | Handles fix loop: fetch feedback → check → commit → push |
| `/complete <#>` | Post-merge cleanup | Updates local repo, deletes branch |

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

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"
```

Examples:
- `[FEAT #60] Add GET/PATCH/DELETE endpoints for journal`
- `[FIX #42] Handle null mood in validation`
- `[REFACTOR #57] Remove redundant whitespace stripping`

### GitHub Automation

Project board transitions are automated via `.github/workflows/project-automation.yml`:
- **Issue created** → 📋 Backlog
- **`/start-work`** → 🔄 In Progress (via gh CLI)
- **PR opened** → 🤖 AI Review
- **Changes requested** → 🔄 In Progress
- **Review approved** → ✅ Approved
- **PR merged** → 🚀 Deployed
- **Issue closed** → ✨ Done

**Required secret**: `PROJECT_TOKEN` - A GitHub PAT with `project` scope for project board access.

### Review Checklist

Before approving a PR, verify:
- Code follows project conventions
- No security vulnerabilities (OWASP top 10)
- No secrets or credentials exposed
- Linting passes (`pdm run lint`)
- Tests pass (`pdm run test`)
- Changes match issue requirements

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

- Run `pdm run lint` before committing
- Run `pdm run test` before pushing
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

### Priority

| Priority | When |
|----------|------|
| Critical | Production broken, security issue |
| High | Core feature broken, blocks work |
| Medium | Important but non-blocking |
| Low | Nice to have, tech debt |

### Size

| Size | Scope |
|------|-------|
| XS | < 1 hour, single file |
| S | 1-2 hours, 1-3 files |
| M | Half day, multiple files |
| L | Full day, significant |
| XL | Multiple days, architectural |

---

## API Reference

- **Base URL**: `/api/v1`
- **Docs**: `/api/docs` (Swagger), `/api/redoc`
- **Health**: `/health`

### Current Endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | `/api/v1/journal` | Create journal entry |
| GET | `/health` | Health check |

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
