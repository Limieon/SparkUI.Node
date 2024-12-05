from fastapi import FastAPI

app = FastAPI()


@app.get("/status")
async def status():
    return {"status": "ok"}


async def main():
    import uvicorn
    import env

    server = uvicorn.Server(
        config=uvicorn.Config(
            app, host=env.SPARKUI_NODE_HOST, port=env.SPARKUI_NODE_PORT
        )
    )
    await server.serve()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
