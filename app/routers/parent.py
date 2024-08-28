from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import ParentIn
from app.dependencies import get_db, verification_codes
from app.crud import create_parent, link_child_to_parent
from app.models import Parent, Child
from app.utils.sms import generate_verification_code

router = APIRouter()

@router.post("/signup")
def create_parent_with_verification(parent: ParentIn, db: Session = Depends(get_db)):
    stored_code = verification_codes.get(parent.phone_number)
    if stored_code is None or stored_code != parent.verification_code:
        raise HTTPException(status_code=400, detail="Invalid verification code")

    db_parent = Parent(
        id=parent.id,
        password=parent.password,
        name=parent.name,
        phone_number=parent.phone_number,
    )
    create_parent(db, db_parent)

    child = db.query(Child).filter(Child.parent_phone_number == parent.phone_number).first()
    if not child:
        raise HTTPException(status_code=404, detail="Child not found")

    link_child_to_parent(db, child, db_parent)
    return {"message": "Parent created and linked to child successfully."}

