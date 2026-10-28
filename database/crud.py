from .config import db
from .models import User




def create_user(username: str, password: str) -> User:
    """
    Создание пользователя

    :param username:
    :param password:
    :return:
    """
    user = User(username=username)
    user.set_password(password=password)

    user.save()
    return user

def create_tables():
    db.connect()

    db.create_tables([User])

