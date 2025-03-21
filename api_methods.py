import allure
import requests
import urls


class User:
    @staticmethod
    @allure.step('Метод регистрации нового пользователя возвращает ответ на запрос и список из email, пароля и имени')
    def register_user(data):
        email_pass = []
        reg_response = requests.post(urls.register_user, json=data)
        if reg_response.status_code == 200:
            email_pass.append(data["email"])
            email_pass.append(data["password"])
            email_pass.append(data["name"])
        else:
            print(f"Ошибка регистрации: {reg_response.status_code}, {reg_response.text}")
        return email_pass, reg_response

    @staticmethod
    @allure.step('Метод авторизации пользователя')
    def login_user(auth_data):
        login_response = requests.post(urls.login_user, json=auth_data)
        return login_response

    @staticmethod
    @allure.step('Метод удаления пользователя')
    def delete_user(access_token):
        del_response = requests.delete(urls.user, headers={'Authorization': access_token})
        return del_response

    @staticmethod
    @allure.step('Метод замены данных пользователя')
    def update_user_data(new_data, access_token):
        update_response = requests.patch(urls.user, json=new_data, headers={'Authorization': access_token})
        return update_response

class Order:
    @staticmethod
    @allure.step('Метод получения данных об ингредиентах')
    def get_ingredients():
        ing_response = requests.get(urls.ingredients)
        if ing_response.status_code == 200:
            response_data = ing_response.json()
            ing_ids = [item["_id"] for item in response_data["data"]]
            return ing_ids

    @staticmethod
    @allure.step('Метод создания заказа')
    def create_order(data, access_token):
        order_response = requests.post(urls.order, json=data, headers={'Authorization': access_token})
        return order_response

    @staticmethod
    @allure.step('Получить заказы конкретного пользователя')
    def get_orders(access_token):
        orders_response = requests.get(urls.order, headers={'Authorization': access_token})
        return orders_response
