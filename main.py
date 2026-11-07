"""
Модуль маршрутов веб-приложения.
"""
from typing import Optional

from database import create_tables, create_user

from flask import render_template, request, flash, redirect
from config import app, login_manager
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
    # TODO: получить данные и вывести на экран
    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")
        password2 = request.form.get("password2")


        is_valid = valid(name=name, password=password, password2=password2)

        if is_valid:
            create_user(username=name, password=password)
            flash(message="Успешная регистрация", category="success-toast")
            return redirect("/")
        else:
            flash("Поля заполненны не верно")
            return redirect("/register")
    else:
        return render_template("register.html")


@app.route("/products", methods=["GET"])
def products() -> str:
    """
    Возвращает страницу со списком продуктов.
    """
    return "Продукты"


@app.route("/info", methods=["GET"])
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

    if request.method == "POST":


    return render_template("/login")


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
