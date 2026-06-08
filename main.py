# crypto_ledger/main.py
from fastapi import FastAPI, HTTPException, status
from typing import List, Optional

# Импортируем наши модули (пока будут пустыми, но мы их заполним)
import models
import crud # Будет использоваться позже
import uvicorn
import dotenv
import os   

dotenv.load_dotenv()
DEV = os.environ["DEV"] = os.getenv("DEV")


app = FastAPI(title="CryptoLedger API")

#  Главный маршрут
@app.get("/", summary="Приветствие API", response_description="Сообщение с приветствием")
def read_root():
    return {"message": "Добро пожаловать в CryptoLedger API!"}

@app.post("/transactions/", summary="Создать транзакцию", response_description="Созданная транзакция")
def create_transaction(transaction: models.TransactionCreate):
    ans = crud.create_transaction(transaction)
    ans.update({"message": "Транзакция успешно создана!"})
    return ans

@app.get("/transactions/", summary="Получить все транзакции", response_description="Список всех транзакций")
def get_transactions():
    return crud.get_transactions()

@app.post("/blocks/", summary="Создать блок", response_description="Созданный блок")
def create_block(block: models.BlockCreate):
    ans = crud.create_block(block)
    ans.update({"message": "Блок успешно создан!"})
    return ans


if __name__ == "__main__":
    if not DEV:
        print("Запуск в продакшн режиме")
        uvicorn.run(app, host="0.0.0.0", port=8000)
    
    