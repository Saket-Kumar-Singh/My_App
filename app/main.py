from tkinter import BASELINE
from typing import Optional
from fastapi import Body, FastAPI, Request, status, HTTPException, APIRouter
from pydantic import BaseModel
import random
import psycopg2
from psycopg2.extras import RealDictCursor
from . import models, utlis
import time
app = FastAPI()


while True:
    try :
        conn = psycopg2.connect(host = "localhost", database = "login", user = "postgres", password = "saket@postgres", cursor_factory=  RealDictCursor)
        cursor = conn.cursor()
        print("Connection was successful")
        break
    except Exception as error:
        print("Connection with fastapi failed")
        print("The error was", error)    
        time.sleep(3)

from .routers import users, login, oauth
app.include_router(users.router)
app.include_router(login.router)
app.include_router(oauth.router)
@app.get("/")
async def root():
    return {"message": "Hello mister please give us what you want"}


# s = "select user_password, user_name from user_data"
# cursor.execute(s)
# p = cursor.fetchall()
# for it in p:
#     it['user_password'] = utlis.hash(it['user_password'])
# for it in p:
#     print(type(it['user_password']))
#     s = f"""update user_data set user_password = E'{it['user_password']}' where user_name = '{it['user_name']}';"""
#     # print(s)
#     cursor.execute(s)    
# conn.commit()


# @app.post("/post")
# def create_post(payload: dict =  Body(...)):
#     # print(f"New post : the title is {payload['title']}, The content is {payload['content']}")
#     return {"New post" : f"New post : the title is {payload['title']}, The content is {payload['content']}"}


# @app.post("/n_post")
# def new_post(payload : Post):
#     print(payload.title)
#     return {"message" : "Success"}    


# @app.post("/post")
# def create_post(payload : Post, status_code = status.HTTP_201_CREATED):
#     pload = payload.dict()
#     pload["id"] = random.randint(1, 1000)
#     post_list.append(pload)
#     return {"details" : "Success is granted"}

# @app.get("/post/latest")
# def create_post():
#     return {"detail" : post_list[len(post_list) - 1]}

# @app.get("/post/{id}")
# def get_post(id : int):
#     my_post = find_post(id)
#     if not my_post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail = "Invalid id")
#     return {"detail" : my_post}

# @app.put("/post/{id}")
# def upd_post(id : int, post : Post):
#     my_post = find_post(id)
#     if not my_post:
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Invalid id")
#     else:
#         my_post = my_post.dict()
        