from collections import defaultdict

from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, Request, status
from app.database import SessionLocal
from app.models import Child, Parent

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(request: Request, db: Session = Depends(get_db)):
    user_id = request.session.get('user_id')
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    user = db.query(Child).filter(Child.id == user_id).first()
    if not user:
        user = db.query(Parent).filter(Parent.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    return user

verification_codes = defaultdict(str)
