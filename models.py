# crypto_ledger/models.py
from pydantic import BaseModel, Field
from typing import Optional
import datetime

# Модель для транзакции
class TransactionBase(BaseModel):
    sender: str
    recipient: str
    amount: float 

class TransactionCreate(TransactionBase):
    pass # Для создания достаточно базовых полей

class TransactionOut(TransactionBase):
    id: int
    timestamp: datetime.datetime

# Модель для блока
class BlockBase(BaseModel):
    previous_hash: str 
    transactions_count: int 
    miner: str 

class BlockCreate(BlockBase):
    pass # Для создания достаточно базовых полей

class BlockOut(BlockBase):
    id: int
    hash: str # Хэш этого блока (упрощенный)
    timestamp: datetime.datetime
    is_mined: bool # Флаг, показывающий, что блок "подтвержден"