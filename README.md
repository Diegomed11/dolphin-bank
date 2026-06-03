# 🏦 Core Bancario Demo

> Sistema bancario **demo** de extremo a extremo: core transaccional + CRM + ERP, desplegado en AWS, con seguridad de nivel bancario, web y móvil.

[![CI](https://github.com/Diegomed11/core-bancario/actions/workflows/ci.yml/badge.svg)](https://github.com/Diegomed11/core-bancario/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-009688)
![License](https://img.shields.io/badge/license-MIT-green)

---

## ⚠️ Aviso

Este es un **proyecto demostrativo de portafolio**. No es un banco real, no opera dinero real, no busca licencia regulatoria y **no debe usarse con datos reales de personas**. Todo el manejo de datos se hace con información sintética.

---

## ¿Qué es esto?

Un sistema que demuestra cómo se construye un banco moderno de forma correcta y segura:

- **Core transaccional** con un *ledger de doble partida* (saldos derivados, nunca mutados).
- **CRM** para gestión de clientes, onboarding y KYC.
- **ERP / Contabilidad** con plan de cuentas, conciliación y reportes.
- **Seguridad rigurosa**: MFA, RBAC/ABAC, cifrado, auditoría inmutable, validada con pruebas en laboratorio controlado.
- **Apps web y móvil** sobre las mismas APIs.
- Desplegado en **AWS** con IaC (Terraform) y CI/CD.

La arquitectura completa está en [`docs/arquitectura-core-bancario.md`](docs/arquitectura-core-bancario.md).

---

## Stack

| Capa | Tecnología |
|---|---|
| API | FastAPI (Python 3.12) |
| Base de datos | PostgreSQL |
| Cache / locks | Redis |
| Web | Next.js + Tailwind + ShadCN |
| Móvil | Flutter (Dart) — Android + iOS |
| Infra | AWS + Terraform |
| CI/CD | GitHub Actions (con SAST, SCA y secret scanning) |

---

## Estructura del repo

```
core-bancario/
├── apps/
│   ├── api/                 # Backend FastAPI (monolito modular)
│   ├── web/                 # Frontend web (próximamente)
│   └── mobile/              # App Flutter (Android + iOS, próximamente)
├── openapi/                 # Contratos OpenAPI (contract-first)
├── infra/                   # Terraform (AWS)
├── security/                # Threat models, reportes de auditoría, checklists
├── docs/                    # Arquitectura y ADRs
└── .github/workflows/       # Pipelines de CI/CD
```

---

## Cómo correr en local

Requisitos: [Docker](https://docs.docker.com/get-docker/) y Docker Compose.

```bash
# 1. Clonar
git clone https://github.com/Diegomed11/core-bancario.git
cd core-bancario

# 2. Copiar variables de entorno
cp .env.example .env

# 3. Levantar todo (API + Postgres + Redis)
docker compose up --build

# 4. Verificar
curl http://localhost:8000/health
# -> {"status":"ok"}
```

La documentación interactiva de la API queda en **http://localhost:8000/docs** (Swagger UI, autogenerada por FastAPI).

---

## Desarrollo de la API sin Docker

```bash
cd apps/api
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
alembic upgrade head        # aplica las migraciones de la BD
uvicorn app.main:app --reload
```

> Las migraciones de base de datos se gestionan con **Alembic** (`apps/api/migrations`).
> Crear una nueva: `alembic revision --autogenerate -m "mensaje"`. Aplicarlas: `alembic upgrade head`.
> En Docker, `docker compose up` corre `alembic upgrade head` automáticamente antes de levantar la API.

---

## Tests y seguridad

```bash
cd apps/api

pytest                 # tests unitarios
ruff check .           # linting
bandit -r app          # análisis estático de seguridad (SAST)
pip-audit              # dependencias vulnerables (SCA)
```

Estas mismas verificaciones corren automáticamente en cada push vía GitHub Actions.

---

## Roadmap

- [x] **Fase 0** — Fundaciones: scaffolding, contratos OpenAPI, CI con seguridad
- [ ] **Fase 1** — Identidad (MFA, RBAC) + Cuentas
- [ ] **Fase 2** — ⭐ Ledger de doble partida + transferencias + auditoría
- [ ] **Fase 3** — CRM (onboarding, KYC)
- [ ] **Fase 4** — ERP / Contabilidad
- [ ] **Fase 5** — App móvil
- [ ] **Fase 6** — Despliegue en AWS + endurecimiento + lab de seguridad
- [ ] **Fase 7** — Antifraude con ML (opcional)

---

## Licencia

MIT — ver [`LICENSE`](LICENSE).
