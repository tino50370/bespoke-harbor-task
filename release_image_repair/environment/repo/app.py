from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "release api"}


@app.get("/health")
def health():
    return {"status": "healthy", "service": "release_api"}