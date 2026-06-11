from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.web.api.routes import router, repo

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    repo.seed()
    yield
    # shutdown (nothing for now)

app = FastAPI(title="Industrial Asset System V1",lifespan=lifespan)
app.include_router(router)