from passlib.context import CryptContext
from passlib.hash import pbkdf2_sha256

# pwd_context = CryptContext(schemes=["sha256_crypt"])

def hash(password : str):
    print(pbkdf2_sha256.hash(password))
    return pbkdf2_sha256.hash(password)

def match(user_password, stored_password):
    return pbkdf2_sha256.verify(user_password, stored_password)

SECRET_KEY = "HCOIED3U2ufhriej2#ioqj3$kso"
ALGORITHM = "HS256"