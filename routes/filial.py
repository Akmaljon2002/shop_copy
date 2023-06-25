import os
import uuid
from fastapi import APIRouter, Depends, HTTPException, Form, File, UploadFile
from sqlalchemy import desc
from sqlalchemy.orm import joinedload
from db import conn, get_db
from models.user import users, User, NewUser, User_diagnostika, ReseptionUser
from routes.login import get_password_hash
from routes.login import get_current_active_user
from enum import Enum
from sqlalchemy.orm.session import Session
from models.all_models import Filial, Filial_schema


filial_router = APIRouter(
    tags=['Filial']
)


#admin uchun filial update
@filial_router.post("/filial_post")
async def data(f: Filial_schema,
        session: Session = Depends(get_db),
        current_user: User = Depends(get_current_active_user)):
    filial_post = Filial(
        manzil = f.manzil,
        tel = f.tel
    )
    session.add(filial_post)
    session.commit()
    session.refresh(filial_post)
    return filial_post


#admin uchun filial update
@filial_router.put("/filial_put")
async def data(id: str,
        f: Filial_schema,
        session: Session = Depends(get_db),
        current_user: User = Depends(get_current_active_user)):
    filial = session.query(Filial).filter(Filial.id == id).first()
    filial.manzil = f.manzil
    filial.tel = f.tel

    session.commit()
    session.refresh(filial)
    return filial

# admin uchun filial delete
@filial_router.delete("/filial_delete")
async def data(id: str,
        session: Session = Depends(get_db),
        current_user: User = Depends(get_current_active_user)):
    session.query(Filial).filter(Filial.id == id).delete()
    session.commit()
    return "Ma'lumot o'chirildi"


# admin uchun filial get
@filial_router.get("/filial_get")
async def data(session: Session = Depends(get_db),
        current_user: User = Depends(get_current_active_user)):
    filial = session.query(Filial).all()
    return filial

