from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.crud import accept_friend_request, send_friend_request, get_friend_ranking
from app.dependencies import get_db, get_current_user
from app.models import Child, Friend, FriendStatus
from app.schemas import FriendRequest, AcceptFriendRequest

router = APIRouter()

@router.post("/send_friend_request/")
def send_friend_request_endpoint(request: FriendRequest, db: Session = Depends(get_db), current_user: Child = Depends(get_current_user)):
    friend = db.query(Child).filter(Child.id == request.friend_id).first()
    if not friend:
        raise HTTPException(status_code=404, detail="Child not found")
    if db.query(Friend).filter(Friend.child_id == current_user.id, Friend.friend_id == request.friend_id).first():
        raise HTTPException(status_code=400, detail="Friend request already sent")
    send_friend_request(db, current_user, request.friend_id)
    return {"message": "Friend request sent successfully"}

@router.post("/accept_friend_request/")
def accept_friend_request_endpoint(request: AcceptFriendRequest, db: Session = Depends(get_db), current_user: Child = Depends(get_current_user)):
    friend_request = db.query(Friend).filter(Friend.child_id == request.friend_id, Friend.friend_id == current_user.id, Friend.status == FriendStatus.pending).first()
    if not friend_request:
        raise HTTPException(status_code=404, detail="Friend request not found")
    accept_friend_request(db, friend_request)
    return {"message": "Friend request accepted successfully"}

@router.get("/pending_friend_requests/")
def pending_friend_requests(db: Session = Depends(get_db), current_user: Child = Depends(get_current_user)):
    pending_requests = db.query(Friend).filter(Friend.friend_id == current_user.id, Friend.status == FriendStatus.pending).all()
    return pending_requests

@router.get("/friend_ranking/")
def get_friend_ranking_endpoint(db: Session = Depends(get_db), current_user: Child = Depends(get_current_user)):
    ranking_results = get_friend_ranking(db, current_user)
    return ranking_results