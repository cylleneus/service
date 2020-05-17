import uvicorn

from .main import app


def run():
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        log_level="info",
        workers=4,
        reload=True,
    )


if __name__ == "__main__":
    run()
