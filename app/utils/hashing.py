from passlib.context import CryptContext

pswd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_pswd(password: str) -> str:
    return pswd_context.hash(password)

def verify_hash(hashed_pswd: str, plain_pswd: str) -> bool:
    return pswd_context.verify(plain_pswd, hashed_pswd)