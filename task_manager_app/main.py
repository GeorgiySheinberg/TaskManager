from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from api import router as api_router
from core.config import settings
from core.models import db_runner
from fastapi.responses import ORJSONResponse

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_runner.dispose()


main_app = FastAPI(
    default_response_class=ORJSONResponse,
    lifespan=lifespan,

)

main_app.include_router(
    api_router,
    prefix=settings.api.api_prefix
)


if __name__ == "__main__":
    uvicorn.run("main:main_app",
                host=settings.run.host,
                port=settings.run.port,
                reload=True
                )