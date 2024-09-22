import uvicorn
import asyncio
from fastapi import FastAPI

from src.routers import user_router
from src.db.db_config import init_db

app = FastAPI()


app.include_router(user_router.router, prefix="/user", tags=["user"])



if __name__ == "__main__":
    asyncio.run(init_db)
    uvicorn.run("main:app", host="localhost", reload=True)