from sqlalchemy import Column, Float, Integer, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Define Monthly Table
class MonthlySummary(Base):
    __tablename__ = "monthly"
    month = Column(Integer, primary_key=True)
    year = Column(Integer, primary_key=True)
    total_income = Column(Float, default=0)
    total_spending = Column(Float, default=0)

    # Composite primary key (month + year)
    __table_args__ = (
        PrimaryKeyConstraint('month', 'year'),
    )