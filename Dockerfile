FROM python:3.12-slim

# System deps (keep minimal; add more later if your CLI needs them)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Create non-root user and ensure /app is writable
RUN useradd -m appuser \
  && chown -R appuser:appuser /app
USER appuser

# Copy metadata first for better caching
COPY --chown=appuser:appuser pyproject.toml README.md LICENSE /app/

# Copy sources
COPY --chown=appuser:appuser src /app/src
COPY --chown=appuser:appuser tests /app/tests

# Install package + dev deps
RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -e .[dev]

ENV PYTHONPATH=/app/src
ENV PATH=/home/appuser/.local/bin:$PATH

CMD ["clifoundry"]