from fastapi import FastAPI
from routes.proproutes import router

app = FastAPI()
app.include_router(router, tags=["CRUD"], prefix="/a")