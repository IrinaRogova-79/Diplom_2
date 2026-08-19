# Автотесты для API Stellar Burgers

## Описание проекта
Проект содержит автотесты для API сервиса Stellar Burgers (https://stellarburgers.education-services.ru/).

## Тестируемые эндпоинты
- **Создание пользователя** (`POST /api/auth/register`)
- **Логин пользователя** (`POST /api/auth/login`)
- **Создание заказа** (`POST /api/orders`)

## Структура проекта
Diplom_1/
├── .gitignore # Исключаемые файлы
├── requirements.txt # Зависимости
├── README.md # Документация
├── conftest.py # Фикстуры
├── helpers.py # Вспомогательные функции
├── data.py # Тестовые данные
├── allure_results/ # Результаты Allure
└── tests/
├── init.py
├── test_create_user.py # Тесты создания пользователя
├── test_login_user.py # Тесты логина
└── test_create_order.py # Тесты создания заказа

## Установка и запуск

### 1. Установка зависимостей
```bash
pip install -r requirements.txt