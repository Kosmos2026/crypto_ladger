# crypto_ledger/main.py
from fastapi import FastAPI, HTTPException, status
from typing import List, Optional

# Импортируем наши модули (пока будут пустыми, но мы их заполним)
import models
import crud # Будет использоваться позже
import uvicorn

app = FastAPI(title="CryptoLedger API")

#  Главный маршрут
@app.get("/", summary="Приветствие API", response_description="Сообщение с приветствием")
def read_root():
    return {"message": "Добро пожаловать в CryptoLedger API!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)