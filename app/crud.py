import hashlib
import hmac
from datetime import datetime, timedelta
from http.client import HTTPException
from typing import Optional

from fastapi import Depends
from jose import JWTError

from app.database import SessionLocal
from app.models import Report, Child
from sqlalchemy.orm import Session

from app.schemas import TokenData

#db 세션
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_report(db: Session, report_id: int):
    return db.query(Report).filter(Report.id == report_id).first()

#최근 6주간 리포트 그래프 생성
def get_last_6_weeks_graph(db: Session):
    return db.query(Report).order_by(Report.report_date.desc()).limit(6).all()

# 리포트 리스트 조회
def get_reports(db: Session):
    return db.query(Report).order_by(Report.report_date.desc()).all()

# 문자 메시지 인증 signature 생성
def generate_signature(api_secret, date_time, salt):
    data = date_time + salt
    signature = hmac.new(api_secret.encode('utf-8'), data.encode('utf-8'), hashlib.sha256).hexdigest()
    return signature