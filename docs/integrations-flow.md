# Fluxo detalhado das integrações

## Microsoft Graph (Outlook)

1. Usuário conecta conta via OAuth 2.0.
2. Sistema salva refresh token criptografado.
3. API cria assinatura de mailbox (webhook).
4. Ao receber evento, worker busca o e-mail completo e anexos.

## Reserve

- **Se houver API**: consumir endpoint autenticado para validar pedido/voucher.
- **Sem API**: automação autenticada com sessão técnica, com controles anti-bloqueio e trilha de auditoria.

## Planilha corporativa

- **Google Sheets API**: leitura da aba com cabeçalho fixo.
- **Excel Online (Graph)**: leitura de tabela/worksheet no OneDrive/SharePoint.

Ordem da busca:
1. `plano (pedido Reserve)` == coluna `plano`
2. fallback: `nome do hóspede` contido em `observação`

## WhatsApp

Preferência de implementação:
1. WhatsApp Business API oficial.
2. Automação WhatsApp Web segura (fallback controlado, conta central dedicada).

Regra de busca do destinatário:
- obter `prefixo do carro`
- localizar contato cujo nome contenha o prefixo
- enviar voucher e registrar `provider_message_id`
