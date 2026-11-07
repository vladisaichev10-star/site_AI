def valid(name, password, password2) -> bool:

    if len(password) <= 8:
        return False

    if password != password2:
        return False

    if len(name) <= 3:

        return False

    return True

