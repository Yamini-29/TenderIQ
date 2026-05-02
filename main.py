from fastapi import FastAPI
from routes import upload, evaluate

app = FastAPI(title="TenderIQ API")

app.include_router(upload.router)
app.include_router(evaluate.router)

@app.get("/")
def home():
    return {"message": "TenderIQ Backend Running"}