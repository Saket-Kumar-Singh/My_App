from argparse import OPTIONAL
from pydantic import BaseModel, EmailStr
import random

class user(BaseModel):
    user_name : EmailStr
    user_password : str
    user_id : int = random.randint(0, 10000000)

class userOut(BaseModel):
    user_id : int
    user_name : EmailStr 

class userLogin(BaseModel):
    user_name : EmailStr
    user_password : str

class TokenData(BaseModel):
    access_token : str
    token_type : str