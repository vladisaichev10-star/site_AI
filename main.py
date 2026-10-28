"""
Модуль маршрутов веб-приложения.

Содержит определение HTTP-маршрутов Flask-приложения, загрузчик
пользователя для Flask-Login и обработчики ошибок.

Маршруты:
    /                — главная страница;
    /register        — регистрация пользователя (GET/POST);
    /products        — список продуктов;
    /info            — дополнительная информация.

Обработчики ошибок:
    404 — страница не найдена;
    500 — внутренняя ошибка сервера.

При запуске как скрипта запускает dev-сервер Flask.
"""
from __future__ import annotations

from typing import Optional, Union

from flask import render_template, request, Response
from flask_login import UserMixin

from config import app, login_manager
from database.models import User


@login_manager.user_loader
def load_user(user_id: str) -> Optional[User]:
    """
    Загружает пользователя по его идентификатору для Flask-Login.

    Вызывается Flask-Login при восстановлении сессии, чтобы получить
    объект пользователя из БД по id, сохранённому в сессии.

    Args:
        user_id: Идентификатор пользователя в виде строки
            (так его хранит Flask-Login в сессии).

    Returns:
        Экземпляр User, если пользователь найден, иначе None.
    """
    user: Optional[User] = User.get_or_none(User.id == int(user_id))
    return user


@app.route("/")
def index() -> str:
    """
    Отображает главную страницу приложения.

    Returns:
        HTML-разметка главной страницы (index.html).
    """
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register() -> str:
    """
    Обрабатывает страницу регистрации пользователя.

    GET-запрос возвращает форму регистрации.
    POST-запрос принимает данные формы (поле ``name``) и выводит их
    в консоль (временная заглушка — TODO: реализовать сохранение).

    Returns:
        HTML-разметка страницы регистрации (register.html).
    """
    # TODO: получить данные и вывести на экран
    print(request.form.get("name"))
    return render_template("register.html")


@app.route("/products", methods=["GET"])
def products() -> str:
    """
    Возвращает страницу со списком продуктов.

    Returns:
        Строка-заглушка «Продукты».
    """
    return "Продукты"


@app.route("/info", methods=["GET"])
def info() -> str:
    """
    Возвращает страницу с дополнительной информацией.

    Returns:
        Строка-заглушка «Дополнительная информация».
    """
    return "Дополнительная информация"


@app.errorhandler(404)
def error_404(error: Exception) -> tuple[str, int]:
    """
    Обработчик ошибки 404 (страница не найдена).

    Args:
        error: Объект исключения, переданный Flask.

    Returns:
        Кортеж (HTML-разметка страницы 404, HTTP-код 404).
    """
    return render_template("404.html"), 404


@app.errorhandler(500)
def error_500(error: Exception) -> tuple[str, int]:
    """
    Обработчик ошибки 500 (внутренняя ошибка сервера).

    Args:
        error: Объект исключения, переданный Flask.

    Returns:
        Кортеж (HTML-разметка страницы 500, HTTP-код 500).
    """
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run()