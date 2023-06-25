from sqlalchemy import Table, Column
from typing import Optional
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from db import meta, Base
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

users: Table = Table(
    'user', meta,
    Column('id', Integer, primary_key=True),
    Column('idd', Integer),
    Column('username', String(255), unique=True),
    Column('hashed_password', String(255)),
    Column('phone', Integer),
    Column('role', String(255)),
    Column('ism', String(255)),
    Column('token', String(255)),
    Column('disabled', Boolean, default=False),
)


class User_model(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    idd = Column(Integer)
    username = Column(String)
    hashed_password = Column(String)
    phone = Column(Integer)
    role = Column(String)
    ism = Column(String)
    token = Column(String)
    disabled = Column(Boolean)


class Token(BaseModel):
    access_token: str
    token_type: str
    role: str
    idd: str


class TokenData(BaseModel):
    username: Optional[str] = None


class ReseptionUser(BaseModel):
    username: str
    password: str
    ism: str
    phone: int


class User(BaseModel):
    id: int
    username: str
    phone: Optional[str] = None
    ism: Optional[str] = None
    disabled: Optional[bool] = None
    role: str
    idd: str


class Tokens(BaseModel):
    token: str


class NewUser(BaseModel):
    username: str
    password: str
    ism: str
    phone: int


class User_diagnostika(BaseModel):
    username: str
    password: str
    ism: str
    phone: int


class CopyToken(BaseModel):
    token2: str


class NewUsers(BaseModel):
    username: str
    password: str
    ism: str
    phone: int


class UserInDB(User):
    hashed_password: str
