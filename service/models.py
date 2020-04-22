from typing import List

from pydantic import BaseModel


class CylleneusSource(BaseModel):
    corpus: str
    filename: str
    author: str = None
    title: str = None


class CylleneusWork(BaseModel):
    corpus: str
    docix: List[int]


class CylleneusQuery(BaseModel):
    query: str
    collection: List[CylleneusWork] = None


class CylleneusResult(BaseModel):
    corpus: str
    author: str
    title: str
    urn: str
    reference: str
    text: str


class CylleneusSearch(BaseModel):
    query: str
    collection: List[CylleneusWork]
    minscore: int = None
    top: int
    start_time: str
    end_time: str
    maxchars: int
    surround: int
    count: List[int]
    results: List[CylleneusResult]
