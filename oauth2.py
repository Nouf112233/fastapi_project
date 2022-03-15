from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import JWToken

from sqlalchemy.orm import session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    # credentials_exception = HTTPException(
    #     status_code=status.HTTP_401_UNAUTHORIZED,
    #     detail="Could not validate credentials",
    #     headers={"WWW-Authenticate": "Bearer"},
    # )
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials")


    return JWToken.verify_token(credentials_exception,token)