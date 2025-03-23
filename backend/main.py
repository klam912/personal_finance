from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, PrimaryKeyConstraint
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from datetime import date
from tables import *

# Note:
# FastAPI: web framework for building APIs 
# SQLAlchemy: database interaction

# Establish database connection
DATABASE_URL = "sqlite:///../db/finance_tracker.db"

# Establish a connection with the database
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create database sessions so queries can be executed
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class to define database models
Base = declarative_base()

# ------------------------------
# Initialize the FastAPI application
app = FastAPI()

# Create and manage the database sessions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#------------------------------
# API Endpoints
@app.post("/transactions/")
# Use async to allow this function run in the background
async def create_transaction(transaction: Transaction):
    return {"message": "Transaction added sccuessfully", "transaction": transaction}

@app.get("/summary/daily/{date}")
def get_daily_summary(date: date, db: Session = Depends(get_db)):
    # Query the date summary
    summary = db.query(DailySummary).filter(DailySummary.date == date).first()
    
    # Handles if none exist
    if not summary:
        raise HTTPException(status_code=404, detail="No summary found for this date")
    return summary

@app.get("/summary/weekly/{week}/{year}")
def get_weekly_summary(week: int, year: int, db: Session = Depends(get_db)):
    # Query summary for a given week and year
    summary = db.query(WeeklySummary).filter(WeeklySummary.week == week, WeeklySummary.year == year).first()

    # Handles if none exist
    if not summary:
        raise HTTPException(status_code=404, detail="No summary found for this week")
    return summary

@app.get("/summary/monthly/{month}/{year}")
def get_monthly_summary(month: int, year: int, db: Session = Depends(get_db)):
    # Query summary for a given month and year
    summary = db.query(MonthlySummary).filter(MonthlySummary.month == month, MonthlySummary.year == year).first()

    # Handles if none exist
    if not summary:
        raise HTTPException(status_code=404, detail="No summary found for this month")
    return summary
#------------------------------