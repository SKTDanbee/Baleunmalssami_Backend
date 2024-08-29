from datetime import datetime
from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

from app import models
from app.crud import get_reports
from app.dependencies import get_db, get_current_user
from app.models import Child, Report, Parent
from app.schemas import ReportResponse

router = APIRouter()

@router.post("/create_txt/")
def create_txt(report_text: str, child_id: str, db: Session = Depends(get_db)):
    db_txt = models.Txt(date=datetime.utcnow(), report_text=report_text, child_id=child_id)
    db.add(db_txt)
    db.commit()
    return db_txt

@router.get("/reports/", response_model=List[ReportResponse])
async def read_all_reports(db: Session = Depends(get_db), current_user: Child = Depends(get_current_user)):
    reports = get_reports(db)
    if not reports:
        raise HTTPException(status_code=404, detail="No reports found")
    return reports

@router.get("/reports/type1/", response_model=List[ReportResponse])
async def get_reports_type1(db: Session = Depends(get_db), current_user: Parent = Depends(get_current_user)):
    # 자녀 ID 목록 가져오기
    child_ids = [child.id for child in current_user.children]

    # 자녀의 리포트 조회
    reports = db.query(Report).filter(Report.child_id.in_(child_ids), Report.report_type == '1').order_by(
        Report.report_date.desc()).all()

    if not reports:
        raise HTTPException(status_code=404, detail="No reports found for report_type '1' for the current user's children")

    return reports


# 엔드포인트 2: 현재 로그인된 사용자에 대해 report_type = '2' 인 리포트 조회
@app.get("/reports/type2/", response_model=List[ReportResponse])
async def get_reports_type2(db: Session = Depends(get_db), current_user: Child = Depends(get_current_user)):
    reports = db.query(Report).filter(Report.child_id == current_user.id, Report.report_type == '2').order_by(
        Report.report_date.desc()).all()

    if not reports:
        raise HTTPException(status_code=404, detail="No reports found for report_type '2' for the current user")

    return reports


# 엔드포인트 3: 현재 로그인된 사용자(부모)의 자녀의 report_type = '3' 인 리포트 조회
@app.get("/reports/type3/", response_model=List[ReportResponse])
async def get_reports_type3(db: Session = Depends(get_db), current_user: Parent = Depends(get_current_user)):
    # 자녀 ID 목록 가져오기
    child_ids = [child.id for child in current_user.children]

    # 자녀의 리포트 조회
    reports = db.query(Report).filter(Report.child_id.in_(child_ids), Report.report_type == '3').order_by(
        Report.report_date.desc()).all()

    if not reports:
        raise HTTPException(status_code=404, detail="No reports found for report_type '3' for the current user's children")

    return reports