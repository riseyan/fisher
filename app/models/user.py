# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/25 15:17
@Auth ： zx.yan
"""
from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash

from app.models.base import db, Base
from app.models.gift import Gift


class User(Base):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    gifts = relationship('Gift')
    _password = Column('password',String(128))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,raw):
        self._password = generate_password_hash(raw)