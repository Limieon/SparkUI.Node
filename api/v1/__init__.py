from fastapi import APIRouter
from services.server import handle

router = APIRouter(prefix="/api/v1")


@router.get("/status")
async def status():
    return {"status": "ok"}


handle.include_router(router)
