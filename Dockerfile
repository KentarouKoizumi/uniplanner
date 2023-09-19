# syntax=docker/dockerfile:1
ARG APP_NAME="app"
ARG PYTHON_VERSION='3.10'
ARG PYTHON_BASE_IMAGE='python'
ARG POETRY_CACHE_DIR='/root/.cache/poetry'

FROM ${PYTHON_BASE_IMAGE}:${PYTHON_VERSION} AS poetry
ENV PYTONUNBUFFERD=true
RUN \
  --mount=type=cache,target=/var/lib/apt/lists \
  --mount=type=cache,target=/var/cache/apt/archives \
  apt-get update \
  && apt-get install -y --no-install-recommends build-essential

RUN \
  --mount=type=cache,target=/root/.cache/pip \
  pip install -U pip poetry

FROM poetry AS dev
ARG APP_NAME
ARG POETRY_CACHE_DIR
WORKDIR /workspace/${APP_NAME}
COPY pyproject.toml poetry.lock ./
RUN \
  --mount=type=cache,target=${POETRY_CACHE_DIR} \
  poetry config cache-dir ${POETRY_CACHE_DIR} && \
  poetry config installer.parallel false && \
  poetry config virtualenvs.create false && \ 
  poetry install --no-interaction

FROM poetry AS run
ARG POETRY_CACHE_DIR
WORKDIR /run
COPY pyproject.toml poetry.lock ./
RUN \
  --mount=type=cache,target=${POETRY_CACHE_DIR} \
  poetry config virtualenvs.in-project true && \
  poetry install --no-interaction
COPY . /run/${APP_NAME}
WORKDIR /run/${APP_NAME}
ENV APP_NAME=${APP_NAME}
ENTRYPOINT python -m ${APP_NAME}