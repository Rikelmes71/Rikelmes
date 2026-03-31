# Modelagem de Banco (PostgreSQL)

## Tabelas principais

### users
- id (uuid, pk)
- name
- email (unique)
- password_hash
- role (`admin`, `operator`)
- is_active
- created_at

### user_integrations
- id (uuid, pk)
- user_id (fk users)
- outlook_connected
- outlook_access_token_enc
- outlook_refresh_token_enc
- outlook_token_expires_at
- reserve_username_enc
- reserve_password_enc
- spreadsheet_provider (`google`|`excel`)
- spreadsheet_id_enc
- spreadsheet_sheet_name
- created_at
- updated_at

### automation_jobs
- id (uuid, pk)
- user_id (fk users)
- graph_message_id
- reserve_order_number
- guest_name
- car_prefix
- status (`RECEIVED`,`MATCHED`,`SENT`,`FAILED`,`MANUAL_REQUIRED`)
- failure_reason
- created_at
- updated_at

### delivery_attempts
- id (uuid, pk)
- job_id (fk automation_jobs)
- attempt_number
- whatsapp_target
- status (`SUCCESS`,`FAILED`)
- provider_message_id
- error_message
- created_at

### audit_logs
- id (bigserial, pk)
- user_id (nullable fk users)
- job_id (nullable fk automation_jobs)
- event_type
- event_payload (jsonb)
- ip_address
- created_at

## Índices recomendados

- `automation_jobs(graph_message_id)`
- `automation_jobs(reserve_order_number)`
- `automation_jobs(status, created_at desc)`
- `audit_logs(created_at desc)`
- `audit_logs(event_type, created_at desc)`

## Política de retenção

- Job diário remove `audit_logs` com mais de 12 meses.
