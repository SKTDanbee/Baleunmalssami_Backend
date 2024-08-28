from sqlalchemy.orm import Session
from app.models import Report, Child, Parent


def create_parent(db: Session, parent: Parent):
    db.add(parent)
    db.commit()
    db.refresh(parent)
    return parent

def link_child_to_parent(db: Session, child: Child, parent: Parent):
    child.parent_id = parent.id
    db.commit()
    return child

def create_child(db: Session, child: Child):
    db.add(child)
    db.commit()
    db.refresh(child)
    return child

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(Child).filter(Child.id == username).first()
    if user and user.password == password:
        return user
    user = db.query(Parent).filter(Parent.id == username).first()
    if user and user.password == password:
        return user
    return None