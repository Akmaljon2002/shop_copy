from sqlalchemy import Table, Column, DateTime, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, Numeric
from db import meta
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from db import Base
from sqlalchemy.orm import relationship
import pytz
from enum import Enum

class Foydalanuvchi_session(Base):
    __tablename__ = 'foydalanuvchi'
    id = Column(String, primary_key=True, index=True)
    ism = Column(String)
    tugilgan_sana = Column(String)
    jinsi = Column(String)
    manzil = Column(String)
    mamlakat = Column(String)
    viloyat_id = Column(Integer)
    tuman_id = Column(Integer)
    tel = Column(String)
    letter = Column(String)
    karta_raqami = Column(String)
    balance = Column(Numeric)
    password = Column(String)
    username = Column(String)
    disabled = Column(Boolean)
    online = Column(DateTime)
    block = Column(Boolean)


class Filial(Base):
    __tablename__ = 'filial'
    id = Column(Integer, primary_key=True, index=True)
    manzil = Column(String)
    tel = Column(String)




class Filial_schema(BaseModel):
    manzil: str
    tel: str