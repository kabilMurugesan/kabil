import app
import app2
from sqlite3 import Cursor
from fastapi import FastAPI,Response,HTTPException, status
import fastapi
from fastapi.params import Body
from pydantic import BaseModel, Field
from typing import Optional
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from typing import Union

app5=FastAPI()
class Admission(BaseModel):
    student_id: str
    father_name: str
    address: str
    phone_number: str
    admission_date: str
    previous_school_info: str
    admission_fees: str

class Fees(BaseModel):
    student_id: str
    academic_year: str
    student_name: str
    total_fees: str
    fees_paid: str
    fees_balance: str

while True:
    try:
        conn = psycopg2.connect(host="localhost",database="fastapi",user="postgres",password="123456789",cursor_factory=RealDictCursor)
        cursor =conn.cursor()
        print("U HAVE SUCCESSFULLY CONNECTED WITH YOUR DATABASE!!!!!!")
        break
    except Exception as error:
        print("U DIDN'T CONNECT WITH YOUR DATABASE& TRY AGAIN!!!!!")
        print("Error:",error)
        time.sleep(2)

@app5.get("/alldata/{student_id}")
def joining():
    cursor.execute("SELECT * FROM FEES1 as t1 join admission1 as t2 ON t2.student_id=t1.student_id ")
    meet=cursor.fetchall()
    return{"data":meet}

@app5.get("/alldatas/{student_id}")
def joining(student_id:int):
    cursor.execute("""SELECT * FROM FEES1 as t1 join admission1 as t2 ON t2.student_id=t1.student_id WHERE t1.student_id=%s""",(str(student_id),))
    meets=cursor.fetchone()
    return{"data":meets}    