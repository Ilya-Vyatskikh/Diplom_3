import allure

from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from data.urls import *



class OrdersFeedPage(BasePage):

    @allure.step('Получить значение счётчика')
    def get_value_any_counter(self, locator):
        text = self.get_text_on_element(locator)
        return int(text)

    @allure.step('Проверить, что открыта страница "Лента заказов"')
    def is_orders_feed_page_opened(self):
        return feed_site in self.get_current_url()

    @allure.step('Ожидать появления заказов в разделе "В работе"')
    def wait_for_orders_in_progress(self):
        self.wait_for_attribute(OrderFeedLocators.IN_PROGRESS_LIST, 'class', 'digits')

    @allure.step('Получаем номер заказа в разделе "В работе"')
    def get_number_orders_in_progress(self):
        number_in_progress = self.get_text_on_element(OrderFeedLocators.IN_PROGRESS_LIST)
        return int(number_in_progress)