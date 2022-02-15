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

app=FastAPI()

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

@app.get("/")
def application():
    return{"welcome":"to fast api"}

@app.get("/posts")
def paid():
    cursor.execute("SELECT * FROM FEES1")
    details=cursor.fetchall()
    return{"data":details}

@app.post("/newlist")
def paidlist(post:Fees):
    cursor.execute("""INSERT INTO FEES1 (student_id,academic_year,student_name,total_fees,fees_paid,fees_balance) VALUES(%s,%s,%s,%s,%s,%s) RETURNING * """,
    (post.student_id,post.academic_year,post.student_name,post.total_fees,post.fees_paid,post.fees_balance))
    new_list=cursor.fetchone()
    conn.commit()
    return{"all data":new_list}

@app.put("/editlist/{student_id}")
def altering(student_id:int,post:Fees):
        cursor.execute("""UPDATE FEES1 SET student_id=%s,academic_year=%s,student_name=%s,total_fees=%s,fees_paid=%s,fees_balance=%s WHERE student_id=%s RETURNING * """,
        (post.student_id,post.academic_year,post.student_name,post.total_fees,post.fees_paid,post.fees_balance,(str(student_id))))
        modified_list=cursor.fetchone()
        conn.commit()
        return{"altered_list":modified_list}
   
@app.delete("/deletedlist/{student_id}")
def erasing(student_id:int):
    cursor.execute("""DELETE FROM FEES1 WHERE student_id=%s RETURNING * """,(str(student_id),))
    application=cursor.fetchone()
    conn.commit()

    if application == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with:{student_id} doesnt exist")
    return Response(status_code=status.HTTP_204_NO_CONTENT)