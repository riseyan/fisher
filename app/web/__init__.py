# -*- coding: utf-8 -*-
"""
@Time ： 2022/4/15 3:10 PM
@Auth ： zx.yan
"""
from flask import Blueprint

web = Blueprint('web',__name__)

from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish