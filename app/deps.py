from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlmodel.ext.asyncio.session import AsyncSession
from database import get_session
from models import User
from auth import decode_token
from sqlmodel import select

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def get_current_user(token: str = Depends(oauth2_scheme), session: AsyncSession = Depends(get_session)):
    payload = decode_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    user_id: int = payload.get("sub")
    query = await session.exec(select(User).where(User.id == user_id))
    user = query.first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def require_role(required_role: str):
    def role_checker(user = Depends(get_current_user)):
        if user.role != required_role:
            raise HTTPException(status_code=403, detail="Forbidden")
        return user
    return role_checker

