# Architecture Overview

This project follows a **hexagonal / DDD-inspired** architecture:

* **api** – FastAPI routers (delivery)
* **core** – pure business logic & domain entities
* **adapters** – infrastructure integrations (DB, external APIs)
* **gpt** – Custom GPT manifest, actions, prompts
* **tasks** – background jobs (Celery)

![diagram](architecture.png)
