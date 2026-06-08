import hashlib

from numpy import block

from models import TransactionCreate, TransactionOut, BlockCreate, BlockOut
from storage import transactions
from datetime import datetime
import random



def create_transaction(transaction: TransactionCreate):
    new_t = {"id": random.randint(10**4, 10**6), "timestamp": datetime.now()}
    new_t.update(transaction.model_dump())
    
    transactions.append(TransactionOut(**new_t))
    return new_t

def get_transactions():
    return transactions



def create_block(block: BlockCreate):
    hash = hashlib.sha256(str(block.model_dump()).encode()).hexdigest()[:8]
    new_b = {"id": random.randint(10**7, 10**9), "timestamp": datetime.now().isoformat(), "hash": hash, "is_mined": True}
    new_b.update(block.model_dump())
    return new_b

# b1 = BlockCreate(previous_hash=" ", transactions_ids=[t.id for t in transactions], miner="Miner1")

# b1_full = create_block(b1)

# b2 = BlockCreate(previous_hash=b1_full["hash"], transactions_ids=[t.id for t in transactions], miner="Miner1")
# b2_full = create_block(b2)