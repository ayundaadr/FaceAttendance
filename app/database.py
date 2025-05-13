from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

DATABASE_URL = "postgresql://postgres:root@localhost:5432/presensi"

engine = create_engine(DATABASE_URL or "")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
