from sqlalchemy import Column, String, Integer, Text
from database import Base

class Recept(Base):
    __tablename__ = "recepts"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    recept = Column(Text)