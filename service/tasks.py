import json
from pathlib import Path

from celery import Celery

from cylleneus.corpus import Corpus, Work
from cylleneus.search import Searcher, Collection
from cylleneus.settings import DEFAULT_CORPUS

# Create the app and set the broker location
Cylleneus = Celery(
    "cylleneus", backend="redis://localhost", broker="pyamqp://guest@localhost//",
)


@Cylleneus.task
def search(q, collection=None):
    if collection:
        works = [json.loads(item) for item in collection]
        c = Collection(
            works=[
                Corpus(work["corpus"]).work_by_docix(work["docix"][0]) for work in works
            ]
        )
    else:
        c = Collection(Corpus(DEFAULT_CORPUS).works)
    searcher = Searcher(c)
    s = searcher.search(q)
    return s.to_json()


@Cylleneus.task
def manifest(corpus):
    c = Corpus(corpus)
    return c.manifest


@Cylleneus.task
def index(corpus, filename):
    c = Corpus(corpus)

    w = Work(corpus=c)
    docix = w.indexer.from_file(Path(filename), destructive=True, optimize=True)

    return {
        "corpus": corpus,
        "docix": docix,
        "filename": filename,
        "author": w.author,
        "title": w.title,
    }
