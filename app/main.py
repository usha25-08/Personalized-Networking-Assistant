from fastapi import FastAPI

from app.routers.conversation import router

app = FastAPI(
    title="Personalized Networking Assistant API",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Personalized Networking Assistant API is running!"
    }