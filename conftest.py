import pytest
from data.user_data import *
from data.order_data import *
from api_methods import User, Order


@pytest.fixture
def user():
    data = get_user_data()
    email_pass, reg_response = User.register_user(data)
    auth_data = get_auth_data(email_pass)
    login_response = User.login_user(auth_data)
    access_token = (login_response.json())["accessToken"]

    yield email_pass, reg_response, login_response, access_token

    User.delete_user(access_token)

@pytest.fixture
def order(user):
    *_, access_token = user
    ing_ids = Order.get_ingredients()
    ingredients_for_order = get_ing_for_order(ing_ids)
    Order.create_order(ingredients_for_order, access_token)
