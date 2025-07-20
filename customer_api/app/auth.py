from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from jwt import encode, decode

import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

# Secret key for JWT token
SECRET_KEY = os.getenv("1160c930ff4f6337d68078a802a17dab54ec5ca6f6b8ab23cba21989b0cc62a4")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # Token expiration time

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Simulated database (replace with real user validation)
fake_users_db = {
    "admin": {
        "username": "admin",
        "password": "password123"  # Replace with hashed password in real applications
    }
}


# Function to create a JWT token


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Login function to verify user credentials and return a token
def authenticate_user(username: str, password: str):
    user = fake_users_db.get(username)
    if not user or user["password"] != password:
        return None
    return user

# Function to verify JWT token
def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload  # Optionally, return user data if stored in the token
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
