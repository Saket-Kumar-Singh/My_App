from .. import utlis
from ..resources import status, models, HTTPException, APIRouter, timedelta
from ..main import conn, cursor
from .oauth import create_user_token

router = APIRouter()

@router.post("/login", status_code=status.HTTP_202_ACCEPTED)
def login_user(payload : models.userLogin):
    pload = payload.dict()
    s = f"select user_password from user_data where user_name = '{payload.user_name}'"
    cursor.execute(s)
    p = cursor.fetchone()
    if(p is None):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Credentials")
    if(utlis.match(pload['user_password'], p['user_password'])):
        token = create_user_token(17, payload.user_name, timedelta(minutes = 20))
        return {"token" : token}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail= "Incorrect Credentials")
    