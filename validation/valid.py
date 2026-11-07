def valid(name, password, password2) -> bool:
    print(name, len(name))
    print(password, len(password))
    print(password2, len(password2))
    print(password == password2)

    if len(password) >= 8:
        return False

    if password != password2:
        return False

    if len(name) >= 3:

        return False

    return True

