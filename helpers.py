"""
Вспомогательные функции для API тестов
"""

import requests
from data import BASE_URL


def generate_unique_email():
    import time
    return f"testuser_{int(time.time())}@yandex.ru"


def get_ingredients():
    url = f"{BASE_URL}/ingredients"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        ingredients = data.get("data", [])
        if ingredients:
            return [ingredient["_id"] for ingredient in ingredients[:2]]
    return []


def create_user(email, password, name):
    url = f"{BASE_URL}/auth/register"
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    return requests.post(url, json=payload)


def login_user(email, password):
    url = f"{BASE_URL}/auth/login"
    payload = {
        "email": email,
        "password": password
    }
    return requests.post(url, json=payload)


def create_order(ingredients, token=None):
    """Создает заказ через API"""
    url = f"{BASE_URL}/orders"
    headers = {}
    if token:
        headers["Authorization"] = token
    
    payload = {"ingredients": ingredients}
    return requests.post(url, json=payload, headers=headers)


def delete_user(token):
    url = f"{BASE_URL}/auth/user"
    headers = {"Authorization": token}
    return requests.delete(url, headers=headers)


def get_user_data(token):
    url = f"{BASE_URL}/auth/user"
    headers = {"Authorization": token}
    return requests.get(url, headers=headers)