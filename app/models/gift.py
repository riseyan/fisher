# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/25 15:17
@Auth ： zx.yan
"""
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship

from app.models.base import db, Base


class Gift(Base):
    id = Column(Integer, primary_key=True)
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    isbn = Column(String(13), nullable=False)
    launched = Column(Boolean, default=False)