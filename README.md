[![Python 3.10+](https://img.shields.io/badge/Python-3.13+-black.svg)](https://www.python.org/)
[![HTMX](https://img.shields.io/badge/HTMX-purple?logo=html5)](https://htmx.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-teal?logo=fastapi)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-green?logo=postgresql)](https://www.postgresql.org/)
[![PyTest](https://img.shields.io/badge/PyTest-blue?logo=pytest)](https://pytest.org/)
[![Playwright](https://img.shields.io/badge/Playwright-blueviolet?logo=playwright)](https://playwright.dev/)
[![Allure TestOps](https://img.shields.io/badge/Allure-violet?logo=allure)](https://docs.qameta.io/allure-testops/)

# LumaireJ 🤍✨
#### A journaling app for emotional self-awareness and reflection (_by Darli Ro_)

---

## Features (MVP)
- Daily emotion & mood journaling with optional tags/triggers
- Soft affirmations and prompts on entry or via Telegram bot (TBD)
- View, edit, and delete past journal entries
- Visualization of emotional trends using charts
- Calm, minimal UI with FastAPI, Jinja2 & HTMX
- Testable and maintainable codebase with CI-friendly structure

---

## Initial Setup (Using PDM)
- [ ] Install [Python](https://www.python.org/downloads/) (version 3.13+ recommended)
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
  ```

---

## Running the App Locally
Start the FastAPI server with:

```bash
pdm run uvicorn app.main:app --reload
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

## Future Enhancements
- Telegram bot integration for check-ins and affirmations
- Advanced visualizations of emotion trends
- User authentication (optional)
- Deployment with Docker