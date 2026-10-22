from flask_login import UserMixin
from peewee import DateTimeField, CharField, Model
from werkzeug.security import check_password_hash, generate_password_hash

from .config import db


class BaseModel(Model):
    class Meta:
        database = db


class User(UserMixin, BaseModel):
    username = CharField(unique=True, max_length=25, index=True, null=False)
    password_hash = CharField()
