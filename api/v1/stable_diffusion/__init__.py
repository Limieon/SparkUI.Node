from fastapi import APIRouter
from services.server import handle
from services.generation_queue import generationQueue as queue

from services.generation_queue import GenerationQueue
from services.ai.stable_diffusion import GenerateImageMeta, generateImage

from uuid import uuid4

router = APIRouter(prefix="/api/v1/stable_diffusion")


@router.post("/generate")
async def status(body: GenerateImageMeta):
    print("Generating image...")

    queue.push_back(body)
    images = await generateImage(body)

    for i in images:
        i.save(f"data/images/{uuid4().hex}.png")

    return {"status": "ok"}


@router.get("/queue")
async def status():
    return {"queue": queue.get_queue()}


handle.include_router(router)
