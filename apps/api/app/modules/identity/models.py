"""Modelos ORM del dominio de Identidad (esqueleto, se completa en Fase 1)."""
from sqlalchemy.orm import Mapped, mapped_column

from app.shared.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    full_name: Mapped[str]
    password_hash: Mapped[str]  # Argon2id
    mfa_secret: Mapped[str | None] = mapped_column(default=None)
    is_active: Mapped[bool] = mapped_column(default=True)
