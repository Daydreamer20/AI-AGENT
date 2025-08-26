# AI Trading Agent

Foundation scaffold for the AI Trading Agent.

## Quickstart

- Create venv and install deps:
```bash
make install
```

- Run API locally:
```bash
make run
```

- Run tests:
```bash
make test
```

## Docker

- Start stack (app + Postgres + Redis):
```bash
make up
```

- Stop stack:
```bash
make down
```

Environment variables are loaded from `.env` (see `.env.example`).