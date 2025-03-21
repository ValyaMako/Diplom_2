from conftest import user, order
from api_methods import Order
from data.order_data import *


class TestGetOrders:

    @allure.title('Получение заказов авторизованного пользователя')
    def test_get_orders_with_auth(self, user, order):
        _, _, _, access_token = user
        get_orders_response = Order.get_orders(access_token)
        assert get_orders_response.status_code == 200
        assert get_orders_response.json()["success"] is True

    @allure.title('Получение заказов неавторизованного пользователя')
    def test_get_orders_without_auth(self, user, order):
        access_token = ""
        get_orders_response = Order.get_orders(access_token)
        assert get_orders_response.status_code == 401
        assert get_orders_response.json() == get_orders
