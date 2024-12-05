import env
from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

handle = FastAPI()


# Middlewares
@handle.middleware("http")
async def authentication(req: Request, next):
    if not "Authorization" in req.headers:
        return JSONResponse(status_code=401, content={"error": "Unauthorized"})

    header = req.headers.get("Authorization")

    [token_type, token] = header.split(" ") if header else [None, None]
    if token_type == "Bearer" and token == env.SPARKUI_NODE_SECRET_KEY:
        return await next(req)

    return JSONResponse(status_code=401, content={"error": "Unauthorized"})


async def run_server():
    import uvicorn
    import env

    server = uvicorn.Server(
        config=uvicorn.Config(
            handle, host=env.SPARKUI_NODE_HOST, port=env.SPARKUI_NODE_PORT
        )
    )
    await server.serve()
