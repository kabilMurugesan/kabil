from doctest import Example
from logging import raiseExceptions
from sqlite3 import Cursor
from urllib import response
from fastapi import FastAPI,Response,HTTPException, status,Depends
import fastapi
from fastapi.params import Body
from pydantic import BaseModel, Field
from typing import List, Optional
from sqlalchemy.orm import Session
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from psycopg2.errors import UniqueViolation
from . import models,schemas,utils 
from .database import engine, get_db
from .routers import post,user,auth
from fastapi.testclient import TestClient
from .config import settings
from fastapi.middleware.cors import CORSMiddleware



models.Base.metadata.create_all(bind=engine)


app=FastAPI()

orgins=["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=orgins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/favicon.ico")
def application():
    return{"welcome":"to fast api"}










    

#@app.get("/posts")
#def paid(db: Session = Depends(get_db)):
 #   cursor.execute("SELECT * FROM FEES1")
  #  details=cursor.fetchall()
   # return{"data":details}
    

