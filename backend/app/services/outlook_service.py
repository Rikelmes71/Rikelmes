from dataclasses import dataclass


@dataclass
class ParsedReserveEmail:
    message_id: str
    guest_name: str
    reserve_order_number: str
    voucher_bytes: bytes
    voucher_filename: str


class OutlookService:
    """Integração Microsoft Graph (stub inicial)."""

    async def fetch_unprocessed_reserve_messages(self, user_id: str) -> list[ParsedReserveEmail]:
        # TODO: implementar Graph subscriptions/webhook e fallback polling
        return []

    async def parse_reserve_message(self, raw_message: dict) -> ParsedReserveEmail:
        # TODO: parser robusto por regex + NLP leve + leitura de anexo
        return ParsedReserveEmail(
            message_id=raw_message["id"],
            guest_name=raw_message.get("guest_name", ""),
            reserve_order_number=raw_message.get("order", ""),
            voucher_bytes=b"",
            voucher_filename="voucher.pdf",
        )
