from fastapi import FastAPI
from pydantic import BaseModel
from src.predict import predict_news

app = FastAPI()

class News(BaseModel):
    text: str

@app.post("/predict")
def predict(news: News):
    return {"result": predict_news(news.text)}