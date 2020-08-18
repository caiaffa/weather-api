from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from app.api.v1.api import api_router
from app.core.config import settings
from app import exceptions

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1}/openapi.json"
)

if settings.CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1)


@app.exception_handler(exceptions.CelerySendTaskException)
async def unicorn_exception_handler(request: Request, exc: exceptions.CelerySendTaskException):
    return JSONResponse(
        status_code=400,
        content={"message": f"An error occurred while sending to the queue: {exc}"},
    )
