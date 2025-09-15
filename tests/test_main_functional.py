import allure
import pytest

from pages.main_page import MainPage
from pages.orders_feed_page import OrdersFeedPage


@allure.epic("Основная функциональность")
@allure.feature("Навигация и взаимодействие")
class TestMainFunctional:

    @allure.title("Переход в 'Ленту заказов' по клику")
    @allure.description("Проверить, что при клике на 'Лента заказов' открывается соответствующая страница")
    def test_switch_by_click_to_orders_feed(self, driver):
        main_page = MainPage(driver)
        orders_feed = OrdersFeedPage(driver)
        main_page.click_by_link_orders_feed()
        assert orders_feed.is_orders_feed_page_opened()

    @allure.title("Возврат в 'Конструктор' из 'Ленты заказов'")
    @allure.description("Проверить, что при клике на 'Конструктор' возвращаемся на главную страницу")
    def test_switch_by_click_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_by_link_orders_feed()
        main_page.click_by_link_constructor()
        assert main_page.is_main_page_opened()

    @allure.title("Открытие модального окна при клике на ингредиент")
    @allure.description("Проверить, что при клике на ингредиент появляется модальное окно с деталями")
    def test_by_click_to_ingredient_opened_modal_window_ingredients(self, driver):
        main_page = MainPage(driver)
        main_page.click_by_ingredient()
        assert main_page.is_ingredient_modal_visible()

    @allure.title("Закрытие модального окна ингредиента по крестику")
    @allure.description("Проверить, что модальное окно закрывается кликом по кнопке 'крестик'")
    def test_by_click_to_button_close_modal_ing(self, driver):
        main_page = MainPage(driver)
        main_page.click_by_ingredient()
        main_page.click_by_button_close_modal_ing()
        assert main_page.is_ingredient_modal_hidden()

    @allure.title("Счётчик булочки увеличивается после добавления в заказ")
    @allure.description("Проверить, что при добавлении булочки в конструктор счётчик увеличивается")
    def test_upgrade_counter_bun_after_add_basket(self, driver):
        main_page = MainPage(driver)
        prev_counter = main_page.check_counter_bun()
        main_page.drag_bun_to_basket()
        new_counter = main_page.check_counter_bun()
        assert new_counter > prev_counter

