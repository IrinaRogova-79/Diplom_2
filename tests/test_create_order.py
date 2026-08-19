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
    @allure.step("Отправка запроса на создание заказа с токеном")
    def test_create_order_with_auth(self, auth_token, valid_ingredients):
        response = create_order(valid_ingredients, auth_token)
        
        @allure.step("Проверка статуса ответа 200")
        def check_status():
            assert response.status_code == 200
        
        @allure.step("Проверка наличия номера заказа")
        def check_order_number():
            data = response.json()
            assert data["success"] is True
            assert "order" in data
            assert "number" in data["order"]
        
        check_status()
        check_order_number()
    
    @allure.title("Создание заказа без авторизации")
    @allure.step("Отправка запроса на создание заказа без токена")
    def test_create_order_without_auth(self, valid_ingredients):
        response = create_order(valid_ingredients)
        
        @allure.step("Проверка статуса ответа 200")
        def check_status():
            assert response.status_code == 200
        
        @allure.step("Проверка наличия номера заказа")
        def check_order_number():
            data = response.json()
            assert data["success"] is True
            assert "order" in data
            assert "number" in data["order"]
        
        check_status()
        check_order_number()
    
    @allure.title("Создание заказа с ингредиентами")
    @allure.step("Отправка запроса на создание заказа с валидными ингредиентами")
    def test_create_order_with_ingredients(self, auth_token, valid_ingredients):
        response = create_order(valid_ingredients, auth_token)
        
        @allure.step("Проверка статуса ответа 200")
        def check_status():
            assert response.status_code == 200
        
        @allure.step("Проверка успешного создания заказа")
        def check_success():
            data = response.json()
            assert data["success"] is True
        
        check_status()
        check_success()
    
    @allure.title("Создание заказа без ингредиентов")
    @allure.step("Отправка запроса на создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self, auth_token):
        response = create_order([], auth_token)
        
        @allure.step("Проверка статуса ответа 400")
        def check_status():
            assert response.status_code == 400
        
        @allure.step("Проверка сообщения об ошибке")
        def check_error_message():
            data = response.json()
            assert data["message"] == ERROR_MESSAGES["no_ingredients"]
        
        check_status()
        check_error_message()
    
    @allure.title("Создание заказа с неверным хешем ингредиентов")
    @allure.step("Отправка запроса на создание заказа с невалидными хешами")
    def test_create_order_with_invalid_ingredients(self, auth_token, invalid_ingredients):
        response = create_order(invalid_ingredients, auth_token)
        
        @allure.step("Проверка статуса ответа 500")
        def check_status():
            assert response.status_code == 500
        
        check_status()