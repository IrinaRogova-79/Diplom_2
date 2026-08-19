"""
Тесты для эндпоинта логина пользователя
POST /api/auth/login
"""

import pytest
import allure
from data import ERROR_MESSAGES, INVALID_EMAIL, INVALID_PASSWORD
from helpers import login_user


@allure.feature("Логин пользователя")
class TestLoginUser:
    
    @allure.title("Вход под существующим пользователем")
    @allure.step("Отправка запроса на логин с корректными данными")
    def test_login_existing_user(self, test_user):
        email = test_user["email"]
        password = test_user["password"]
        
        response = login_user(email, password)
        
        @allure.step("Проверка статуса ответа 200")
        def check_status():
            assert response.status_code == 200
        
        @allure.step("Проверка наличия токена в ответе")
        def check_token():
            data = response.json()
            assert "accessToken" in data
            assert data["user"]["email"] == email
        
        check_status()
        check_token()
    
    @allure.title("Вход с неверным логином")
    @allure.step("Отправка запроса на логин с неверным email")
    def test_login_with_invalid_email(self, test_user):
        password = test_user["password"]
        
        response = login_user(INVALID_EMAIL, password)
        
        @allure.step("Проверка статуса ответа 401")
        def check_status():
            assert response.status_code == 401
        
        @allure.step("Проверка сообщения об ошибке")
        def check_error_message():
            data = response.json()
            assert data["message"] == ERROR_MESSAGES["invalid_credentials"]
        
        check_status()
        check_error_message()
    
    @allure.title("Вход с неверным паролем")
    @allure.step("Отправка запроса на логин с неверным паролем")
    def test_login_with_invalid_password(self, test_user):
        email = test_user["email"]
        
        response = login_user(email, INVALID_PASSWORD)
        
        @allure.step("Проверка статуса ответа 401")
        def check_status():
            assert response.status_code == 401
        
        @allure.step("Проверка сообщения об ошибке")
        def check_error_message():
            data = response.json()
            assert data["message"] == ERROR_MESSAGES["invalid_credentials"]
        
        check_status()
        check_error_message()
    
    @allure.title("Вход с неверным логином и паролем")
    @allure.step("Отправка запроса на логин с неверными данными")
    def test_login_with_invalid_credentials(self):
        response = login_user(INVALID_EMAIL, INVALID_PASSWORD)
        
        @allure.step("Проверка статуса ответа 401")
        def check_status():
            assert response.status_code == 401
        
        @allure.step("Проверка сообщения об ошибке")
        def check_error_message():
            data = response.json()
            assert data["message"] == ERROR_MESSAGES["invalid_credentials"]
        
        check_status()
        check_error_message()