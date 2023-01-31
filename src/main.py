from fastapi import FastAPI
from src.rooters import root

api = FastAPI()

routers = [
    root.router
]

for router in routers:
    api.include_router(router)

@api.get("/")
def read_root():
    return {"Hello": "World"}