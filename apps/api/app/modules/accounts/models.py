"""Modelos ORM del dominio de Cuentas (esqueleto, se completa en Fase 1-2)."""
from sqlalchemy.orm import Mapped, mapped_column

from app.shared.database import Base


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[str] = mapped_column(primary_key=True)
    owner_id: Mapped[str | None] = mapped_column(index=True)
    type: Mapped[str]
    currency: Mapped[str] = mapped_column(default="MXN")
    status: Mapped[str] = mapped_column(default="active")
