from doctest import Example
from sqlite3 import Cursor
from fastapi import FastAPI,Response,HTTPException, status
import fastapi
from fastapi.params import Body
from pydantic import BaseModel, Field
from typing import Optional
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from psycopg2.errors import UniqueViolation

newjoinies=FastAPI()

class Admission(BaseModel):
    student_id: str
    father_name: str
    address: str
    phone_number: str
    admission_date: str
    previous_school_info: str
    admission_fees: str


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

@newjoinies.get("/")
def application():
    return{"welcome":"to fast api"}

@newjoinies.get("/admission")
def paid():
    cursor.execute("SELECT * FROM ADMISSION1")
    details=cursor.fetchall()
    return{"data":details}

@newjoinies.post("/newadmission")
def students(us:Admission):
    cursor.execute("""INSERT INTO ADMISSION1(student_id,father_name,address,phone_number,admission_date,previous_school_info,admission_fees) VALUES(%s,%s,%s,%s,%s,%s,%s) RETURNING * """,
    (us.student_id,us.father_name,us.address,us.phone_number,us.admission_date,us.previous_school_info,us.admission_fees))
    newadmission=cursor.fetchone()
    conn.commit()
    return{"joinies":newadmission}

@newjoinies.put("/changes/{student_id}")
def changing(us:Admission,student_id):
    cursor.execute("""UPDATE ADMISSION1 SET student_id=%s,father_name=%s,address=%s,phone_number=%s,admission_date=%s,previous_school_info=%s,admission_fees=%s WHERE student_id=%s RETURNING *""",
    (us.student_id,us.father_name,us.address,us.phone_number,us.admission_date,us.previous_school_info,us.admission_fees,str(student_id),))
    newchanges=cursor.fetchone()
    conn.commit()
    return{"new":newchanges}

@newjoinies.delete("/deletion/{student_id}")
def deletionn(student_id:int):
    cursor.execute("""DELETE FROM ADMISSION1 WHERE student_id=%s RETURNING * """,(str(student_id),))
    deleting_post=cursor.fetchone()
    conn.commit()

    if deleting_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with student_id:{student_id} not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


     