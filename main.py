from fastapi import FastAPI
from routes.evaluate import router as eval_router

app = FastAPI()

app.include_router(eval_router)

@app.get("/")
def home():
    return {"message": "TenderIQ running"}