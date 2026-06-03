"""Contratos (DTOs) del dominio de Cuentas."""
from enum import Enum

from pydantic import BaseModel, Field


class AccountType(str, Enum):
    checking = "checking"
    savings = "savings"


class CreateAccountRequest(BaseModel):
    type: AccountType
    currency: str = Field(default="MXN", min_length=3, max_length=3)


class AccountPublic(BaseModel):
    id: str
    type: AccountType
    currency: str
    status: str


class BalanceResponse(BaseModel):
    account_id: str
    # El saldo se expresa en centavos (entero) para evitar errores de redondeo.
    balance_cents: int
    currency: str
