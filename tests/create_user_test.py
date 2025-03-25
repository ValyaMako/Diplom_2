import pytest
from conftest import user
from api_methods import User
from data.user_data import *


class TestCreateUser:

    @allure.title('Проверяем создание пользователя')
    @allure.description('В качестве подтверждения создания пользователя авторизуем его')
    def test_create_user(self):
        data = get_user_data()
        email_pass, reg_response = User.register_user(data)
        assert reg_response.status_code == 200
        assert reg_response.json()["success"]
        auth_data = get_auth_data(email_pass)
        login_response = User.login_user(auth_data)
        access_token = (login_response.json())["accessToken"]
        assert login_response.status_code == 200
        assert login_response.json()["success"]
        User.delete_user(access_token)


    @allure.title('Проверяем, что нельзя создать двух одинаковых пользователей')
    def test_create_identical_user_show_error(self, user):
        email_pass, reg_response, _, _ = user
        email = email_pass[0]
        password = email_pass[1]
        name = email_pass[2]
        register_data = get_register_data(email, password, name)
        _, second_reg_response = User.register_user(register_data)
        assert second_reg_response.status_code == 403
        assert second_reg_response.json()["message"] in create_user_expected_messages

    @pytest.mark.parametrize("invalid_data", [invalid_data_without_email(), invalid_data_without_password(), invalid_data_without_name()])
    @allure.title('Проверяем, что запрос возвращает ошибку, если нет одного из обязательных полей')
    def test_create_user_without_field_show_error(self, invalid_data):
        _, reg_response = User.register_user(invalid_data)
        assert reg_response.status_code == 403
        assert reg_response.json()["message"] in create_user_expected_messages
