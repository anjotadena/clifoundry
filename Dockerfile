FROM python:3.12-slim

# System deps (keep minimal; add more later if your CLI needs them)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Create non-root user
RUN useradd -m appuser
USER appuser

# Copy metadata first for better caching
COPY --chown=appuser:appuser pyproject.toml README.md LICENSE /app/

# Install package + dev deps (editable install done via compose volume later)
RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -e .[dev]

# Copy sources
COPY --chown=appuser:appuser src /app/src
COPY --chown=appuser:appuser tests /app/tests

ENV PYTHONPATH=/app/src

ENTRYPOINT ["clifoundry"]