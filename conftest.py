"""
Фикстуры для API тестов
"""

import pytest
from data import TEST_USER_PASSWORD, TEST_USER_NAME
from helpers import create_user, delete_user, generate_unique_email, get_ingredients

@pytest.fixture
def test_user():
    """Создает тестового пользователя и возвращает его данные"""
    email = generate_unique_email()
    password = TEST_USER_PASSWORD
    name = TEST_USER_NAME
    
    response = create_user(email, password, name)
    # Убираем assert — фикстура только готовит данные
    
    data = response.json()
    token = data.get("accessToken")
    
    yield {
        "email": email,
        "password": password,
        "name": name,
        "token": token,
        "refreshToken": data.get("refreshToken")
    }
    
    # Удаляем пользователя после теста
    if token:
        delete_user(token)

@pytest.fixture
def auth_token(test_user):
    """Возвращает токен авторизации тестового пользователя"""
    return test_user["token"]

@pytest.fixture
def existing_user():
    """Создает пользователя, который уже существует в системе"""
    email = "testuser_fixed@yandex.ru"
    password = TEST_USER_PASSWORD
    name = TEST_USER_NAME
    
    response = create_user(email, password, name)
    if response.status_code == 200:
        data = response.json()
        token = data.get("accessToken")
        yield {
            "email": email,
            "password": password,
            "name": name,
            "token": token
        }
        delete_user(token)
    else:
        yield {
            "email": email,
            "password": password,
            "name": name,
            "token": None
        }

@pytest.fixture
def valid_ingredients():
    """Возвращает валидные хеши ингредиентов"""
    ingredients = get_ingredients()
    if not ingredients:
        pytest.skip("Не удалось получить ингредиенты с сервера")
    return ingredients

@pytest.fixture
def invalid_ingredients():
    """Возвращает невалидные хеши ингредиентов"""
    return ["invalid_hash_1", "invalid_hash_2"]