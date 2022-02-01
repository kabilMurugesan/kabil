from cgitb import text
import string
from sqlalchemy import TIMESTAMP, Column, Integer, String
from sqlalchemy.sql.expression import null,text
from .database import Base

class Fees(Base):
    __tablename__="feemaster"

    student_id=Column(Integer,primary_key=True,nullable=False)
    student_name=Column(String,nullable=False)
    academic_fees=Column(String,nullable=False)
    fees_paid=Column(String,nullable=False)
    fees_balance=Column(String,nullable=False)
    paid_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

class User(Base):
    __tablename__ ="user"
    id=Column(Integer,primary_key=True,nullable=False)
    email=Column(String,nullable=False, unique=True)
    password=Column(String,nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

