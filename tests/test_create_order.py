"""
Тесты для эндпоинта создания заказа
POST /api/orders
"""

import pytest
import allure
from data import ERROR_MESSAGES
from helpers import create_order

@allure.feature("Создание заказа")
class TestCreateOrder:
    
    @allure.title("Создание заказа с авторизацией")
    def test_create_order_with_auth(self, auth_token, valid_ingredients):
        with allure.step(f"Отправка запроса на создание заказа с токеном и ингредиентами: {valid_ingredients}"):
            response = create_order(valid_ingredients, auth_token)
        
        data = response.json()
        
        assert response.status_code == 200
        assert data["success"] is True
        assert "order" in data
        assert "number" in data["order"]
    
    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth(self, valid_ingredients):
        with allure.step(f"Отправка запроса на создание заказа без токена с ингредиентами: {valid_ingredients}"):
            response = create_order(valid_ingredients)
        
        data = response.json()
        
        assert response.status_code == 200
        assert data["success"] is True
        assert "order" in data
        assert "number" in data["order"]
    
    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients(self, auth_token, valid_ingredients):
        with allure.step(f"Отправка запроса на создание заказа с валидными ингредиентами: {valid_ingredients}"):
            response = create_order(valid_ingredients, auth_token)
        
        data = response.json()
        
        assert response.status_code == 200
        assert data["success"] is True
    
    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self, auth_token):
        with allure.step("Отправка запроса на создание заказа без ингредиентов"):
            response = create_order([], auth_token)
        
        data = response.json()
        
        assert response.status_code == 400
        assert data["message"] == ERROR_MESSAGES["no_ingredients"]
    
    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_with_invalid_ingredients(self, auth_token, invalid_ingredients):
        with allure.step(f"Отправка запроса на создание заказа с невалидными хешами: {invalid_ingredients}"):
            response = create_order(invalid_ingredients, auth_token)
        
        assert response.status_code == 500