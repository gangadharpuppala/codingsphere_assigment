from models import User, Project
from auth import hash_password, verify_password, create_access_token
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

async def create_user(user_data, session: AsyncSession):
    user = User(username=user_data.username, hashed_password=hash_password(user_data.password), role=user_data.role)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user

async def authenticate_user(username: str, password: str, session: AsyncSession):
    result = await session.exec(select(User).where(User.username == username))
    user = result.first()
    if not user or not verify_password(password, user.hashed_password):
        return None
    token = create_access_token(data={"sub": user.id, "role": user.role})
    return token

async def get_projects(session: AsyncSession):
    return (await session.exec(select(Project))).all()

async def create_project(project_data, session: AsyncSession):
    project = Project(**project_data.dict())
    session.add(project)
    await session.commit()
    await session.refresh(project)
    return project

