# Base image
FROM python:3.13-slim

# Disable .pyc files and force unbuffered stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Make PDM-installed scripts available on PATH
ENV PATH=/app/__pypackages__/3.13/bin:$PATH
ENV PYTHONPATH=/app/__pypackages__/3.13/lib

# Set workdir
WORKDIR /app

# Install PDM and its runtime dependencies, then clean up apt cache
RUN apt-get update \
 && apt-get install -y --no-install-recommends gcc \
 && pip install --no-cache-dir pdm \
 && pdm config python.use_venv false \
 && apt-get purge -y --auto-remove gcc \
 && rm -rf /var/lib/apt/lists/*

# Copy only manifest and lockfile, install production dependencies
COPY pyproject.toml pdm.lock ./
RUN pdm sync --prod

# Copy application code
COPY . .

# Expose HTTP port
EXPOSE 8000

# Launch Uvicorn on all interfaces (no runtime installs)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
