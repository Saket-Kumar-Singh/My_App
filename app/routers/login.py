from .. import utlis
from ..resources import status, models, HTTPException, APIRouter
from ..main import conn, cursor

router = APIRouter()

@router.post("/login", status_code=status.HTTP_202_ACCEPTED)
def login_user(payload : models.userLogin):
    pload = payload.dict()
    s = f"select user_password from user_data where user_name = '{payload.user_name}'"
    cursor.execute(s)
    p = cursor.fetchone()
    if(utlis.match(pload['user_password'], p['user_password'])):
        return {"details" : "Correct_Credentials"}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)