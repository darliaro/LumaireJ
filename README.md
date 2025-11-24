[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-black.svg)](https://www.python.org/)
[![HTMX](https://img.shields.io/badge/HTMX-purple?logo=html5)](https://htmx.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-teal?logo=fastapi)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-green?logo=postgresql)](https://www.postgresql.org/)
[![PyTest](https://img.shields.io/badge/PyTest-blue?logo=pytest)](https://pytest.org/)
[![Playwright](https://img.shields.io/badge/Playwright-blueviolet?logo=playwright)](https://playwright.dev/)
[![Allure TestOps](https://img.shields.io/badge/Allure-violet?logo=allure)](https://docs.qameta.io/allure-testops/)

# LumaireJ 🤍✨
#### A journaling app for emotional self-awareness and reflection

---

## Features (MVP)
- **Beautiful Landing Page** - Professional and aesthetic main page at `/`
- **Daily emotion & mood journaling** with optional tags/triggers
- **Enhanced UI/UX** - Modern, responsive design with smooth animations
- **Mood Suggestions** - Quick mood selection with emojis
- **View, edit, and delete past journal entries** (API endpoints)
- **Visualization of emotional trends** using charts (planned)
- **Calm, minimal UI** with FastAPI, Jinja2 & HTMX
- **Testable and maintainable codebase** with CI-friendly structure

---

## Quick Start

### **Option 1: Direct Access**
1. Start the application: `pdm run dev`
2. Open your browser at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### **Option 2: Journal Interface**
1. Navigate to: [http://127.0.0.1:8000/static/journal.html](http://127.0.0.1:8000/static/journal.html)
2. Or click "Create Your First Entry" from the main page

### **Option 3: API Documentation**
- Swagger UI: [http://127.0.0.1:8000/api/docs](http://127.0.0.1:8000/api/docs)
- ReDoc: [http://127.0.0.1:8000/api/redoc](http://127.0.0.1:8000/api/redoc)

---

## Initial Setup (Using PDM)
- [ ] Install [Python](https://www.python.org/downloads/) (version 3.11 or 3.12 recommended)
- [ ] Install [PDM](https://pdm-project.org/latest/#recommended-installation-method):
  ```bash
  curl -sSL https://pdm-project.org/install-pdm.py | python3
  ```
- [ ] Initialize the project:
  ```bash
  pdm init
  ```
- [ ] Install project dependencies:
  ```bash
  pdm install
  ```
- [ ] Set up pre-commit hooks (optional):
  ```bash
  pdm add pre-commit --dev
  pre-commit install -f
  ```
- [ ] Create `.env` file for environment variables:
  ```bash
  touch .env
  echo "database_url=sqlite:///./test.db" >> .env
  echo "debug=true" >> .env
  ```
  The FastAPI app and Alembic migrations both read the same `database_url` value (Alembic also
  accepts the legacy `DATABASE_URL` variable for compatibility).

---

## Running the App Locally
Start the FastAPI server with:

```bash
pdm run dev
```

Then open your browser at:
[http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Running Tests

### Through Terminal
- Basic Run:
  ```bash
  pdm run pytest -sv tests/path_to_file_or_directory
  ```
- Run with Browser UI / Headed:
  ```bash
  pdm run pytest -sv --headed tests/path_to_file_or_directory
  ```
- Debug Run (slowed interactions):
  ```bash
  pdm run pytest -sv --headed --slowmo 500 tests/path_to_file_or_directory
  ```

### Generate Allure Reports
```bash
pdm run pytest -sv --alluredir=allure-results tests/path_to_file_or_directory
allure generate allure-results --clean -o allure-report
allure open allure-report
```

---

## Running Tests in GitHub Actions
1. Go to [GitHub Actions](https://github.com/darliaro/lumairej/actions)
2. Select the desired workflow (e.g., UI Tests)
3. Click **Run workflow**
4. Choose branch and trigger the run

---

## Code Quality & Formatting with [ruff](https://github.com/astral-sh/ruff)
- Check Code Quality:
  ```bash
  pdm run ruff check path_to_file_or_folder
  ```
- Autofix Issues:
  ```bash
  pdm run ruff check path_to_file_or_folder --fix
  ```
- Format Code:
  ```bash
  pdm run ruff format path_to_file_or_folder --fix
  ```

---

## Tips for Testing
- Use `conftest.py` in test directories to define reusable fixtures/hooks
- Use `--headed` and `--slowmo` for visual debugging during UI test runs
- Maintain small, isolated test units alongside high-level E2E flows

---

## Deployment

### GitHub Pages
The frontend is automatically deployed to GitHub Pages on every push to `main` branch.

- **Live Site**: Available at `https://darliaro.github.io/LumaireJ/` (after first deployment)
- **Deployment**: Automatic via GitHub Actions workflow (`.github/workflows/deploy-pages.yml`)
- **Manual Deployment**: Go to repository Settings → Pages → Build and deployment

### Local Development
For full-stack development (frontend + backend API):

```bash
pdm run dev
```

Then access:
- Frontend: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- API Docs: [http://127.0.0.1:8000/api/docs](http://127.0.0.1:8000/api/docs)

## Future Enhancements
- Telegram bot integration for check-ins and affirmations
- Advanced visualizations of emotion trends
- User authentication (optional)
- Backend API hosting (Vercel, Railway, or Render)
- Dark/Light theme toggle
- Export functionality (PDF, JSON)
