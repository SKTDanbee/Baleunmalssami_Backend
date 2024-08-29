import secrets
from sys import prefix

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware


from app import models, database
from app.routers import child, parent, auth, reports, friends

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key=secrets.token_hex(32))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=database.engine)

app.include_router(child.router, prefix="/child", tags=["child"])
app.include_router(parent.router, prefix="/parent", tags=["parents"])
app.include_router(auth.router, prefix='/auth', tags=['auth'])
app.include_router(reports.router, prefix='/reports', tags=['reports'])
app.include_router(friends.router, prefix='/friends', tags=['friends'])


# You can include more routers here if needed
