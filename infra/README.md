# Infraestructura (Terraform / AWS)

Pendiente — **Fase 6**.

Aquí vivirá la definición de infraestructura como código:
- VPC con subredes pública / privada (app) / privada (datos)
- ECS Fargate + ECR
- RDS PostgreSQL (subred privada, cifrado KMS)
- ElastiCache Redis (subred privada)
- ALB + WAF
- IAM con menor privilegio
- Secrets Manager + KMS

El state de Terraform se guardará remoto (S3 + DynamoDB lock), cifrado.
