from fastapi import FastAPI
from .data import set_dataset, get_dataset
from fastapi import UploadFile, HTTPException
import pandas as pd
from .schemas import AskRequest, AskResponse
from .llm import ask_model
from .chain.pipeline import pipeline
from .chain.steps import PromptInput

app = FastAPI()


@app.get("/health")
def Health():
    return {"status": "ok"}


@app.post("/data/upload")
async def upload_data(uploaded_file: UploadFile):
    if not uploaded_file.filename.endswith(".csv"):

        raise HTTPException(status_code=400, detail="only csv files allowed")

    df = pd.read_csv(uploaded_file.file)

    set_dataset(df)

    return {
        "rows": len(df),
        "columns": list(df.columns),
        "dtypes": {column: str(dtype) for column, dtype in df.dtypes.items()},
    }


@app.get("/data/stats")
def get_stats():

    df = get_dataset()

    if df is None:
        raise HTTPException(status_code=404, detail="No dataset loaded")

    return df.describe().to_dict()


@app.post("/ai/ask")
def ask_ai(request: AskRequest):

    return pipeline.invoke(
        PromptInput(
            question=request.question
        )
    )
