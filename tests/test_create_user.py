"""
Тесты для эндпоинта создания пользователя
POST /api/auth/register
"""

import pytest
import allure
import requests
from data import ERROR_MESSAGES
from helpers import create_user, generate_unique_email

@allure.feature("Создание пользователя")
class TestCreateUser:
    
    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self):
        email = generate_unique_email()
        password = "testpass123"
        name = "Test User"
        
        with allure.step(f"Отправка запроса на регистрацию с email: {email}"):
            response = create_user(email, password, name)
        
        with allure.step("Проверка статуса ответа 200"):
            assert response.status_code == 200
        
        data = response.json()
        with allure.step("Проверка наличия токена в ответе"):
            assert "accessToken" in data
            assert data["user"]["email"] == email
    
    @allure.title("Создание пользователя, который уже зарегистрирован")
    def test_create_existing_user(self, existing_user):
        email = existing_user["email"]
        password = existing_user["password"]
        name = existing_user["name"]
        
        with allure.step(f"Отправка запроса на регистрацию с существующим email: {email}"):
            response = create_user(email, password, name)
        
        with allure.step("Проверка статуса ответа 403"):
            assert response.status_code == 403
        
        data = response.json()
        with allure.step("Проверка сообщения об ошибке"):
            assert data["message"] == ERROR_MESSAGES["user_exists"]
    
    @allure.title("Создание пользователя без обязательного поля email")
    def test_create_user_without_email(self):
        password = "testpass123"
        name = "Test User"
        
        url = "https://stellarburgers.education-services.ru/api/auth/register"
        payload = {
            "password": password,
            "name": name
        }
        
        with allure.step("Отправка запроса на регистрацию без email"):
            response = requests.post(url, json=payload)
        
        with allure.step("Проверка статуса ответа 403"):
            assert response.status_code == 403
        
        data = response.json()
        with allure.step("Проверка сообщения об ошибке"):
            assert data["message"] == ERROR_MESSAGES["required_fields"]
    
    @allure.title("Создание пользователя без обязательного поля password")
    def test_create_user_without_password(self):
        email = generate_unique_email()
        name = "Test User"
        
        url = "https://stellarburgers.education-services.ru/api/auth/register"
        payload = {
            "email": email,
            "name": name
        }
        
        with allure.step("Отправка запроса на регистрацию без password"):
            response = requests.post(url, json=payload)
        
        with allure.step("Проверка статуса ответа 403"):
            assert response.status_code == 403
        
        data = response.json()
        with allure.step("Проверка сообщения об ошибке"):
            assert data["message"] == ERROR_MESSAGES["required_fields"]
    
    @allure.title("Создание пользователя без обязательного поля name")
    def test_create_user_without_name(self):
        email = generate_unique_email()
        password = "testpass123"
        
        url = "https://stellarburgers.education-services.ru/api/auth/register"
        payload = {
            "email": email,
            "password": password
        }
        
        with allure.step("Отправка запроса на регистрацию без name"):
            response = requests.post(url, json=payload)
        
        with allure.step("Проверка статуса ответа 403"):
            assert response.status_code == 403
        
        data = response.json()
        with allure.step("Проверка сообщения об ошибке"):
            assert data["message"] == ERROR_MESSAGES["required_fields"]