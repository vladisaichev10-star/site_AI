# Todo сделать документацию и анотацию всему и на уровне модуля
from flask import render_template, request

from config import app, login_manager
from database.models import User


@login_manager.user_loader
def load_user(user_id):
    user = User.get_or_none(User.id == int(user_id))
    return user


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    # TODO получить данные и вывести на экран
    print(request.form.get("name"))
    return render_template("register.html")


@app.route("/products", methods=["GET"])
def products():
    return "Продукты"


@app.route("/info", methods=["GET"])
def info():
    return "Дополнительнвя информация"


@app.errorhandler(404)
def error_404(error):
    return render_template("404.html"), 404


# Todo ощибка 500 или 503


if __name__ == '__main__':
    app.run()
