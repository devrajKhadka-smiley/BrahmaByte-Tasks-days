from fastapi import FastAPI
from .user import router as user_route

app = FastAPI()

app.include_router(user_route)

# if __name__=="__main__":
#     import uvicorn
#     uvicorn.run("main:app",port=8001)