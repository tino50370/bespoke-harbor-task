from fastapi import FastAPI

from service.settings import SERVICE_NAME, STATUS_VALUE, VERSION

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "release api"}


@app.get("/health")
def health():
    return {"status": STATUS_VALUE, "service": SERVICE_NAME}


@app.get("/version")
def version():
    return {"version": VERSION}