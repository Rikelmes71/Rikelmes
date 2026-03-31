import asyncio

from app.services.outlook_service import OutlookService
from app.services.automation_orchestrator import AutomationOrchestrator


async def run() -> None:
    outlook = OutlookService()
    orchestrator = AutomationOrchestrator()

    while True:
        # TODO: iterar usuários ativos (4 acessos internos)
        messages = await outlook.fetch_unprocessed_reserve_messages(user_id="system")
        for parsed in messages:
            await orchestrator.process_reserve_email(parsed)
        await asyncio.sleep(30)


if __name__ == "__main__":
    asyncio.run(run())
