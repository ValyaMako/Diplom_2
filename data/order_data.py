import allure
import random


@allure.step('Получаем тело запроса для успешного создания заказа из трёх ингредиентов')
def get_ing_for_order(ing_ids):
    ingredients_for_order = []
    if ing_ids and len(ing_ids) >= 3:
        ingredients_for_order = random.sample(ing_ids, 3)
    return {"ingredients": ingredients_for_order}

@allure.step('Меняем в правильном хеше первый символ на W')
def convert_to_wrong_hash(correct_hash):
    return correct_hash[1:] + 'W'

@allure.step('Получаем тело запроса создания заказа из трёх ингредиентов, хеш которых переделали')
def get_wrong_ing_for_order(ing_ids):
    wrong_hashes = [convert_to_wrong_hash(h) for h in ing_ids]
    ingredients_for_order = []
    if ing_ids and len(ing_ids) >= 3:
        ingredients_for_order = random.sample(wrong_hashes, 3)
    return {"ingredients": ingredients_for_order}

get_orders = {
"success": False,
"message": "You should be authorised"
}
