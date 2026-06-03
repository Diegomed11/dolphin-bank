"""Endpoints del dominio de Cuentas.

Fase 0: contratos definidos, lógica pendiente (Fase 1).
"""
from fastapi import APIRouter, HTTPException, status

from app.modules.accounts.schemas import (
    AccountPublic,
    BalanceResponse,
    CreateAccountRequest,
)

router = APIRouter(prefix="/accounts", tags=["accounts"])


@router.post("", response_model=AccountPublic, status_code=status.HTTP_201_CREATED)
def create_account(_body: CreateAccountRequest) -> AccountPublic:
    """Abre una nueva cuenta para el usuario autenticado. (Fase 1.)"""
    raise HTTPException(status.HTTP_501_NOT_IMPLEMENTED, "Pendiente: Fase 1")


@router.get("", response_model=list[AccountPublic])
def list_accounts() -> list[AccountPublic]:
    """Lista las cuentas del usuario autenticado. (Fase 1.)"""
    raise HTTPException(status.HTTP_501_NOT_IMPLEMENTED, "Pendiente: Fase 1")


@router.get("/{account_id}/balance", response_model=BalanceResponse)
def get_balance(account_id: str) -> BalanceResponse:
    """Devuelve el saldo derivado de los asientos del ledger. (Fase 2.)"""
    raise HTTPException(status.HTTP_501_NOT_IMPLEMENTED, "Pendiente: Fase 2")
