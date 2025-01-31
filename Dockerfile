FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    curl \
    netcat-openbsd && \
    apt-get clean

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH=/app

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

COPY . .
