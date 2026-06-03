"""Punto único de importación de los modelos ORM.

Importar este módulo garantiza que todos los modelos quedan registrados en
``Base.metadata`` (necesario para que Alembic los detecte en el autogenerate).
"""
from app.modules.accounts.models import Account  # noqa: F401
from app.modules.identity.models import User  # noqa: F401
from app.shared.database import Base  # noqa: F401

__all__ = ["Base", "User", "Account"]
