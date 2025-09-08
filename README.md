# Дипломный проект. 3 задание
# Вятских Илья
# Когорта 27FS
# 🛵 UI-тесты для Stellar Burgers
Проект по автоматизированному тестированию пользовательского интерфейса сервиса Stellar Burgers — платформы для заказа бургеров.

Тесты реализованы с использованием Selenium WebDriver, паттерна Page Object и генерации отчётов в Allure.

---

## 🧪 Тестируемые сценарии
### 1. Навигация между разделами
- ✅ test_switch_by_click_to_orders_feed — переход в раздел «Лента заказов»
- ✅ test_switch_by_click_to_constructor — возврат в «Конструктор»
### 2. Работа с модальным окном ингредиента
- ✅ test_by_click_to_ingredient_opened_modal_window_ingredients — открытие модального окна при клике на ингредиент
- ✅ test_by_click_to_button_close_modal_ing — закрытие модального окна по крестику
### 3. Добавление ингредиентов и проверка счётчиков
- ✅ test_upgrade_counter_bun_after_add_basket — счётчик булочки увеличивается после добавления
- ✅ test_upgrade_counter_orders — счётчики «Выполнено за всё время» и «за сегодня» увеличиваются после заказа
### 4. Проверка ленты заказов
- ✅ test_visible_order_number_in_progress — номер заказа появляется в разделе «В работе»

--- 

## 🗂 Структура проекта
```
Diplom_3/
├── data/                     # 📄 Константы и тестовые данные
│   ├── __init__.py
│   ├── data.py              # 🧩 Тексты модальных окон, заголовки
│   └── urls.py              # 🌐 URL приложения
│
├── locators/                 # 🎯 Локаторы элементов
│   ├── __init__.py
│   ├── auth_page_locators.py     # 🔐 Локаторы страницы авторизации
│   ├── main_page_locators.py     # 🍔 Локаторы главной страницы
│   ├── ingredient_modal_locators.py  # 📦 Локаторы модального окна ингредиента
│   ├── succ_order_modal_locators.py  # ✅ Локаторы модального окна успеха заказа
│   └── order_feed_locators.py    # 📊 Локаторы ленты заказов
│
├── pages/                    # 🧩 Page Object классы
│   ├── __init__.py
│   ├── base_page.py         # 🧱 Базовый класс с общими методами
│   ├── auth_page.py         # 👤 Страница авторизации
│   ├── main_page.py         # 🏠 Главная страница
│   └── orders_feed_page.py  # 📋 Лента заказов
│
├── tests/                    # ✅ Автотесты
│   ├── __init__.py
│   ├── conftest.py          # 🔁 Фикстуры: driver, login
│   ├── test_main_functional.py     # 🔄 Тесты навигации и модальных окон
│   └── test_orders_feed.py         # 📈 Тесты счётчиков и ленты заказов
│
├── reports/                  # 📊 Результаты Allure
│   └── allure-results/
│
├── .gitignore               # 🚫 Игнорируемые файлы
├── requirements.txt          # ⚙️ Зависимости: selenium, pytest, allure-pytest
├── pytest.ini                # 🛠 Конфигурация Pytest
└── README.md                 # 📘 Этот файл
```