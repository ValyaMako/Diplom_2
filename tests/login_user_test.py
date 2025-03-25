import pytest
from data.user_data import *
from conftest import user
from api_methods import User


class TestLoginUser:
    @allure.title('Проверяем, что пользователь может авторизоваться')
    def test_user_login_success(self, user):
        _, _, login_response, _ = user
        assert login_response.status_code == 200
        assert login_response.json()["success"]

    @pytest.mark.parametrize("invalid_auth_data", [get_auth_data_wrong_email, get_auth_data_wrong_password])
    @allure.title('Проверяем, что запрос возвращает ошибку, если неверно указаны логин или пароль')
    def test_courier_login_wrong_login_or_password_error(self, user, invalid_auth_data):
        email_name_pass, _, _, _ = user
        wrong_auth_data = invalid_auth_data(email_name_pass)
        auth_response = User.login_user(wrong_auth_data)
        assert auth_response.status_code == 401
        assert auth_response.json() == auth_courier