"""
Тестовые данные для API тестов Stellar Burgers
"""

BASE_URL = "https://stellarburgers.education-services.ru/api"

TEST_USER_EMAIL = "testuser_@yandex.ru"
TEST_USER_PASSWORD = "testpassword123"
TEST_USER_NAME = "Test User"

INVALID_EMAIL = "invalid@email.com"
INVALID_PASSWORD = "wrongpassword"

ERROR_MESSAGES = {
    "user_exists": "User already exists",
    "required_fields": "Email, password and name are required fields",
    "invalid_credentials": "email or password are incorrect",
    "no_ingredients": "Ingredient ids must be provided",
    "unauthorized": "You should be authorised"
}