"""Endpoints del dominio de Identidad.

Fase 0: contratos definidos, lógica pendiente (Fase 1).
"""
from fastapi import APIRouter, HTTPException, status

from app.modules.identity.schemas import (
    LoginRequest,
    MFAVerifyRequest,
    RegisterRequest,
    TokenPair,
    UserPublic,
)

router = APIRouter(prefix="/auth", tags=["identity"])


@router.post("/register", response_model=UserPublic, status_code=status.HTTP_201_CREATED)
def register(_body: RegisterRequest) -> UserPublic:
    """Registra un nuevo usuario. (Pendiente de implementación - Fase 1.)"""
    raise HTTPException(status.HTTP_501_NOT_IMPLEMENTED, "Pendiente: Fase 1")


@router.post("/login")
def login(_body: LoginRequest) -> dict:
    """Valida credenciales y devuelve un token temporal para el paso de MFA."""
    raise HTTPException(status.HTTP_501_NOT_IMPLEMENTED, "Pendiente: Fase 1")


@router.post("/mfa/verify", response_model=TokenPair)
def verify_mfa(_body: MFAVerifyRequest) -> TokenPair:
    """Verifica el código TOTP y emite el par de tokens de acceso."""
    raise HTTPException(status.HTTP_501_NOT_IMPLEMENTED, "Pendiente: Fase 1")
