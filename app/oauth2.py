import email
from logging import raiseExceptions
from mmap import ACCESS_DEFAULT
from webbrowser import get
from anyio import current_time
from fastapi import Depends,status,HTTPException
from jose import JWTError,jwt
from datetime import datetime,timedelta
from pynput.mouse import Button,Controller
from app import models
from . import schemas,database
from fastapi.security import OAuth2PasswordBearer
from typing import List
from sqlalchemy.orm import Session
import time

oauth2_scheme =OAuth2PasswordBearer(tokenUrl= 'login')



SECRET_KEY="09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 2
REFRESH_TOKEN_EXPIRE_HOURS = 6


def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})

    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

    return encoded_jwt

def verify_access_token(token:str,credentials_exception):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        id:str=payload.get("user_id")
    
        if id is None:
            raise credentials_exception
        token_data=schemas.TokenData(id=id)
    except JWTError:
        raise credentials_exception
    
    return token_data

def get_current_user(token:str=Depends(oauth2_scheme),db:Session=Depends(database.get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
    detail=f"could not valiadate credentials",headers={"WWW-Authenticate":"Bearer"})

    token=verify_access_token(token,credentials_exception)
    
    user=db.query(models.User).filter(models.User.id == token.id).first()
    return user



def create_refresh_token(data:dict):
    to_encode = data.copy()
    
    expired = datetime.utcnow()+timedelta(hours=REFRESH_TOKEN_EXPIRE_HOURS)
    to_encode.update({"exp":expired})


    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    

    return encoded_jwt
'''
def verify_refresh_token(tokenla:str,credentials_exception):
    try:
        payload=jwt.decode(tokenla,SECRET_KEY,algorithms=[ALGORITHM])
        id:str=payload.get("user_id")
    
        if id is None:
            raise credentials_exception
        token_data=schemas.TokenData(id=id)
    except JWTError:
        raise credentials_exception
    
    return token_data

'''
'''
def verify_refresh_token(refreshtoken:str,credentials_exception):
    try:
        payload=jwt.decode(refreshtoken,SECRET_KEY,algorithms=[ALGORITHM])
        refreshtoken:str=payload.get("refreshtoken")
    
        if refreshtoken is None:
            raise credentials_exception
        refreshtoken_data=schemas.TokenData(refreshtoken=refreshtoken) 
    except JWTError:
        raise credentials_exception
    
    return refreshtoken_data
'''


def create_neww_token(data:dict):
    to_encode = data.copy()
    
    expired = datetime.utcnow()+timedelta(hours=REFRESH_TOKEN_EXPIRE_HOURS)
    to_encode.update({"exp":expired})


    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

    return encoded_jwt

def verify_neww_token(token1:str,credentials_exception):
    try:
        payload=jwt.decode(token1,SECRET_KEY,algorithms=[ALGORITHM])
        id:str=payload.get("user_id")
    
        if id is None:
            raise credentials_exception
        token1_data=schemas.TokenData(id=id)
    except JWTError:
        raise credentials_exception
    
    return token1_data    
def get_current_user(token1:str=Depends(oauth2_scheme),db:Session=Depends(database.get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
    detail=f"could not valiadate credentials",headers={"WWW-Authenticate":"Bearer"})

    token=verify_neww_token(token1,credentials_exception)
    
    user=db.query(models.User).filter(models.User.id == token.id).first()
    return user

'''    
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)  
    else:
        expire = datetime.utcnow() + timedelta(hours=REFRESH_TOKEN_EXPIRE_HOURS)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
'''
'''
async def get_current_user(token: str = Depends(oauth2_scheme),db:Session=Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user.id")
        if id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=id)
    except JWTError:
        raise credentials_exception
    user =db.query(models.User).filter(models.User.id == token.id).first()
    #get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

'''    
'''
async def get_current_active_user(current_user: models.User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
'''
'''
async def login_for_access_token(form_data:OAuth2PasswordRequestForm = Depends(),db:Session=Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    #authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
'''
'''
def create_refreshness_token(data:dict):
    to_encode=data.copy()

    expired=datetime.minute(1)+timedelta(hours=REFRESH_TOKEN_EXPIRE_HOURS)
    to_encode.update({'exp':expired})

    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    

    def verify_refreshness_token(token:str,credentials_exception):
        try:
            payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
            id:str=payload.get("user_id")
        
            if id is None:
                raise credentials_exception
            token_data=schemas.TokenData(id=id)    
        except JWTError:
            raise credentials_exception
        
        return token_data
    def get_current_user(token:str=Depends(oauth2_scheme),db:Session=Depends(database.get_db)):
        credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"could not valiadate credentials",headers={"WWW-Authenticate":"Bearer"})

        token=verify_refreshness_token(token,credentials_exception)
        
        user=db.query(models.User).filter(models.User.id == token.id).first()
        return user       

'''
'''
def get_value_user(refreshtoken:str=Depends(oauth2_scheme),db:Session=Depends(database.get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
    detail=f"could not valiadate credentials",headers={"WWW-Authenticate":"Bearer"})

    refreshtoken=verify_refresh_token(refreshtoken,credentials_exception)
    
    
    return create_neww_token
'''