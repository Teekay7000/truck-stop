from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine =  create_engine(DATABASE_URL)

#sessionmaker: Creates database sessions for performing database operations.
#SessionLocal: A factory for creating individual database sessions.
SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind =  engine
)
#The foundation for defining Python database models (tables).
Base = declarative_base()
