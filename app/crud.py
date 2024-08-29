from collections import defaultdict

from sqlalchemy.orm import Session
from app.models import Report, Child, Parent, Friend, FriendStatus


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

def get_reports(db: Session):
    return db.query(Report).order_by(Report.report_date.desc()).all()

def send_friend_request(db: Session, current_user: Child, friend_id: str):
    new_friend_request = Friend(child_id=current_user.id, friend_id=friend_id)
    db.add(new_friend_request)
    db.commit()
    return new_friend_request

def accept_friend_request(db: Session, friend_request: Friend):
    friend_request.status = FriendStatus.accepted
    db.commit()
    return friend_request

def get_friend_ranking(db: Session, current_user: Child):
    friends = db.query(Friend).filter(Friend.child_id == current_user.id, Friend.status == FriendStatus.accepted).all()
    friend_ids = [friend.friend_id for friend in friends]
    friend_ids.append(current_user.id)

    reports = db.query(Report).filter(Report.child_id.in_(friend_ids)).all()
    reports_by_date = defaultdict(list)
    for report in reports:
        reports_by_date[report.report_date].append(report)

    ranking_results = {}
    for report_date, reports in sorted(reports_by_date.items(), reverse=True):
        sorted_reports = sorted(reports, key=lambda r: r.abuse_count)
        ranking_results[report_date] = [
            {"rank": idx + 1, "child_id": report.child_id, "abuse_count": report.abuse_count}
            for idx, report in enumerate(sorted_reports)
        ]

    return ranking_results