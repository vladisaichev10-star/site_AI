"""
Модуль маршрутов веб-приложения.
"""
from typing import Optional

from flask_login import login_user, login_required, logout_user, current_user

from database import create_tables, create_user

from flask import render_template, request, flash, redirect, url_for
from config import app, login_manager
from database.crud import get_user
from database.models import User
from validation import valid


@login_manager.user_loader
def load_user(user_id: str) -> Optional[User]:
    """
    Загружает пользователя по его идентификатору для Flask-Login.
    """
    user: Optional[User] = User.get_or_none(User.id == int(user_id))
    return user



@app.route("/")
def index() -> str:
    """
    Отображает главную страницу приложения.
    """
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register() -> str:
    """
    Обрабатывает страницу регистрации пользователя.
    """
    if request.method == "POST":
        login = request.form.get("login")
        password = request.form.get("password")
        password2 = request.form.get("password2")


        is_valid = valid(login=login, password=password, password2=password2)

        if is_valid:
            create_user(login=login, password=password)
            flash(message="Успешная регистрация", category="success-toast")
            return redirect("/")
        else:
            flash("Поля заполненны не верно")
            return redirect("/register")
    else:
        return render_template("register.html")


@app.route("/services", methods=["GET"])
def services() -> str:
    """
    Возвращает страницу со списком продуктов.
    """
    return render_template("services.html")

@app.route("/product", methods=["GET"])
def product() -> str:


    return render_template("product.html")


@app.route("/info", methods=["GET"])
@login_required
def info() -> str:
    """
    Возвращает страницу с дополнительной информацией.
    """
    return "Дополнительная информация"

@app.route("/login", methods=["GET", "POST"])
def login() -> str:
    """
    Возвращает страницу с авторизацией.
    """

    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        login = (request.form.get("login") or "").strip()
        password = (request.form.get("password") or "").strip()


        if not login or not password:
            flash("Введите логин или пароль", category="login_toast")
            return redirect("/login")

        user = get_user(login=login)
        print(user)
        if user is None:
            flash(message="Пользователь не найден", category="login_toast")
            return redirect("/login")

        if not user.check_password(password=password):
            flash(message="Пароли не совпадают", category="login_toast")
            return redirect("/login")

        login_user(user)

        flash("Вы вошли в систему", category="success-toast")
        return redirect("/")


@app.route("/logout")
def logout():
    login = current_user.login
    logout_user()
    flash()
    app.logger.info(f"sadas {login}")


    return redirect("/login")



@app.errorhandler(404)
def error_404(error: Exception) -> tuple[str, int]:
    """
    Обработчик ошибки 404 (страница не найдена).
    """
    return render_template("404.html"), 404


@app.errorhandler(500)
def error_500(error: Exception) -> tuple[str, int]:
    """
    Обработчик ошибки 500 (внутренняя ошибка сервера).
    """
    return render_template("500.html"), 500


if __name__ == "__main__":
    create_tables()
    app.run()
