from .. import utlis
from ..resources import status, models, HTTPException, APIRouter, timedelta
from ..main import conn, cursor
from .oauth import create_user_token
from passlib.context import CryptContext
from jose import JWTError

router = APIRouter(
    prefix = '/login',
    tags = ['login']
)

@router.post("/", status_code=status.HTTP_202_ACCEPTED)
def login_user(payload : models.userLogin):
    try:
        pload = payload.dict()
        s = f"select * from user_data where user_name = '{payload.user_name}'"
        cursor.execute(s)
        p = cursor.fetchone()
        if(p is None):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Credentials")
        if(utlis.match(pload['user_password'], p['user_password'])):
            token = create_user_token(p['user_id'], payload.user_name, timedelta(minutes = 20))
            return {"token" : token}
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail= "Incorrect Credentials")
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail = "Something's off")    
    