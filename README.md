# Gandra Codex Demo Projects

This repository contains multiple demo applications showcasing Spring Authorization Server and resource servers along with Python, NestJS and Angular clients. A PostgreSQL instance is provided via Docker Compose.

## Projects

- **sc-authorization-server** – Spring Boot application running Spring Authorization Server.
- **sc-white-pages-api** – Resource server exposing a `Person` entity.
- **sc-cities-api** – Resource server exposing geographical entities (`Country`, `Municipality`, `Place`, `Locality`).
- **sc-client** – Example Spring Boot client application.
- **sc-cities-py** – Python demo client consuming the APIs using OAuth tokens.
- **sc-books-js-api** – NestJS resource server that can also call `sc-cities-api`.
- **sc-books-ui** – Angular application consuming `sc-books-js-api`.

Run `docker compose up -d` to start the PostgreSQL database used by the applications.

Each project contains its own README with build and run instructions.
