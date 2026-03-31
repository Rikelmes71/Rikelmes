from fastapi import APIRouter

from app.schemas.common import MessageResponse

router = APIRouter()


@router.get("/dashboard")
def dashboard() -> dict:
    return {
        "status": "running",
        "last_deliveries": [],
        "manual_queue": 0,
    }


@router.get("/logs")
def logs() -> dict:
    return {"items": []}


@router.post("/manual/send", response_model=MessageResponse)
def manual_send() -> MessageResponse:
    return MessageResponse(message="Envio manual enfileirado")


@router.get("/integrations")
def integrations() -> dict:
    return {
        "outlook": False,
        "reserve": False,
        "spreadsheet": False,
        "whatsapp": True,
    }
