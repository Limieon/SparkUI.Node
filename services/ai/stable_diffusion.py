from pydantic import BaseModel

from diffusers import StableDiffusionXLPipeline
from DeepCache import DeepCacheSDHelper


class GenerateImageMeta(BaseModel):
    prompt: str
    negative_prompt: str
    checkpoint: str  # Currently the filename on the server, later the id of the model
    width: int
    height: int
    cfgScale: float
    steps: int
    batchSize: int
    loras: dict[str, float]


async def generateImage(body: GenerateImageMeta):
    pipe = StableDiffusionXLPipeline.from_single_file(
        body.checkpoint, safety_checker=None
    )
    pipe.enable_model_cpu_offload()
    pipe.enable_xformers_memory_efficient_attention()
    pipe.enable_vae_tiling()

    for lora, weight in body.loras.items():
        pipe.load_lora_weights(lora)

    helper = DeepCacheSDHelper(pipe)
    helper.set_params(
        cache_interval=3,
        cache_branch_id=0,
    )
    helper.enable()

    print("Generating image...")
    images = pipe(
        prompt=body.prompt,
        negative_prompt=body.negative_prompt,
        width=body.width,
        height=body.height,
        cfg_scale=body.cfgScale,
        num_images_per_prompt=body.batchSize,
        num_inference_steps=body.steps,
    )
    print("Image generated!")

    helper.disable()

    return images[0]
