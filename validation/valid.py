def valid(login, password, password2) -> bool:
    if len(password) < 8:
        return False

    if password != password2:
        return False

    if len(login) <= 3:

        return False

    return True

