from fastapi import FastAPI, Depends, HTTPException
from database import init_db, get_session
from models import Project
from schemas import UserCreate, UserLogin, Token, ProjectCreate, ProjectRead
from crud import create_user, authenticate_user, get_projects, create_project
from deps import get_current_user, require_role
from sqlmodel.ext.asyncio.session import AsyncSession

app = FastAPI()

@app.on_event("startup")
async def startup():
    await init_db()

@app.post("/register")
async def register(user: UserCreate, session: AsyncSession = Depends(get_session)):
    return await create_user(user, session)

@app.post("/login", response_model=Token)
async def login(user: UserLogin, session: AsyncSession = Depends(get_session)):
    token = await authenticate_user(user.username, user.password, session)
    if not token:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"access_token": token, "token_type": "bearer"}

@app.get("/projects", response_model=list[ProjectRead])
async def read_projects(session: AsyncSession = Depends(get_session), user=Depends(get_current_user)):
    return await get_projects(session)

@app.post("/projects", response_model=ProjectRead)
async def add_project(project: ProjectCreate,
                      session: AsyncSession = Depends(get_session),
                      admin=Depends(require_role("admin"))):
    return await create_project(project, session)

