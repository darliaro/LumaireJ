# Use Python 3.14 image (matching pyproject.toml requirement)
FROM python:3.14-slim

# Exclude .pyc files and disable stdout buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory to /app
WORKDIR /app

# Install build dependencies and curl for healthcheck
RUN apt-get update \
 && apt-get install -y --no-install-recommends build-essential curl \
 && rm -rf /var/lib/apt/lists/*

# Install PDM
RUN pip install --no-cache-dir pdm

# Copy dependency files
COPY pyproject.toml pdm.lock ./

# Install production dependencies only (no dev deps)
RUN pdm install --prod --no-lock --no-editable

# Create non-root user
RUN adduser --disabled-password --gecos "" appuser

# Copy application source code
COPY --chown=appuser:appuser app ./app

# Switch to non-root user
USER appuser

# Expose application port
EXPOSE 8000

# Start the app
CMD ["pdm", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
