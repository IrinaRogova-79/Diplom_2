"""
Вспомогательные функции для API тестов
"""

import requests
import allure
from data import BASE_URL

def generate_unique_email():
    """Генерирует уникальный email для тестов"""
    import time
    return f"testuser_{int(time.time())}@yandex.ru"

@allure.step("Получение списка ингредиентов")
def get_ingredients():
    """Получает список актуальных ингредиентов с сервера"""
    url = f"{BASE_URL}/ingredients"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        ingredients = data.get("data", [])
        if ingredients:
            return [ingredient["_id"] for ingredient in ingredients[:2]]
    return []

@allure.step("Создание пользователя: {email}")
def create_user(email, password, name):
    """Создает пользователя через API"""
    url = f"{BASE_URL}/auth/register"
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    return requests.post(url, json=payload)

@allure.step("Логин пользователя: {email}")
def login_user(email, password):
    """Авторизует пользователя через API"""
    url = f"{BASE_URL}/auth/login"
    payload = {
        "email": email,
        "password": password
    }
    return requests.post(url, json=payload)

@allure.step("Создание заказа с ингредиентами: {ingredients}")
def create_order(ingredients, token=None):
    """Создает заказ через API"""
    url = f"{BASE_URL}/orders"
    headers = {}
    if token:
        headers["Authorization"] = token
    
    payload = {"ingredients": ingredients}
    return requests.post(url, json=payload, headers=headers)

@allure.step("Удаление пользователя")
def delete_user(token):
    """Удаляет пользователя через API"""
    url = f"{BASE_URL}/auth/user"
    headers = {"Authorization": token}
    return requests.delete(url, headers=headers)

@allure.step("Получение данных пользователя")
def get_user_data(token):
    """Получает данные пользователя через API"""
    url = f"{BASE_URL}/auth/user"
    headers = {"Authorization": token}
    return requests.get(url, headers=headers)