from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./cook.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()