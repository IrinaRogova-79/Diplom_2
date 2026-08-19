"""
Тесты для эндпоинта создания пользователя
POST /api/auth/register
"""

import pytest
import allure
from data import ERROR_MESSAGES
from helpers import create_user, generate_unique_email


@allure.feature("Создание пользователя")
class TestCreateUser:
    
    @allure.title("Создание уникального пользователя")
    @allure.step("Отправка запроса на регистрацию с уникальными данными")
    def test_create_unique_user(self):
        email = generate_unique_email()
        password = "testpass123"
        name = "Test User"
        
        response = create_user(email, password, name)
        
        @allure.step("Проверка статуса ответа")
        def check_status():
            assert response.status_code == 200
        
        @allure.step("Проверка наличия токена в ответе")
        def check_token():
            data = response.json()
            assert "accessToken" in data
            assert data["user"]["email"] == email
        
        check_status()
        check_token()
    
    @allure.title("Создание пользователя, который уже зарегистрирован")
    @allure.step("Отправка запроса на регистрацию с существующим email")
    def test_create_existing_user(self, existing_user):
        email = existing_user["email"]
        password = existing_user["password"]
        name = existing_user["name"]
        
        response = create_user(email, password, name)
        
        @allure.step("Проверка статуса ответа 403")
        def check_status():
            assert response.status_code == 403
        
        @allure.step("Проверка сообщения об ошибке")
        def check_error_message():
            data = response.json()
            assert data["message"] == ERROR_MESSAGES["user_exists"]
        
        check_status()
        check_error_message()
    
    @allure.title("Создание пользователя без обязательного поля email")
    @allure.step("Отправка запроса на регистрацию без email")
    def test_create_user_without_email(self):
        password = "testpass123"
        name = "Test User"
        
        url = "https://stellarburgers.education-services.ru/api/auth/register"
        payload = {
            "password": password,
            "name": name
        }
        import requests
        response = requests.post(url, json=payload)
        
        @allure.step("Проверка статуса ответа 403")
        def check_status():
            assert response.status_code == 403
        
        @allure.step("Проверка сообщения об ошибке")
        def check_error_message():
            data = response.json()
            assert data["message"] == ERROR_MESSAGES["required_fields"]
        
        check_status()
        check_error_message()
    
    @allure.title("Создание пользователя без обязательного поля password")
    @allure.step("Отправка запроса на регистрацию без password")
    def test_create_user_without_password(self):
        email = generate_unique_email()
        name = "Test User"
        
        url = "https://stellarburgers.education-services.ru/api/auth/register"
        payload = {
            "email": email,
            "name": name
        }
        import requests
        response = requests.post(url, json=payload)
        
        @allure.step("Проверка статуса ответа 403")
        def check_status():
            assert response.status_code == 403
        
        @allure.step("Проверка сообщения об ошибке")
        def check_error_message():
            data = response.json()
            assert data["message"] == ERROR_MESSAGES["required_fields"]
        
        check_status()
        check_error_message()
    
    @allure.title("Создание пользователя без обязательного поля name")
    @allure.step("Отправка запроса на регистрацию без name")
    def test_create_user_without_name(self):
        email = generate_unique_email()
        password = "testpass123"
        
        url = "https://stellarburgers.education-services.ru/api/auth/register"
        payload = {
            "email": email,
            "password": password
        }
        import requests
        response = requests.post(url, json=payload)
        
        @allure.step("Проверка статуса ответа 403")
        def check_status():
            assert response.status_code == 403
        
        @allure.step("Проверка сообщения об ошибке")
        def check_error_message():
            data = response.json()
            assert data["message"] == ERROR_MESSAGES["required_fields"]
        
        check_status()
        check_error_message()