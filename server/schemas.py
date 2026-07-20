from pydantic import BaseModel

class CreateRecept(BaseModel):
    title: str
    recept: str

class ResponseRecept(BaseModel):
    id: int
    title: str
    recept: str

    class Config:
        from_attributes = True
