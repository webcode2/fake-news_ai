from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.services.sentiment_service import SentimentService
from src.config.setting import settings
from src.routes import authRoute, messageRoute


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize sentiment service
    app.state.sentiment_service = SentimentService()
    yield
    # Optional: Cleanup logic here

app = FastAPI(lifespan=lifespan, title=settings.PROJECT_NAME,
              version=settings.VERSION)
# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(authRoute.router)
app.include_router(messageRoute.router)


@app.get("/")
async def home():
    return {"message": "welcome tofake new backend"}
