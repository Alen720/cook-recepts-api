from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine, session_local, Base
from models import Recept
from schemas import ResponseRecept, CreateRecept

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/get_recepts")
def get_recepts(db: Session = Depends(get_db)):
    recepts_db = db.query(Recept).all()

    return recepts_db

@app.post("/get_recepts")
def new_recepts(add_recept: CreateRecept, db: Session = Depends(get_db)):
    new_recept = Recept(title=add_recept.title, recept=add_recept.recept)

    db.add(new_recept)
    db.commit()
    db.refresh(new_recept)

    return new_recept