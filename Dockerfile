# Use lightweight Python 3.13 image
FROM python:3.13-slim

# Don't write .pyc files and disable stdout buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Add PDM-managed packages to PATH and PYTHONPATH
ENV PATH=/app/__pypackages__/3.13/bin:$PATH
ENV PYTHONPATH=/app/__pypackages__/3.13/lib

# Set working directory to /app
WORKDIR /app

# Install build dependencies, PDM, then clean up
RUN apt-get update \
 && apt-get install -y --no-install-recommends gcc \
 && pip install --no-cache-dir pdm \
 && pdm config python.use_venv false \
 && apt-get purge -y --auto-remove gcc \
 && rm -rf /var/lib/apt/lists/*

# Copy dependency manifests and install production packages
COPY pyproject.toml pdm.lock ./
RUN pdm sync --prod

# Copy application source code
COPY . .

# Expose application port
EXPOSE 8000

# Start the app with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
