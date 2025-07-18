FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH=/app/__pypackages__/3.13/bin:$PATH
ENV PYTHONPATH=/app/__pypackages__/3.13/lib

WORKDIR /app

RUN apt-get update \
 && apt-get install -y --no-install-recommends gcc \
 && pip install --no-cache-dir pdm \
 && pdm config python.use_venv false \
 && apt-get purge -y --auto-remove gcc \
 && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml pdm.lock ./
RUN pdm install

COPY . .

EXPOSE 8000
CMD ["bash","-lc","pdm install && pdm run dev"]