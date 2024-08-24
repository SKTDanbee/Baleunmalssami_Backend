from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from app.database import Base


class Child(Base):
    __tablename__ = 'child'

    id = Column(String(255), primary_key=True)
    password = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    parent_phone_number = Column(String(255), nullable=True)
    is_verified = Column(Boolean, default=False)
    parent_id = Column(String(255), ForeignKey('parent.id'))
    parent = relationship('Parent', back_populates='children')


class Parent(Base):
    __tablename__ = 'parent'

    id = Column(String(255), primary_key=True)
    password = Column(String(255), nullable=True)
    name = Column(String(255), nullable=True)
    phone_number = Column(String(255),unique=True, nullable=True)
    verification_code = Column(String(255), nullable=True)
    children = relationship('Child', back_populates='parent')

class Report(Base):
    __tablename__ = 'report'

    id = Column(Integer, primary_key=True)
    report_date = Column(DateTime, nullable=False)
    report = Column(Text, nullable=False)
    child_id = Column(String(255), nullable=False)
    abuse_count = Column(Integer, nullable=False)
