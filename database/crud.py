from .config import db
from .models import User




def create_user(login: str, password: str) -> User:
    """
    Создание пользователя

    :param username:
    :param password:
    :return:
    """
    user = User(login=login)
    user.set_password(password=password)

    user.save()
    return user

def create_tables():
    db.connect()

    db.create_tables([User])

def get_user(login: str):
    user = User.get_or_none(User.login == login)
    print(user)
    return user

