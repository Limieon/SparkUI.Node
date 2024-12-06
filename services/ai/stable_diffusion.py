from pydantic import BaseModel

from diffusers import StableDiffusionPipeline


class GenerateImageMeta(BaseModel):
    prompt: str


async def generateImage(body: GenerateImageMeta):
    pass
