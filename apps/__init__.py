from flask import Flask
from dotenv import load_dotenv
import os
from pathlib import Path
from flask_login import LoginManager
from models import User


# 載入環境變數
load_dotenv()

ROOT_PATH = Path().parent.absolute()
TEMPLATE_FOLDER = ROOT_PATH / "templates"
DB_PATH = ROOT_PATH / "db" / "blog.db"

app = Flask(__name__, template_folder=TEMPLATE_FOLDER)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"

# 從環境變數讀取 SECRET KEY
app.secret_key = os.getenv("APP_SECRET_KEY")

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "user.login"
login_manager.login_message = "請登入會員帳號"

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)