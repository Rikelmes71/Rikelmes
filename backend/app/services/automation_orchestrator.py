from app.services.outlook_service import ParsedReserveEmail
from app.services.spreadsheet_service import SpreadsheetService
from app.services.whatsapp_service import WhatsAppService
from app.services.audit_service import AuditService


class AutomationOrchestrator:
    def __init__(self) -> None:
        self.spreadsheet = SpreadsheetService()
        self.whatsapp = WhatsAppService()
        self.audit = AuditService()

    async def process_reserve_email(self, parsed: ParsedReserveEmail) -> dict:
        match = await self.spreadsheet.find_driver_by_plan_or_observation(
            plan=parsed.reserve_order_number,
            guest_name=parsed.guest_name,
        )
        if not match:
            self.audit.log(
                "NOT_FOUND_SHEET",
                {
                    "message_id": parsed.message_id,
                    "reserve_order_number": parsed.reserve_order_number,
                    "guest_name": parsed.guest_name,
                },
            )
            return {"status": "MANUAL_REQUIRED", "reason": "NOT_FOUND_SHEET"}

        contact = await self.whatsapp.find_contact_by_prefix(match.car_prefix)
        if not contact:
            self.audit.log(
                "NOT_FOUND_PREFIX",
                {"message_id": parsed.message_id, "car_prefix": match.car_prefix},
            )
            return {"status": "MANUAL_REQUIRED", "reason": "NOT_FOUND_PREFIX"}

        provider_id = await self.whatsapp.send_voucher(
            contact_id=contact,
            filename=parsed.voucher_filename,
            content=parsed.voucher_bytes,
        )

        self.audit.log(
            "VOUCHER_SENT",
            {
                "message_id": parsed.message_id,
                "car_prefix": match.car_prefix,
                "contact": contact,
                "provider_message_id": provider_id,
            },
        )
        return {"status": "SENT", "provider_message_id": provider_id}
