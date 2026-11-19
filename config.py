from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)

app.config["SECRET_KEY"] = "secret"

login_manager = LoginManager(app=app)
login_manager.login_view = "login"
login_manager.login_message = "Войдите для продолжения"
login_manager.login_message_category = "error-toast"
login_manager.login_message_category = "error-toast"
