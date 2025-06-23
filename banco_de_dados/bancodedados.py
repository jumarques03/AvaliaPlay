import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()  

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)    # Responsável pela conexão entre minha API e o banco de dados
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()   # Cria a base do banco de dados


