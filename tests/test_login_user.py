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
    def test_login_existing_user(self, test_user):
        email = test_user["email"]
        password = test_user["password"]
        
        with allure.step(f"Отправка запроса на логин с email: {email}"):
            response = login_user(email, password)
        
        data = response.json()
        
        assert response.status_code == 200
        assert "accessToken" in data
        assert data["user"]["email"] == email
    
    @allure.title("Вход с неверным логином")
    def test_login_with_invalid_email(self, test_user):
        password = test_user["password"]
        
        with allure.step(f"Отправка запроса на логин с неверным email: {INVALID_EMAIL}"):
            response = login_user(INVALID_EMAIL, password)
        
        data = response.json()
        
        assert response.status_code == 401
        assert data["message"] == ERROR_MESSAGES["invalid_credentials"]
    
    @allure.title("Вход с неверным паролем")
    def test_login_with_invalid_password(self, test_user):
        email = test_user["email"]
        
        with allure.step(f"Отправка запроса на логин с неверным паролем"):
            response = login_user(email, INVALID_PASSWORD)
        
        data = response.json()
        
        assert response.status_code == 401
        assert data["message"] == ERROR_MESSAGES["invalid_credentials"]
    
    @allure.title("Вход с неверным логином и паролем")
    def test_login_with_invalid_credentials(self):
        with allure.step(f"Отправка запроса на логин с неверными данными"):
            response = login_user(INVALID_EMAIL, INVALID_PASSWORD)
        
        data = response.json()
        
        assert response.status_code == 401
        assert data["message"] == ERROR_MESSAGES["invalid_credentials"]