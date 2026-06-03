"""Contratos (DTOs) del dominio de Identidad."""
from pydantic import BaseModel, EmailStr, Field


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=12, description="Mínimo 12 caracteres")
    full_name: str = Field(min_length=2, max_length=120)


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class MFAVerifyRequest(BaseModel):
    mfa_token: str = Field(description="Token temporal emitido tras login")
    code: str = Field(min_length=6, max_length=6, description="Código TOTP de 6 dígitos")


class TokenPair(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"  # noqa: S105 (esquema OAuth2, no es un secreto)


class UserPublic(BaseModel):
    id: str
    email: EmailStr
    full_name: str
    roles: list[str]
