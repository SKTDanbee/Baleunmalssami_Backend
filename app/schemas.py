from typing import Optional

from pydantic import BaseModel


class ChildIn(BaseModel):
    id: str
    password: str
    name: str
    parent_phone_number: str

class ParentIn(BaseModel):
    id: str
    password: str
    name: str
    phone_number: str
    verification_code: str


class Token(BaseModel):
    access_token: str
    token_type: str
    username: str