from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DB_url = os.getenv('DB_URL')

try:
    engine = create_engine(DB_url, pool_recycle= 500, echo=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
    print("DB 연결 성공")
except Exception as e:
    print("DB 연결 실패")
    print(e)