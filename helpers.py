import allure
from faker import Faker


@allure.step('Генерируем логин, пароль и имя пользователя')
def generate_user_data():
    fake = Faker()
    email = fake.email()
    password = fake.password()
    name = fake.name()
    return email, password, name
