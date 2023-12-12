import datetime
from datetime import timedelta
from tkinter import BASELINE
from typing import Optional
from fastapi import Body, FastAPI, Request, status, HTTPException, APIRouter, Depends
from pydantic import BaseModel
import random
import psycopg2
from psycopg2.extras import RealDictCursor
from . import models
import time
from fastapi.security import OAuth2PasswordBearer