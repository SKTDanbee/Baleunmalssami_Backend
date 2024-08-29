from datetime import date
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

class PhoneNumberRequest(BaseModel):
    phone_number: str

class VerifyCodeRequest(BaseModel):
    phone_number: str
    verification_code: str

class FriendRequest(BaseModel):
    friend_id: str

class AcceptFriendRequest(BaseModel):
    friend_id: str

class ReportResponse(BaseModel):
    report_date: date
    child_id: str
    report: Optional[str]
    abuse_count: Optional[int]
    report_type: str

    class Config:
        orm_mode = True