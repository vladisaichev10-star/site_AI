# Todo Использовать ленивый сетере и гшеттер (@property @setter)
# Todo Создать crud и функцию создания бд (create_tables)


"""
Модели базы данных приложения.

Определяет базовую модель :class:`BaseModel` (наследник ``peewee.Model``,
привязанный к общему подключению ``db``) и модель пользователя :class:`User`.

Модели:
    BaseModel — общая база для всех таблиц, задаёт подключение к БД;
    User      — пользователь приложения с хешированием пароля
                (совместим с Flask-Login через ``UserMixin``).
"""
from __future__ import annotations

from datetime import datetime

from flask_login import UserMixin
from peewee import CharField, DateTimeField, Model
from werkzeug.security import check_password_hash, generate_password_hash

from .config import db


class BaseModel(Model):
    """
    Базовая модель всех таблиц в БД.

    Наследует ``peewee.Model`` и привязывает модель к подключению ``db``
    из модуля ``config``. Все модели приложения должны наследоваться
    от этого класса, чтобы использовать одну и ту же БД.
    """

    class Meta:
        """Метаданные модели: подключение к базе данных."""
        database = db


class User(UserMixin, BaseModel):
    """
    Пользователь приложения.

    Наследует :class:`BaseModel` (Peewee) и :class:`flask_login.UserMixin`
    (для интеграции с Flask-Login: ``is_authenticated``, ``get_id`` и т.д.).

    Attributes:
        username: Уникальное имя пользователя (до 25 символов).
        password_hash: Хеш пароля пользователя (см. :meth:`set_password`).
        created_at: Дата и время создания записи.
    """

    username = CharField(unique=True, max_length=25, index=True, null=False)
    password_hash = CharField(max_length=255, null=False)
    created_at = DateTimeField(default=datetime.now)

    def set_password(self, password: str) -> None:
        """
        Устанавливает пароль пользователя, сохраняя только его хеш.

        Генерирует безопасный хеш через ``werkzeug.security``
        и записывает его в поле :attr:`password_hash`.
        Открытый пароль нигде не сохраняется.

        Args:
            password: Пароль в открытом виде.

        Returns:
            None
        """
        self.password_hash = generate_password_hash(password=password)

    def check_password(self, password: str) -> bool:
        """
        Проверяет, соответствует ли переданный пароль сохранённому хешу.

        Args:
            password: Пароль в открытом виде для проверки.

        Returns:
            True, если пароль верный, иначе False.
        """
        return check_password_hash(self.password_hash, password)