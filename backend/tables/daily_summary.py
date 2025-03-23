from sqlalchemy import Column, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Define Daily Table
class DailySummary(Base):
    __tablename__ = "daily"
    date = Column(Date, primary_key=True)
    total_income = Column(Float, default=0)
    total_spending = Column(Float, default=0)