# Black Hub Games test task:
https://docs.google.com/document/d/1074lx20YAXAC5yMe8FZzPMdKngWF8oB9NKQM10-Ikgc/mobilebasic

#  Service "BlackHubGetServer"

The project provides a simple interface for sending GET requests to the address of a web server to receive web pages with changed information.

## Used technologies

- [FastAPI](https://fastapi.tiangolo.com/) is a modern, fast (high-performance), web framework for building APIs.
- [Uvicorn](https://www.uvicorn.org/) is an ASGI web server implementation for Python.

## Environments

- use `pyproject.toml`
- edit the black.service file and use it to create a service via systemd

## Configs

- `config.toml`
- LEVEL_LOG — Logging level
  - 0 — DEBUG
  - 1 — INFO
  - 2 — WARNING
  - 3 — ERROR
 
 - add path_config in 'app/logger.py'
 - add uvicorn_addr in 'tests/tests_modules.py'
 - add uvicorn_port in 'tests/tests_modules.py'
 
  ## Tests
  - `tests/tests_modules.py`
  
  
