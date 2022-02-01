import email
from msilib.schema import Class
from os import access
from turtle import update
from typing import Optional
from pydantic import BaseModel,EmailStr
from datetime import datetime

class FeesBase(BaseModel):
    student_id: str
    student_name:str
    academic_fees: str
    fees_paid: str
    fees_balance: str

class FeesCreate(FeesBase):
    pass

class Fees(FeesBase):
    paid_at:datetime
    
    class Config:
        orm_mode = True



class UserCreate(BaseModel):
    email:EmailStr
    password:str   

class UserOut(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime
    class Config:
        orm_mode =True         

class UserLogin(BaseModel):
    email:EmailStr
    password:str
 
class Token(BaseModel):
    access_token=str
    token_type=str

class TokenData(BaseModel):
    id:Optional[str] = None
    





    
