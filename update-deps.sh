#!/bin/bash

poetry add any-case@latest
poetry add construct@latest
poetry add dpkt@latest
poetry add humanize@latest
poetry add inflect@latest
poetry add pydantic@latest -E email -E dotenv
poetry add stevedore@latest
poetry add structlog@latest
poetry add tomlkit@latest
poetry add toml-sort@latest
poetry add typer@latest -E all
poetry add ursine@latest

poetry install --no-dev
poetry update --no-dev
