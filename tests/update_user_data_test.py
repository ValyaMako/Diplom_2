import pytest
from data.user_data import *
from conftest import user
from api_methods import User


class TestUpdateUserData:
    @pytest.mark.parametrize("new_data, expected_field", [
        (get_new_email(), "email"),
        (get_new_name(), "name")
    ])
    @allure.title('Изменение имени и почты авторизованного пользователя')
    def test_update_user_data_with_login(self, user, new_data, expected_field):
        email_pass, _, _, access_token = user
        update_response = User.update_user_data(new_data, access_token)
        assert update_response.status_code == 200
        assert update_response.json()["user"][expected_field] == new_data[expected_field]

    @pytest.mark.parametrize("new_password", [get_new_password()])
    @allure.title('Изменение пароля авторизованного пользователя - в качесте подтверждения авторизуем его')
    def test_update_user_password_with_login(self, user, new_password):
        email_pass, _, _, access_token = user
        new_auth_data = {"email": email_pass[0], "password": new_password["password"]}
        update_response = User.update_user_data(new_password, access_token)
        assert update_response.status_code == 200

        login_response = User.login_user(new_auth_data)
        assert login_response.status_code == 200

    @pytest.mark.parametrize("new_data, expected_field", [
        (get_new_email(), "email"),
        (get_new_password(), "password"),
        (get_new_name(), "name")
    ])
    @allure.title('Изменение имени и почты неавторизованного пользователя')
    def test_update_user_data_without_login(self, user, new_data, expected_field):
        access_token = ""
        update_response = User.update_user_data(new_data, access_token)
        assert update_response.status_code == 401
        assert update_response.json() == update_user
