from typing import Optional

from pydantic import BaseModel

class ChildCreate(BaseModel):
    id: str
    password: str
    name: str
    parent_phone_number: str


class ParentCreateWithCode(BaseModel):
    id: str
    password: str
    name: str
    phone_number: str
    verification_code: str

class ChildIn(BaseModel):
    id: str
    password: str
    name: str

class ChildOut(BaseModel):
    id: str
    name: str

class TokenData(BaseModel):
    username: Optional[str] = None