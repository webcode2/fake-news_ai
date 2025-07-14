from fastapi import FastAPI

from src.config.setting import settings
from src.routes import authRoute, messageRoute


app = FastAPI(
    title=settings.app_name,
    debug=settings.debug
)


app.include_router(authRoute.router)
app.include_router(messageRoute.router)


@app.get("/")
async def home():
    return {"message": "welcome tofake new backend"}
