# 🐬 Bank Dolphin

> Sistema bancario **demo** de extremo a extremo: core transaccional + CRM + ERP, desplegado en AWS, con seguridad de nivel bancario, web y móvil


[![CI](https://github.com/Diegomed11/dolphin-bank/actions/workflows/ci.yml/badge.svg)](https://github.com/Diegomed11/dolphin-bank/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-009688)
![License](https://img.shields.io/badge/license-MIT-green)

---



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

La arquitectura completa está en [`docs/arquitectura-dolphin-bank.md`](docs/arquitectura-dolphin-bank.md).

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

## Estado del proyecto

> Actualizado: junio 2026 · Versión 0.1.0

**Fase 0 (Fundaciones) — ✅ completada.** El repositorio arranca en local de extremo a extremo, con migraciones de base de datos y un pipeline de CI con seguridad desde el día uno.

| Componente | Estado | Notas |
|---|---|---|
| Monorepo + estructura modular | ✅ | `apps/api` (FastAPI), `openapi/`, `infra/`, `security/`, `docs/` |
| Contratos OpenAPI (Identidad, Cuentas) | ✅ | Contract-first, antes de implementar |
| API FastAPI con `/health` | ✅ | Módulos `identity` y `accounts` registrados |
| Endpoints de Identidad y Cuentas | 🟡 stubs | Devuelven `501 Not Implemented` — se implementan en Fase 1 |
| Base de datos + migraciones (Alembic) | ✅ | Migración baseline `users` + `accounts`; corre sola en `docker compose up` |
| Docker Compose local (API + Postgres + Redis) | ✅ | Un comando levanta todo |
| CI: lint + tests + SAST + SCA + secret scan | ✅ | `ruff`, `bandit`, `pip-audit`, `gitleaks` en GitHub Actions |
| Suite local | ✅ verde | `ruff` · `bandit` (0 hallazgos) · `pytest` |
| Web (Next.js) | ⏳ pendiente | Fase 1+ |
| Móvil (Flutter) | ⏳ pendiente | Fase 5 |
| Infra AWS (Terraform) | ⏳ pendiente | Fase 6 |

Leyenda: ✅ hecho · 🟡 esqueleto / parcial · ⏳ pendiente

---

## Estructura del repo

```
dolphin-bank/
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
git clone https://github.com/Diegomed11/dolphin-bank.git
cd dolphin-bank

# 2. Copiar variables de entorno
cp .env.example .env

# 3. Levantar todo (API + Postgres + Redis)
#    Aplica las migraciones de Alembic automáticamente antes de arrancar.
docker compose up --build

# 4. Verificar
curl http://localhost:8000/health
# -> {"status":"ok","env":"development"}
```

La documentación interactiva de la API queda en **http://localhost:8000/docs** (Swagger UI, autogenerada por FastAPI).

---

## Desarrollo de la API sin Docker

```bash
cd apps/api
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev]"

# Aplicar migraciones (requiere una Postgres accesible vía DATABASE_URL)
alembic upgrade head

uvicorn app.main:app --reload
```

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

- [x] **Fase 0** — Fundaciones: scaffolding, contratos OpenAPI, migraciones, CI con seguridad
- [ ] **Fase 1** — Identidad (MFA, RBAC) + Cuentas
- [ ] **Fase 2** — ⭐ Ledger de doble partida + transferencias + auditoría
- [ ] **Fase 3** — CRM (onboarding, KYC)
- [ ] **Fase 4** — ERP / Contabilidad
- [ ] **Fase 5** — App móvil (Flutter)
- [ ] **Fase 6** — Despliegue en AWS + endurecimiento + lab de seguridad
- [ ] **Fase 7** — Antifraude con ML (opcional)

---

## Qué sigue (Fase 1)

El núcleo de la siguiente fase es **Identidad + Cuentas**, con seguridad real:

- Registro con hash **Argon2id** y validación estricta (Pydantic).
- Login en dos pasos + **MFA (TOTP)**.
- **JWT de vida corta** + refresh tokens rotativos.
- **RBAC** (cliente / operador / admin), `default = denegar`.
- Apertura y listado de cuentas con protección contra **IDOR** (verificación de propiedad del recurso).
- Tests de autorización (intentos de escalamiento, acceso cruzado).

Después llega el hito estrella (**Fase 2**): el ledger de doble partida con idempotencia, concurrencia segura y auditoría inmutable.

---

## Licencia

MIT — ver [`LICENSE`](LICENSE).
