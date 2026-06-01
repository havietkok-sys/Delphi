from fastapi import FastAPI
from .data import set_dataset
from fastapi import UploadFile

app = FastAPI()


@app.get("/health")
def Health():
    return {"status": "ok"}


@app.post("/data/upload")
async def upload_data(uploaded_file: UploadFile):
    return {"filename": uploaded_file.filename}
