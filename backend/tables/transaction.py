from pydantic import BaseModel
from sqlalchemy import Column, Float, Integer, Date, String
from pydantic import BaseModel

# Define Transaction table
class Transaction(BaseModel):
    date: str
    trans_type: str
    category: str
    amount: float

    class Config:
        orm_mode = True 
