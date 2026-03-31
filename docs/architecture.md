# Arquitetura Corporativa Completa

## 1. Visão geral

Sistema web com 4 usuários internos, autenticação corporativa, painel operacional e engine de automação para orquestrar:

- Outlook (Microsoft Graph)
- Reserve (API ou scraping autenticado)
- Planilha corporativa (Google Sheets API ou Excel Graph)
- WhatsApp único central (Business API preferencial)

## 2. Componentes

- **Frontend React**
  - Login
  - Dashboard (status/últimos envios)
  - Integrações
  - Logs auditáveis
  - Modo manual
  - Gestão de usuários (4 acessos)

- **API Backend FastAPI**
  - Auth/session
  - Gestão de integrações por usuário
  - Endpoints de logs e dashboard
  - Endpoint de fallback manual

- **Automation Worker**
  - Monitoramento Outlook (subscription webhook + fallback polling)
  - Parsing Reserve e extração de voucher
  - Match de planilha
  - Envio WhatsApp
  - Auditoria e tratamento de falhas

- **PostgreSQL**
  - Usuários, integrações, jobs, eventos de auditoria, tentativas de envio

- **Object Storage (opcional)**
  - Guardar cópia de voucher para auditoria (S3/MinIO)

## 3. Fluxo ponta a ponta

1. Chega e-mail da Reserve no Outlook do usuário conectado.
2. Graph notifica webhook `/api/webhooks/graph`.
3. Worker valida remetente/assunto/conteúdo (voucher/check-in).
4. Parser extrai: `guest_name`, `reserve_plan_order`, metadados do voucher e anexo.
5. Planilha:
   - tenta match exato em coluna `plano`
   - se falhar, busca `guest_name` em coluna `observação`
6. Da linha obtida, pega `prefixo do carro`.
7. WhatsApp busca contato contendo o número do prefixo.
8. Envia voucher (PDF/Imagem) para contato.
9. Registra auditoria completa e atualiza dashboard.

## 4. Regra crítica de negócio

Os contatos de WhatsApp são identificados por **prefixo do carro**, não pelo nome do motorista. A estratégia de busca:

- Normalizar prefixo para dígitos (`420`)
- Buscar contatos por:
  - nome igual ao prefixo
  - nome contendo prefixo (`CARRO 420`)
- Resolver ambiguidade por ranking e confirmação automática de contexto

## 5. Tratamento de falhas

- **Não achou hóspede na planilha**: status `NOT_FOUND_SHEET`, gera item em modo manual.
- **Não achou prefixo**: status `NOT_FOUND_PREFIX`, exige intervenção manual.
- **Falha WhatsApp**: retry com backoff e depois `FAILED_DELIVERY`.
- **Falha de integração externa**: circuit breaker por serviço + alerta.

## 6. Segurança

- OAuth Microsoft com consentimento mínimo (mail.read, offline_access)
- Tokens por usuário armazenados criptografados
- Credenciais Reserve criptografadas em AES-GCM
- Sessão com JWT + refresh token rotativo
- Auditoria imutável lógica (append-only)
- Retenção de logs por 12 meses (job de expurgo)
- Suporte a proxy corporativo (`HTTP_PROXY`, `HTTPS_PROXY`, `NO_PROXY`)

## 7. Deploy sugerido

- **App/API:** Render/Railway/VPS
- **Banco:** PostgreSQL gerenciado
- **Worker:** processo dedicado no mesmo provedor
- **Observabilidade:** OpenTelemetry + Prometheus + painel Grafana

## 8. Modo manual (fallback)

Tela lista pendências e permite:

- visualizar dados extraídos do voucher
- revisar match de planilha/prefixo
- enviar com botão “Enviar”
- registrar justificativa e usuário executor
