from tkinter import BASELINE
from typing import Optional
from fastapi import Body, FastAPI, Request, status, HTTPException, APIRouter
from pydantic import BaseModel
import random
import psycopg2
from psycopg2.extras import RealDictCursor
from .. import models
import time
from ..main import conn, cursor
from ..utlis import hash
print(int('707'))
router = APIRouter()

@router.put("/users", status_code=status.HTTP_201_CREATED)
def create_user(payload: models.user, status_code = status.HTTP_201_CREATED):
    # try:
    pload = payload.dict()
    # print(type(pload["user_password"]))
    print(pload["user_password"])
    k = hash(pload["user_password"])
    del pload["user_password"]
    # print(pload["user_password"])
    t = tuple(pload.keys())
    # q = tuple(pload.values())
    q = []
    for r in t:
        try:
            q.append(int(pload[r]))
        except:
            q.append("'" + str(pload[r]) + "'")    
    print(q)
    q = tuple(q)
    print(t)
    p = ""
    for i in range(len(t)):
        p+="%s, "
    p = p[:len(p)-2]
    s = f"""insert into user_data ({p}, user_password) values ({p}, E'{k}') returning user_id, user_name""" %(t+q)
    print(s)
    try:
        cursor.execute(s)
        print("ok")
        new_post = cursor.fetchone()
        conn.commit()
        return {"details" : new_post}
    except Exception as error:
        # print(error)
        return {"details" : "%s" %error , "error type" : type(error)}
        

@router.put("/users/{id}")
def update_post(payload : dict, id : int): 
    s = f"""update user_data set """
    for i in payload:
        s += f"""{i} = '{payload[i]}',"""
    # print(s)
    s = s[:len(s)-1]
    s += f"where user_id = {id} returning *"
    cursor.execute(s)
    new_post = cursor.fetchone() 
    if new_post == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)
    conn.commit()
    return {"detail" : new_post}


@router.get("/users/{id}", status_code = status.HTTP_302_FOUND)
def get_user_info(id : int):
    s = """select user_id, user_name, last_updated from user_data where user_id = %s""" %(id)
    cursor.execute(s)
    data = cursor.fetchone()
    if data == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return {"details" : "User not found"}
    return {"details" : data}


