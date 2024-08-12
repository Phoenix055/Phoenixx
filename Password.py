
def check_length(password):
    if len(password) < 8 or len(password) > 17:
        return "Пароль должен быть длиной от 8 до 17 символов."
    return True


def check_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return "Пароль должен содержать как минимум одну цифру."


def check_underscores(password):
    for char in password:
        if not char.isalnum() and char != "_":
            return "Пароль должен содержать только буквы, цифры и нижние подчеркивания."
    return True


def check_password(password):
    length_check = check_length(password)
    if length_check != True:
        return length_check

    digit_check = check_digit(password)
    if digit_check != True:
        return digit_check

    underscores_check = check_underscores(password)
    if underscores_check != True:
        return underscores_check

while True:
    a = check_password(input('Password '))
    print(a)
