VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
UVICORN := $(VENV)/bin/uvicorn
PYTEST := $(VENV)/bin/pytest

.PHONY: venv install run test up down fmt lint

venv:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip

install: venv
	$(PIP) install -r requirements.txt

run:
	$(UVICORN) trader.app.main:app --reload --host 0.0.0.0 --port 8000

test:
	$(PYTEST) -q

up:
	docker compose up -d --build

down:
	docker compose down -v