# Seguridad

Carpeta de artefactos de seguridad del proyec

## Contenido (se irá poblando)
- `threat-model.md` — modelo STRIDE por dominio
- `asvs-checklist.md` — checklist OWASP ASVS nivel 2
- `audit-reports/` — reportes de las pruebas en laboratorio controlado

## Recordatorio
Todo testing de seguridad se hace contra **este sistema**, en **entorno aislado**,
con **datos sintéticos**. Nunca contra terceros ni con datos reales.

## Pipeline de seguridad (ya activo desde Fase 0)
- SAST: bandit + ruff (regla S)
- SCA: pip-audit
- Secret scanning: gitleaks
- Pre-commit hooks locales
