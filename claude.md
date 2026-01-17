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

1. Create issue using template from `.github/ISSUE_TEMPLATE/`:
   - `bug_report.md` - Defects
   - `feature_request.md` - New functionality
   - `refactor.md` - Code improvements (no behavior change)
   - `architecture_task.md` - Infrastructure changes

2. Add to project board:
   ```bash
   gh issue create --title "[TYPE] Description" --body "..." --label "labels" --assignee darliaro
   gh project item-add 1 --owner darliaro --url <issue-url>
   ```

3. Create branch AFTER issue exists:
   ```bash
   git checkout -b <type>/<issue-number>-<short-description>
   ```

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

### Pull Request Process

1. Push branch and create PR:
   ```bash
   git push -u origin <branch>
   gh pr create --title "[TYPE #issue] Description" --body "..." \
     --assignee darliaro --reviewer darliaro --label "labels"
   ```

2. Add PR to project board:
   ```bash
   gh project item-add 1 --owner darliaro --url <pr-url>
   ```

3. **Review the PR** (required before merge):
   - Code follows project conventions
   - No security vulnerabilities (OWASP top 10)
   - No secrets or credentials exposed
   - Linting passes
   - Tests pass
   - Changes match issue requirements

4. After merge, move issue to "Done":
   ```bash
   gh project item-edit --project-id PVT_kwHODR8J4s4A9wbx \
     --id <item-id> --field-id PVTSSF_lAHODR8J4s4A9wbxzgxXTgM \
     --single-select-option-id caff0873
   ```

### Project Board Columns

| Column | Meaning |
|--------|---------|
| Backlog | Accepted, waiting |
| To Do | Planned for current cycle |
| In Progress | Actively working |
| Ready for Test | Code complete, awaiting QA |
| QA | Being tested |
| Done | Verified complete |

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
