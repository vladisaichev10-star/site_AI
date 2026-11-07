from flask import request, flash, redirect, render_template

from database import create_user


def valid():
    if request.method == "POST":
        name = request.form.get("name")
        login = request.form.get("login")
        password = request.form.get("password")
        password2 = request.form.get("password2")

        if len(password) <= 8:
            flash(message="Пароль не должен меньше 8 символов", category="error")
            redirect("/register")

        if password != password2:
            flash(message="Пароли не совпадают")

        if len(name) <= 3:
            flash(message="Имя не должно быть менее 3 символов")

        if len(login) <= 5:
            flash(message="Логин не может быть меньше 5 символов")

        create_user(username=login, password=password)
    else:
        return render_template("register.html")