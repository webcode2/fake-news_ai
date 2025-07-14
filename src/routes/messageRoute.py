from fastapi import APIRouter
from src.db.schemas.messageSchema import MessageRequest

router = APIRouter()


@router.get("/messages")
async def get_messages():
    return {"messages": ["Hello", "World"]}


@router.post("/messages")
async def create_message(request: MessageRequest):
    # Here you could process or store the message
    return {"received_message": request.message}
