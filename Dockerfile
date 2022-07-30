
FROM python:3.10-slim-buster AS base

RUN apt-get update \
    && apt-get upgrade -y

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /src
WORKDIR /src

RUN pip install --upgrade pip poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

RUN poetry install
COPY ./ /src/
RUN poetry install

ENV PYTHONPATH /src
ENV COLUMNS 80

CMD ["/bin/bash"]
