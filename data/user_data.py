from helpers import *
import allure


@allure.step('Получаем тело запроса для успешной регистрации пользователя')
def get_user_data():
    email, password, name = generate_user_data()
    return {
        "email": email,
        "password": password,
        "name": name
    }

@allure.step('Получаем тело запроса для успешной авторизации пользователя')
def get_auth_data(email_pass):
    if len(email_pass) < 2:
        raise ValueError("Недостаточно данных для авторизации.")
    return {
        "email": email_pass[0],
        "password": email_pass[1]
    }

@allure.step('Получаем тело запроса для повторной регистрации пользователя')
def get_register_data(email, password, name):
    return {
        "email": email,
        "password": password,
        "name": name
    }

@allure.step('Получаем тело запроса для регистрации пользователя без email')
def invalid_data_without_email():
    _, password, name = generate_user_data()
    return {
        "email": "",
        "password": password,
        "name": name
    }

@allure.step('Получаем тело запроса для регистрации пользователя без пароля')
def invalid_data_without_password():
    email, _, name = generate_user_data()
    return {
        "email": email,
        "password": "",
        "name": name
    }

@allure.step('Получаем тело запроса для регистрации пользователя без имени')
def invalid_data_without_name():
    email, password, _ = generate_user_data()
    return {
        "email": email,
        "password": password,
        "name": ""
    }

allure.step('Получаем тело запроса для авторизации пользователя с неверным email')
def get_auth_data_wrong_email( email_pass):
    email, _, _ = generate_user_data()
    return {
        "email": email,
        "password": email_pass[1],
    }
@allure.step('Получаем тело запроса для авторизации пользователя с неверным паролем')
def get_auth_data_wrong_password(email_pass):
    _, password, _ = generate_user_data()
    return {
        "email": email_pass[0],
        "password": password,
    }

@allure.step('Получаем новый email')
def get_new_email():
    email, _, _ = generate_user_data()
    return {"email": email}

@allure.step('Получаем новый пароль')
def get_new_password():
    _, password, _ = generate_user_data()
    return {"password": password}

@allure.step('Получаем новое имя пользователя')
def get_new_name():
    _, _, name = generate_user_data()
    return {"name": name}

create_user_expected_messages = [
    "User already exists",
    "Email, password and name are required fields"
]

auth_courier = {
"success": False,
"message": "email or password are incorrect"
}

update_user = {
    "success": False,
    "message": "You should be authorised"
}
