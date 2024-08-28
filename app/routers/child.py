from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import ChildIn
from app.dependencies import get_db, verification_codes
from app.crud import create_child
from app.utils.sms import generate_verification_code, send_sms
from app.models import Child

router = APIRouter()

@router.post("/signup")
def create_child_endpoint(child: ChildIn, db: Session = Depends(get_db)):
    verification_code = generate_verification_code()

    verification_codes[child.parent_phone_number] = verification_code

    send_sms(
        to=child.parent_phone_number,
        from_="01012345678",
        text=f"바른말싸미 부모-자녀 연동 인증번호는 {verification_code}입니다.",
    )

    db_child = Child(
        id=child.id,
        password=child.password,
        name=child.name,
        parent_phone_number=child.parent_phone_number,
    )

    create_child(db, db_child)
    return {"message": "Child created successfully. Verification code sent to parent."}
