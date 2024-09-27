from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

class NumberRequest(BaseModel):
    number: int


@app.get("/")
async def home():
    return {
        "node": "node_name",
        "ip": "node_ip"
    }

@app.post("/multiply")
async def multiply(request: NumberRequest) -> Dict[int, int]:
    number = request.number
    multiplication_table = {i: number * i for i in range(1, 11)}
    return multiplication_table
