# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/25 15:16
@Auth ： zx.yan
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, SmallInteger

db = SQLAlchemy()

class Base(db.Model):
    # base不去创建表
    __abstract__ = True
    # create_time = Column('create_time',Integer)
    status = Column(SmallInteger,default=1)

    # 表单动态赋值
    def set_attrs(self,attrs_dict):
        for key,value in attrs_dict.items():
            if hasattr(self,key) and key != 'id':
                setattr(self,key,value)