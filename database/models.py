"""
Модели базы данных приложения.

Модели:
    BaseModel — общая база для всех таблиц, задаёт подключение к БД;
    User — пользователь приложения с хешированием пароля
"""

from datetime import datetime

from flask_login import UserMixin
from peewee import CharField, DateTimeField, Model
from werkzeug.security import check_password_hash, generate_password_hash

from .config import db


class BaseModel(Model):
    """
    Базовая модель всех таблиц в БД.
    """

    class Meta:
        """Метаданные модели: подключение к базе данных."""
        database = db


class User(UserMixin, BaseModel):
    """
    Пользователь приложения.


    Attributes:
        username: Уникальное имя пользователя.
        password_hash: Хеш пароля пользователя .
        created_at: Дата и время создания записи.
    """

    username = CharField(unique=True, max_length=25, index=True, null=False)
    password_hash = CharField(max_length=255, null=False)
    created_at = DateTimeField(default=datetime.now)

    def set_password(self, password: str) -> None:
        """
        Устанавливает пароль пользователя, сохраняя только его хеш.
        """
        self.password_hash = generate_password_hash(password=password)

    def check_password(self, password: str) -> bool:
        """
        Проверяет, соответствует ли переданный пароль сохранённому хешу.
        """
        return check_password_hash(self.password_hash, password)

