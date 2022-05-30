# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/26 10:09
@Auth ： zx.yan
"""
from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError

from app.models.user import User


class RegisterForm(Form):
    nickname = StringField('昵称', validators=[
        DataRequired(message='昵称不能为空，需要2-10个字符'), Length(2, 10, message='昵称至少需要两个字符，最多10个字符')])

    password = PasswordField('密码', validators=[
        DataRequired(message='密码不能为空，需要6-20个字符'), Length(6, 20)])

    email = StringField('电子邮件', validators=[DataRequired(), Length(8, 64),Email(message='电子邮箱不符合规范！')])
    # Email(message='电子邮箱不符合规范！')

    def validate_email(self,field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError('电子邮件已被注册！')

    def validate_nickname(self,field):
        if User.query.filter_by(nickname = field.data).first():
            raise ValidationError('该昵称已被注册！')

class LoginForm(Form):
    email = StringField('电子邮件', validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱不符合规范！')])
    password = PasswordField('密码', validators=[
        DataRequired(message='密码不能为空，需要6-20个字符'), Length(6, 20)])
