from fastapi import FastAPI
from app.endpoints.user import router as user_router

app = FastAPI(
    title="Void API",
    description="a long trip",
    version="1.0.0",
)

app.include_router(user_router)


@app.get("/")
def default_root():
    return {"message": "Hello, this is void"}
