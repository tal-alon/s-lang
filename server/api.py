from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel

from s_lang import run

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RunParams(BaseModel):
    code: str
    inputs: list[int]


@app.get("/")
async def root():
    return "OK"


@app.post("/run")
async def _run(params: RunParams):
    return run(params.code, params.inputs)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
