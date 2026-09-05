from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:Saikiran12@localhost:5432/fastapi_db"

engine = create_engine(DATABASE_URL)

session = sessionmaker(autoflush=False, autocommit=False, bind=engine)
