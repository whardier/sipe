#!/bin/bash

sh ./update-deps.sh

# 5 is a big change and is mismatched against current vscode environment (07/2020)
poetry add -D "isort@<5"

poetry add -D autoflake@latest
poetry add -D bandit@latest
poetry add -D black@latest
poetry add -D coverage@latest
poetry add -D doc8@latest
poetry add -D flake8@latest
poetry add -D hypothesis@latest
poetry add -D mock@latest
poetry add -D mypy@latest
poetry add -D pytest-cov@latest
poetry add -D pytest@latest
poetry add -D rope@latest
poetry add -D setuptools@latest
poetry add -D sphinx@latest
poetry add -D tox@latest

poetry install
poetry update
