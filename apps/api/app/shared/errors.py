"""Errores de dominio compartidos."""


class DomainError(Exception):
    """Base para errores de negocio."""


class NotFoundError(DomainError):
    """El recurso solicitado no existe."""


class UnauthorizedError(DomainError):
    """El actor no tiene permiso para esta operación."""
