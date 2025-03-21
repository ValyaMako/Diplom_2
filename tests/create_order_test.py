from conftest import user
from api_methods import Order
from data.order_data import *


class TestCreateUser:

    @allure.title('Создание заказа с ингредиентами авторизованным пользователем')
    def test_create_order_with_ingredients_and_auth_success(self, user):
        _, _, _, access_token = user
        ing_ids = Order.get_ingredients()
        ingredients_for_order = get_ing_for_order(ing_ids)
        order_response = Order.create_order(ingredients_for_order, access_token)
        assert order_response.status_code == 200
        assert order_response.json()["success"] is True

    @allure.title('Создание заказа с ингредиентами неавторизованным пользователем')
    def test_create_order_with_ingredients_without_auth_error(self, user):
        access_token = ""
        ing_ids = Order.get_ingredients()
        ingredients_for_order = get_ing_for_order(ing_ids)
        order_response = Order.create_order(ingredients_for_order, access_token)
        assert order_response.status_code == 400
        assert order_response.json()["success"] is False

    @allure.title('Создание заказа без ингредиентов авторизованным пользователем')
    def test_create_order_without_ingredients_error(self, user):
        _, _, _, access_token = user
        ingredients_for_order = []
        order_response = Order.create_order(ingredients_for_order, access_token)
        assert order_response.status_code == 400
        assert order_response.json()["success"] is False

    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_create_order_with_wrong_ingredients_error(self, user):
        _, _, _, access_token = user
        ing_ids = Order.get_ingredients()
        ingredients_for_order = get_wrong_ing_for_order(ing_ids)
        order_response = Order.create_order(ingredients_for_order, access_token)
        assert order_response.status_code == 500
