from os import access
from pyexpat import model
from fastapi import APIRouter,Depends,status,HTTPException,Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm 
from sqlalchemy.orm import Session
from datetime import datetime,timedelta
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi_jwt_auth import AuthJWT


access=[]



from .. import database,schemas,models,utils,oauth2

router= APIRouter(tags=['Authentication'])

@router.post('/login')
def login(user_credentials:OAuth2PasswordRequestForm=Depends(), db:Session=Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email == user_credentials.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"invalid credential")
    
    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"invaid credential")

    access_token=oauth2.create_access_token(data={"user_id":user.id})
    refresh_token=oauth2.create_refresh_token(data={"user_password":user.id})
    access.append(refresh_token)

    return{"access_token":access_token,"token_type":"bearer","refresh_token":refresh_token,"token_type":"bearer"}

@router.post('/relogin')
def relogin(user_credentials:OAuth2PasswordRequestForm=Depends(), db:Session=Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"invalid credential")
    
    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"invaid credential")    
    
    neww_token=oauth2.create_neww_token(data={"user_id":user.id})
    return{"neww_token":neww_token}   
'''
@router.post('/relogin')
def logins():
    user=models.User
'''    






'''
@router.post('/refresh')
def refresh(Authorize: AuthJWT = Depends()):
    Authorize.jwt_refresh_token_required()
    get_current_user=Authorize._refresh_token_expires()
    new_access_token=Authorize.create_neww_token(subject=get_current_user)
    return{"new access token":new_access_token}
'''

'''
@router.post('/login')
def refresh(user_credentials:OAuth2PasswordRequestForm=Depends()):
    refreshness_token=oauth2.create_refreshness_token(data={"user_id:user.id"})
    return{"refresh token":refreshness_token,"token_type":"bearer"}
'''
'''
@router.post("/token", response_model=models.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),db:Session=Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    #authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_refresh_token(
        data={"user_id": user.id}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
'''
'''
@router.get('/refresh_token')
def refresh_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    refresh_token = credentials.credentials
    new_token = auth_handler.refresh_token(refresh_token)
    return {'access_token': new_token}    
    '''