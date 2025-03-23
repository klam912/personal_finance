from sqlalchemy import Column, Float, Integer, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Define Weekly Table
class WeeklySummary(Base):
    __tablename__ = "weekly"
    week = Column(Integer, primary_key=True)
    year = Column(Integer, primary_key=True)
    month = Column(Integer)
    total_income = Column(Float, default=0)
    total_spending = Column(Float, default=0)

    # Composite primary key (week + year)
    __table_args__ = (
        PrimaryKeyConstraint('week', 'year'),
    )

