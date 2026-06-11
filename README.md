
***

# 📦 Industrial Asset Maintenance System (v1)

A lightweight Industrial Asset Management API designed for performance and clean code.

## 🚀 Overview
This project is built to demonstrate **Clean Architecture** and **Domain-Driven Design (DDD)** using modern Python 3.12+ standards. It is designed to be lightweight, modular, and easy to deploy.

*   **⚡ Framework:** FastAPI
*   **🚀 Dependency Management:** `uv`
*   **🧠 Architecture:** DDD-inspired (Application / Domain / Infrastructure / Presentation)
*   **🧪 Testing:** Pytest suite
*   **🐳 Deployment:** Dockerized & Vercel-ready
*   **🤖 CI/CD:** GitHub Actions automation

> **Note:** This project is designed for learning clean architecture + modern Python tooling (2026 style).

---

## 🏗 Architecture Overview

The project follows a strict separation of concerns:

```text
app/
├── application/       # Use cases (business logic)
├── domain/            # Entities (Asset)
├── infrastructure/    # In-memory repository
├── web/
│   ├── api/           # FastAPI routes
│   └── schemas/       # Pydantic models
└── main.py            # App entrypoint
```

---

## 🚀 Features

### Asset Management
*   **Create Asset:** Register new industrial equipment.
*   **List Assets:** Retrieve all registered assets.
*   **Delete Asset:** Remove assets from the system.
*   **Storage:** Lightweight in-memory persistence (no database required).

---

## 🛠 Engineering Principles

This system enforces high-quality software engineering standards:

*   **SOLID Principles:** Applied throughout the layers to ensure maintainability.
*   **DDD-style Separation:** Clear boundaries between business rules, application logic, and infrastructure.
*   **OOP-based Repository Pattern:** Abstracted data access to keep the domain layer decoupled from the persistence implementation.
