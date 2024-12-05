from fastapi import APIRouter, WebSocket
from services.server import handle
from services.socket_handler import socketHandler

router = APIRouter(prefix="/api/v1")


@router.get("/status")
async def status():
    return {"status": "ok"}


@router.websocket("/ws")
async def websocket(socket: WebSocket):
    connection_id = await socketHandler.connect(socket)
    try:
        while True:
            data = await socket.receive_text()
            await socketHandler.broadcast("echo", data)
    except Exception as e:
        print(e)
    finally:
        await socketHandler.disconnect(connection_id)


handle.include_router(router)
