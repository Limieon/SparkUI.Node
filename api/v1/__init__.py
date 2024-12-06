import platform

from fastapi import APIRouter, WebSocket
from services.server import handle
from services.socket_handler import socketHandler
from services.sys_info import get_system_info

router = APIRouter(prefix="/api/v1")


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


@router.get("/info")
async def info():
    return get_system_info()


@router.get("/status")
async def status():
    return {"status": "ok"}


handle.include_router(router)
