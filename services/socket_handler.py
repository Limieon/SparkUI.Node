import json

from dataclasses import dataclass
from fastapi import WebSocket
from uuid import uuid4


@dataclass
class SocketConnection:
    socket: WebSocket
    id: str = uuid4().hex


class SocketHandler:
    def __init__(self):
        self.clients = dict[str, SocketConnection]()

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        connection = SocketConnection(socket=websocket)
        print(f"Socket connected {connection.id}")
        self.clients[connection.id] = connection
        return connection.id

    async def disconnect(self, connection_id: str):
        print(f"Socket disconnected {connection_id}")
        del self.clients[connection_id]

    async def broadcast(self, type: str, data: dict | str):
        for connection in self.clients.values():
            await connection.socket.send_json({"type": type, "data": data})

    async def send(self, connection_id: str, type: str, data: dict | str):
        connection = self.clients[connection_id]
        if not connection:
            return

        await connection.socket.send_json({"type": type, "data": data})

    sockets: dict[str, SocketConnection] = {}


socketHandler = SocketHandler()
