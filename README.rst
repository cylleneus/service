============================
Cylleneus background service
============================

.. image:: https://img.shields.io/badge/cylleneus-next--gen%20corpus%20search%20for%20ancient%20languages-blue.svg
        :target: https://github.com/cylleneus/cylleneus

.. image:: https://travis-ci.org/cylleneus/service.svg?branch=master
    :target: https://travis-ci.org/cylleneus/service

* Free software: Apache Software License 2.0
* Documentation: https://cylleneus.readthedocs.io.


Overview
--------

Cylleneus is a next-generation search engine for electronic corpora of Greek and Latin, which enables texts to be searched on the basis of their semantic and morpho-syntactic properties. This means that, for the first time, texts can be searched by the *meanings* of words as well as by the kinds of grammatical constructions they occur in. Semantic search takes advantage of the `Ancient Greek WordNet <https://greekwordnet.chs.harvard.edu/>`_ and `Latin WordNet <https://latinwordnet.exeter.ac.uk/>`_ and is fully implemented, and thus is available for any annotated or plain-text corpus. However, semantic queries may still be imprecise due to the on-going nature of these two projects. Syntactic search functionality is still under development and is available for only certain structured corpora.  Morphological searching and query filtering will work with any Latin corpus, and any Greek corpus with sufficient morhological annotation.


Installation
------------

Clone this repository and then ``$ python setup.py install``. The service uses Celery as the asynchronous task runner, RabbitMQ as message broker and Redis as result store.


Running
-------

Start up Celery, the RabbitMQ server, and the FastAPI server using Uvicorn, or preferably Gunicorn managing Uvicorn.

``$ sudo rabbitmq-server start``
``$ celery -A service.tasks worker --loglevel=INFO --concurrency=4``
``$ gunicorn -k uvicorn.workers.UvicornWorker service.main:app``

Usage
-----

Submit search queries as POST requests to ``http://127.0.0.1:8000/search`` with the JSON body of the request in the format: e.g.,

``
{
    "query": "<habeo>",
    "collection": [
                    { "corpus": "agldt", "docix": [0] }
                  ]
}
``

This will return a JSON object with the key ``id``, whose value is the unique identifier of the search task.

You can check the status of a search running in the background with a GET request to ``http://127.0.0.1:8000/status?id=<id>``, where <id> is the unique identifier of the required search task.

If the result is ``SUCCESS``, then it will be possible to obtain the search results again through a GET request to ``http://127.0.0.1:8000/results?id=<id>``, where <id> is the unique identifier of the successfully completed task.

In addition, you can obtain a listing of the available corpora by GET request to ``http://127.0.0.1:8000/corpus?c=<name>``, where <name> is the name of the relevant corpus.

Locally-stored files can be indexed in the background through a POST request to ``http://127.0.0.1:8000/index`` with a JSON body providing the following data:

``
{
    "corpus": str,      # corpus name
    "filename": str,    # path to file
    "author": str,      # optional
    "title": str        # optional
}
``

Credits
-------

© 2019 William Michael Short.
