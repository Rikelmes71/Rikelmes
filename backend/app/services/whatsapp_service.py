class WhatsAppService:
    """Encapsula WhatsApp Business API (preferencial) ou automação Web controlada."""

    async def find_contact_by_prefix(self, prefix: str) -> str | None:
        # TODO: consultar contatos e procurar nomes contendo prefixo numérico
        # ex.: "420", "CARRO 420"
        return None

    async def send_voucher(self, contact_id: str, filename: str, content: bytes) -> str:
        # TODO: upload/anexo e envio da mídia
        return "provider-message-id"
