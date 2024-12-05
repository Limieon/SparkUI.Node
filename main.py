from fastapi import FastAPI
from services.server import run_server

# Import API routers
import api.v1
import api.v1.stable_diffusion


async def main():
    await run_server()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
