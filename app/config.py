from os import access
from pydantic import BaseSettings

from app import database   


class Setting(BaseSettings):
    database_hostname:str
    database_port:str
    database_password:str
    database_name:str
    database_username: str
    secret_key:str
    algorithm:str
    access_token_expire_minutes:int

    class Config:
        env_file =".env"


settings= Setting()
