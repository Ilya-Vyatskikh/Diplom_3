import allure

from locators.main_page_locators import MainPageLocators
from locators.ingredient_modal_locators import IngredientLocators
from locators.succ_order_modal_locators import SuccessOrderModalLocators
from pages.base_page import BasePage
from data.urls import *


class MainPage(BasePage):

    @allure.step('Дождаться загрузки страницы')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)

    @allure.step('Кликнуть по ссылке "Лента заказов"')
    def click_by_link_orders_feed(self):
        self.click_on_element(MainPageLocators.LINK_ORDER_FEED)

    @allure.step('Кликнуть по ссылке "Конструктор"')
    def click_by_link_constructor(self):
        self.click_on_element(MainPageLocators.LINK_CONSTRUCT)

    @allure.step('Кликнуть по ингредиенту "Краторная булка N-200i"')
    def click_by_ingredient(self):
        self.click_on_element(MainPageLocators.BUN_KRATOR)

    @allure.step('Проверяем, что модальное окно "Детали ингредиентов" открыто')
    def is_ingredient_modal_visible(self):
        return self.wait_for_element_visible(IngredientLocators.WINDOW_MODAL_ING)

    @allure.step('Закрываем модальное окно ингредиента по крестику')
    def click_by_button_close_modal_ing(self):
        self.click_on_element(IngredientLocators.BUTTON_CLOSE_MODAL_ING)

    @allure.step('Проверяем, что модальное окно "Детали ингредиентов" становиться невидимым')
    def is_ingredient_modal_hidden(self):
        return self.wait_for_element_hide(IngredientLocators.WINDOW_MODAL_ING)

    @allure.step('Перетаскиваем булочку в корзину')
    def drag_bun_to_basket(self):
        source = self.wait_for_element_visible(MainPageLocators.BUN_KRATOR)
        target = self.wait_for_element_visible(MainPageLocators.POS_TOP_BASKET)
        self.drag_and_drop_element(source, target)

    @allure.step('Проверяем, что счётчик булочки увеличился')
    def check_counter_bun(self):
        counter_element = self.wait_for_element_visible(MainPageLocators.COUNTER_BUN)
        return int(counter_element.text)

    @allure.step('Нажимаем кнопку "Оформить заказ"')
    def click_order_button(self):
        self.click_on_element(MainPageLocators.BUT_ORDER)

    @allure.step('Проверяем, что модальное окно "Ваш заказ начали готовить" открыто')
    def is_order_success_modal_visible(self):
        return self.wait_for_element_visible(SuccessOrderModalLocators.ORDER_SUCCESS_NUMBER)

    @allure.step('Ждем когда модальное окно заказа пропадет после закрытия')
    def wait_for_order_success_modal_hidden(self):
        return self.wait_for_element_hide(SuccessOrderModalLocators.ORDER_SUCCESS_NUMBER)

    @allure.step('Ожидаем завершения анимации')
    def wait_for_animation_end(self):
        self.wait_for_element_hide(SuccessOrderModalLocators.LOADING_ANIMATION)

    @allure.step('Получаем номер оформленного заказа')
    def get_number_of_order(self):
        text = self.get_text_on_element(SuccessOrderModalLocators.ORDER_SUCCESS_NUMBER)
        return int(text)

    @allure.step('Нажимаем кнопку закрытие модального окна успешного заказа')
    def click_close_button_success_modal(self):
        self.click_on_element(SuccessOrderModalLocators.BUTTON_CLOSE_MODAL_ORDER)

    @allure.step('Проверяем, что открыта главная страница')
    def is_main_page_opened(self):
        return main_site in self.get_current_url()

    @allure.step('Оформить заказ: добавить булку и нажать "Оформить заказ"')
    def create_order(self):
        self.main_page_loading_wait()
        self.drag_bun_to_basket()
        self.click_order_button()

