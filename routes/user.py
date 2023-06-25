import os
import uuid
from fastapi import APIRouter, Depends, HTTPException, Form, File, UploadFile
from sqlalchemy import desc
from sqlalchemy.orm import joinedload
from db import conn, get_db
from models.user import users, User, NewUser, User_diagnostika, ReseptionUser
from models.all_models import Filial
from routes.login import get_password_hash
from routes.login import get_current_active_user
from enum import Enum
from sqlalchemy.orm.session import Session



user_router = APIRouter(
    tags=['User']
)


@user_router.get("/userlar_test")
async def read_data():
    count_username = conn.execute(users.select()).rowcount
    if count_username > 0:
        test = 1
    else:
        test = 0
    return {"status": test}


# POST method
@user_router.post("/filial_admin_creates")
async def write_data(filial_id: str, user_data: NewUser, session: Session = Depends(get_db)):
    # validate username
    user_validation = conn.execute(users.select()).fetchall()
    filial = session.query(Filial).filter(Filial.id == filial_id).first()
    if filial == None:
        raise HTTPException(status_code=404, detail="Bunday filial mavjud emas")
    if user_validation == 0:
        raise HTTPException(status_code=404, detail="Xizmatdan foydalana olmaysiz !!!")
    count_username = conn.execute(users.select().where(users.c.username == user_data.username)).rowcount
    if count_username > 0:
        raise HTTPException(status_code=404, detail="Bu username bilan avval ham ro`yxatga olingan")
    elif len(user_data.username) < 5 or len(user_data.password) < 8:
        raise HTTPException(status_code=404, detail="Login yoki parolni to`g`ri kiriting!")

    conn.execute(users.insert().values(
        username=user_data.username,
        hashed_password=get_password_hash(user_data.password),
        role="filial_admin",
        ism=user_data.ism,
        phone=user_data.phone,
        token="0",
        idd=filial.id,
    ))
    raise HTTPException(status_code=200, detail="SuccessFull")
