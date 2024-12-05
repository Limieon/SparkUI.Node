from fastapi import APIRouter
from services.server import handle

from services.generation_queue import GenerationQueue, GenerationRequest

router = APIRouter(prefix="/api/v1/stable_diffusion")

queue = GenerationQueue()


@router.post("/generate")
async def status(body: GenerationRequest):
    print("Generating image...")

    queue.push_back(body)

    return {"status": "ok"}


@router.get("/queue")
async def status():
    return {"queue": queue.get_queue()}


handle.include_router(router)
