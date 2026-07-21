from fastapi import APIRouter, Depends
from database import session_local
from schemas import ResponseRecept, CreateRecept
from models import Recept
from sqlalchemy.orm import Session

route = APIRouter()

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

@route.get("/get_recepts", response_model=list[ResponseRecept])
def get_recepts(db: Session = Depends(get_db)):
    recepts_db = db.query(Recept).all()

    return recepts_db

@route.post("/get_recepts", response_model=ResponseRecept)
def new_recepts(add_recept: CreateRecept, db: Session = Depends(get_db)):
    new_recept = Recept(title=add_recept.title, recept=add_recept.recept)

    db.add(new_recept)
    db.commit()
    db.refresh(new_recept)

    return new_recept
