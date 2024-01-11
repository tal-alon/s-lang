from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel

from s_lang import run

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RunParams(BaseModel):
    code: str
    inputs: list[int]


class RunResult(BaseModel):
    output: int
    error: str | None = None


@app.get("/")
async def root():
    return "OK"


@app.post("/run")
async def _run(params: RunParams) -> RunResult:
    try:
        return RunResult(
            output=run(params.code, params.inputs)
        )
    except Exception as err:
        return RunResult(
            output=-1,
            error=str(err)
        )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
