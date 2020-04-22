import json

from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK, HTTP_202_ACCEPTED

from . import models, tasks

app = FastAPI()


@app.post("/search/", status_code=HTTP_202_ACCEPTED)
async def search(query: models.CylleneusQuery):
    result = tasks.search.delay(query.query, [work.json() for work in query.collection])
    return JSONResponse(content={"id": result.id})


@app.get("/status/")
async def status(id: str):
    result = tasks.search.AsyncResult(id)

    return {"status": result.status}


@app.get("/results/", status_code=HTTP_200_OK, response_model=models.CylleneusSearch)
async def results(id: str):
    result = tasks.search.AsyncResult(id)

    if result.ready():
        return json.loads(result.get())


@app.get("/corpus/", status_code=HTTP_200_OK)
async def corpus(c: str):
    result = tasks.corpus(c)
    return JSONResponse(content={c: result})


@app.post("/index/", status_code=HTTP_200_OK)
async def index(source: models.CylleneusSource):
    result = tasks.index(source.corpus, source.filename, source.author, source.title)
    return JSONResponse(content=result)
