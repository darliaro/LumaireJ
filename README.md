[![Python 3.14+](https://img.shields.io/badge/Python-3.14+-black.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-teal?logo=fastapi)](https://fastapi.tiangolo.com/)
[![SQLModel](https://img.shields.io/badge/SQLModel-0.0.22-blue)](https://sqlmodel.tiangolo.com/)
[![HTMX](https://img.shields.io/badge/HTMX-purple?logo=html5)](https://htmx.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-green?logo=postgresql)](https://www.postgresql.org/)
[![PyTest](https://img.shields.io/badge/PyTest-blue?logo=pytest)](https://pytest.org/)
[![Playwright](https://img.shields.io/badge/Playwright-blueviolet?logo=playwright)](https://playwright.dev/)
[![CI](https://img.shields.io/badge/CI-GitHub_Actions-black?logo=githubactions)](https://github.com/dariero/LumaireJ/actions)

# LumaireJ
A journaling application focused on emotional self-awareness and reflective practice, built with a modular FastAPI backend and a minimal HTMX-driven UI.

---

## Overview
LumaireJ combines a small, focused API surface with a clean UI to support daily mood journaling. The backend follows clear boundaries between API, domain, persistence, and configuration, enabling fast iteration without compromising maintainability.

---

## Architecture
```
app/
├── api/v1/          # FastAPI routers and endpoints
├── core/            # settings, database, exceptions
├── dependencies/    # dependency injection
├── models/          # SQLModel tables
├── schemas/         # Pydantic request/response models
├── crud/            # persistence operations
└── main.py          # FastAPI app assembly
```

---

## Tech Stack
- **API**: FastAPI
- **Data**: SQLModel + SQLAlchemy
- **DB**: PostgreSQL (SQLite for local/dev)
- **UI**: HTMX + static HTML
- **Testing**: Pytest (unit) and Playwright (E2E/UI)
- **Tooling**: PDM, Ruff
- **CI/CD**: GitHub Actions, GitHub Pages

---

## Quick Start
### Prerequisites
- Python 3.14+
- PDM

### Install and Run
```bash
pdm install
pdm run dev
```
Open:
- App: http://127.0.0.1:8000
- Docs: http://127.0.0.1:8000/api/docs

---

## Configuration
Create a `.env` file at the project root:
```bash
database_url=sqlite:///./lumairej.db
debug=true
allowed_origins=http://localhost,http://127.0.0.1:8000
```
Alembic and FastAPI both read `database_url` (legacy `DATABASE_URL` is also supported).

---

## Database & Migrations
```bash
pdm run dbrevision
pdm run dbupgrade
```

---

## Testing
```bash
pdm run pytest
```
For UI/E2E runs (Playwright):
```bash
pdm run pytest --headed
```

---

## CI/CD
- **CI**: GitHub Actions runs lint and test workflows
- **Pages**: Static UI deploys to GitHub Pages on `main`
- Actions: https://github.com/dariero/LumaireJ/actions
- Live site: https://dariero.github.io/LumaireJ/

---

## Technical Decisions
- **Modular layering**: API, schema, CRUD, and configuration layers remain separate to keep responsibilities isolated and testable. See `docs/adr/001-keep-modular-architecture.md`.
- **Sync SQLModel for MVP**: The current SQLModel session is synchronous for simplicity; the service boundary makes it straightforward to migrate to `AsyncSession` if concurrency grows.
- **Explicit dependencies**: FastAPI dependencies are centralized in `dependencies/` to avoid hidden coupling.
- **SDLC approach**: Small, traceable changes with ADRs for architectural decisions, CI gates on lint/tests, and incremental releases.

---

## Roadmap
- Add GET/PATCH/DELETE endpoints for journal entries
- Mood trend visualization
- Export formats (PDF/JSON)
- Optional authentication

---

## Author
Darie Ro
