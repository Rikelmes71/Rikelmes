# CS Brasil - Automação Operacional Reserve → Outlook → Planilha → WhatsApp

Projeto base corporativo para automatizar o fluxo crítico de envio de vouchers da Reserve, com rastreabilidade completa e fallback manual.

## Entregáveis incluídos

- Arquitetura completa (lógica, segurança, integrações e operação): `docs/architecture.md`
- Modelagem de banco: `docs/database.md` + modelos SQLAlchemy em `backend/app/models`
- Estrutura de pastas backend/frontend
- Código base backend (FastAPI + worker + serviços de integração)
- Código base frontend (React)
- Fluxo detalhado das integrações
- Passo a passo de execução

## Stack adotada

- **Backend:** Python 3.12 + FastAPI + SQLAlchemy + PostgreSQL
- **Worker:** processamento assíncrono de e-mails/vouchers
- **Frontend:** React + Vite
- **Integrações:** Microsoft Graph, Planilha (Google Sheets ou Excel Graph), WhatsApp Business API / WhatsApp Web automação controlada

## Como rodar (local)

### 1) Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --port 8000
```

### 2) Worker de automação

```bash
cd backend
source .venv/bin/activate
python -m app.workers.email_worker
```

### 3) Frontend

```bash
cd frontend
npm install
npm run dev
```

### 4) Banco PostgreSQL

Suba um PostgreSQL local/container e configure `DATABASE_URL` no `.env`.

## Fluxo automatizado (resumo)

1. Webhook/polling Graph captura e-mail da Reserve.
2. Parser extrai hóspede, pedido (plano) e anexo voucher.
3. Serviço de planilha tenta casar por coluna **plano**; fallback por **observação** contendo hóspede.
4. Obtém **prefixo do carro**.
5. Serviço WhatsApp busca contato cujo nome contenha o número do prefixo (ex.: `420`, `CARRO 420`).
6. Envia voucher.
7. Registra log auditável (quem, quando, mensagem-id, prefixo, status).

## Observações corporativas

- Logs com retenção de 12 meses.
- Segredos criptografados em AES-GCM.
- Suporte a modo manual obrigatório.
- Preparado para proxy corporativo via variáveis de ambiente.
