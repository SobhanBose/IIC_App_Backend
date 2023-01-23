from passlib.context import CryptContext

pswd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_pswd(password: int):
    return pswd_context.hash(password)