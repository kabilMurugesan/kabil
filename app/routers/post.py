from fastapi import FastAPI,Response,HTTPException, status,Depends,APIRouter

from app import oauth2
from .. import models,schemas,oauth2
from typing import List
from sqlalchemy.orm import Session
from ..database import get_db
from fastapi.security import OAuth2PasswordBearer


router=APIRouter(
    prefix='/details',
    tags=['posts']
)



@router.get("/",response_model=List[schemas.Fees])
def test_posts(db: Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    print(current_user.email)
    posts=db.query(models.Fees).all()
    return posts

@router.get("/{student_id}",response_model=schemas.Fees)
def get_post(student_id:int,db: Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):#,ultra_user:int=Depends(oauth2.get_ultra_user)):
    print(current_user.email)
    #print(ultra_user.email)
    post=db.query(models.Fees).filter(models.Fees.student_id == student_id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with student_id:{student_id} was not found")
    return post                    


@router.post("/", response_model=schemas.Fees)
def paidlist(post:schemas.FeesCreate,db: Session = Depends(get_db),current_user: int =Depends(oauth2.get_current_user)):
    #new_post=models.Fees(student_id=post.student_id,student_name=post.student_name,academic_fees=post.academic_fees,fees_paid=post.fees_paid,fees_balance=post.fees_balance)
    print(current_user.email)
    new_post=models.Fees(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post



@router.put("/{student_id}",response_model=schemas.Fees)
def altering(student_id:int,po:schemas.FeesCreate,db: Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
        print(current_user.email)
        modified_list=db.query(models.Fees).filter(models.Fees.student_id == student_id)
        post = modified_list.first()
        if post == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"post with:{student_id} doesnt exist")
        
        modified_list.update(po.dict(),synchronize_session=False)
        db.commit()

        return modified_list.first()
   
@router.delete("/{student_id}")
def erasing(student_id:int,db: Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    print(current_user.email)
    post=db.query(models.Fees).filter(models.Fees.student_id == student_id)

    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with:{student_id} doesnt exist")
    post.delete(synchronize_session=False)
    db.commit()    
    return Response(status_code=status.HTTP_204_NO_CONTENT)