from ..models import userOut, TokenData
from ..main import APIRouter, HTTPException, cursor 
from ..utlis import SECRET_KEY, ALGORITHM, CryptContext
from ..resources import OAuth2PasswordBearer, Depends, status
from datetime import datetime
from jose import jwt, JWTError
from passlib.hash import bcrypt

router = APIRouter(
    prefix = '/oauth',
    tags = ['oath']
)

pwd_context = CryptContext(schemes = ['bcrypt'], deprecated = "auto")
oauth_bearer = OAuth2PasswordBearer(tokenUrl = "oauth/token")

def create_user_token(user_id, user_name, expiry_time):
 expiry = datetime.utcnow(datetime.timezone.utc)
 encode = {"id" : user_id, "sub" : user_name, "exp" : expiry}
 return jwt.encode(encode, SECRET_KEY, algorithm =  ALGORITHM )   

def get_user(username : str or None = None):
   s = f"select * from user_data where user_name = '{username}"
   cursor.execute(s)
   p = cursor.fetchone()
   return p

def active_user(token : str = Depends(oauth_bearer)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, details = "Could Not Validate", 
                                      headers={"WWW-Authenticate" : "Bearer"})
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms = [ALGORITHM])
        username : str = payload.get("sub")
        if username is None:
            raise credential_exception
        
        token_data = TokenData(username = username)
    except JWTError:
        raise credential_exception

    user = get_user(username = token_data.username)
    if user is None:
       raise credential_exception
    
    return user
#  except:
#     return credential_exception
