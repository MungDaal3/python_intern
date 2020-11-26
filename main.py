from fastapi import FastAPI
from app import is_alive_host

app = FastAPI()


@app.get("/health")
def read_item(hostname: str):
    if is_alive_host(hostname) is True:
        return {"status": "up"}
    else:
        return {"status": "down"}
