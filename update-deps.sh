#!/bin/bash

poetry add dpkt@latest
poetry add humanize@latest
poetry add inflect@latest
poetry add pydantic@latest -E email -E dotenv
poetry add structlog@latest
poetry add typer@latest -E all
poetry add ursine@latest

poetry install --no-dev
poetry update --no-dev
