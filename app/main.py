from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"meggage": "Hello World- This is my first sample hello world app and trigger the CI/CD action on GCP Cloud Build and deploy on cloud run"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
