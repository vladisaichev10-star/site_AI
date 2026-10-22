# Todo Использовать ленивый сетере и гшеттер (@property @setter)
# Todo Анотация и докуаментация
# Todo Создать crud и функцию создания бд (create_tables)
from datetime import datetime

from flask_login import UserMixin
from peewee import DateTimeField, CharField, Model
from werkzeug.security import check_password_hash, generate_password_hash

from .config import db


class BaseModel(Model):
    """Базовая модель всех таблиц в бд"""

    class Meta:
        database = db


class User(UserMixin, BaseModel):
    username = CharField(unique=True, max_length=25, index=True, null=False)
    password_hash = CharField(max_length=15, null=False)
    created_at = DateTimeField(default=datetime.now())

    def set_password(self, password):
        self.password_hash = generate_password_hash(password=password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
