from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def Health():
  return {"status": "ok"}