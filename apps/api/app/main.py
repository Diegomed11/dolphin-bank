"""Punto de entrada de la API del core bancario."""
from fastapi import FastAPI

from app.config import settings
from app.modules.accounts.router import router as accounts_router
from app.modules.identity.router import router as identity_router

app = FastAPI(
    title="Core Bancario Demo",
    version="0.1.0",
    description="Sistema bancario demo. Datos sintéticos únicamente.",
)


@app.get("/health", tags=["infra"])
def health() -> dict[str, str]:
    """Health check para load balancer y monitoreo."""
    return {"status": "ok", "env": settings.app_env}


# Registro de módulos (cada dominio expone su router)
app.include_router(identity_router)
app.include_router(accounts_router)
