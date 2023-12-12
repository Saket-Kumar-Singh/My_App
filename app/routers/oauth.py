from ..models import userOut
from ..main import APIRouter 
from ..utlis import SECRET_KEY, ALGORITHM, CryptContext
from ..resources import OAuth2PasswordBearer, Depends
import datetime
from jose import jwt, JWTError
from passlib.hash import bcrypt

router = APIRouter(
    prefix = '/oauth',
    tags = ['oath']
)

pwd_context = CryptContext(schemes = ['bcrypt'], deprecated = "auto")
oauth_bearer = OAuth2PasswordBearer(tokenUrl = "oauth/token")

def create_user_token(user_id, user_name, expiry_time):
 expiry =datetime.datetime.now(datetime.timezone.utc)
 encode = {"id" : user_id, "sub" : user_name, "exp" : expiry}
 return jwt.encode(encode, SECRET_KEY, algorithm =  ALGORITHM )   

