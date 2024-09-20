from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from models.user import User
# 表單驗證

STYLES = "text-xl w-full md:w-1/2 px-3 py-2 border border-gray-900 rounded-sm"

def unique_username(form, field):
    if User.query.filter_by(username=field.data).first():
        raise ValidationError("該帳號已被申請過!")

class UserRegisterForm(Form):
    username = StringField("帳號",
                           validators=[InputRequired(), Length(min=4), unique_username],
                           render_kw={"placeholder": "使用者帳號", "class": STYLES},)
    
    password = PasswordField("密碼",
                             validators=[InputRequired(), Length(min=4)],
                             render_kw={"placeholder": "請填寫密碼", "class": STYLES},)
    
    password_confirm = PasswordField("密碼確認",
                                     validators=[InputRequired(), EqualTo("password", message="密碼不符")],
                                     render_kw={"placeholder": "再次確認密碼", "class": STYLES},)
    

class UserLoginForm(Form):
    username = StringField("帳號",
                           validators=[InputRequired(), Length(min=4)],
                           render_kw={"placeholder": "使用者帳號", "class": STYLES},
                           )
    password = PasswordField("密碼",
                             validators=[InputRequired()],
                             render_kw={"placeholder": "登入密碼", "class": STYLES},
                             )