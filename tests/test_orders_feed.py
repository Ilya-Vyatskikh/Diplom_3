import allure
import pytest

from pages.orders_feed_page import OrdersFeedPage
from pages.main_page import MainPage
from locators.order_feed_locators import OrderFeedLocators

@allure.epic("Лента заказов")
@allure.feature("Счётчики и отображение заказов")
class TestOrdersFeed:

    @allure.title("Счётчики 'Выполнено за всё время' и 'за сегодня' увеличиваются после заказа")
    @allure.description(
        "Проверить, что при оформлении заказа счётчики на странице 'Лента заказов' увеличиваются"
    )
    @pytest.mark.parametrize('counter', [OrderFeedLocators.COUNTER_TOTAL, OrderFeedLocators.COUNTER_TODAY])
    def test_upgrade_counter_total_orders(self, driver, login, counter):
        main_page = MainPage(driver)
        orders_page = OrdersFeedPage(driver)
        main_page.main_page_loading_wait()
        main_page.click_by_link_orders_feed()
        prev_counter = orders_page.get_value_any_counter(counter)
        main_page.click_by_link_constructor()
        main_page.create_order()
        main_page.is_order_success_modal_visible()
        main_page.wait_for_animation_end()
        main_page.click_close_button_success_modal()
        main_page.wait_for_order_success_modal_hidden()
        main_page.click_by_link_orders_feed()
        new_counter = orders_page.get_value_any_counter(counter)
        assert new_counter > prev_counter

    @allure.title("Номер заказа появляется в разделе 'В работе'")
    @allure.description(
        "Проверить, что после оформления заказа его номер отображается в блоке 'В работе' на странице 'Лента заказов'"
    )
    def test_visible_order_number_in_progress(self, driver, login):
        main_page = MainPage(driver)
        orders_page = OrdersFeedPage(driver)
        main_page.main_page_loading_wait()
        main_page.create_order()
        main_page.is_order_success_modal_visible()
        main_page.wait_for_animation_end()
        order_number = main_page.get_number_of_order()
        main_page.click_close_button_success_modal()
        main_page.wait_for_order_success_modal_hidden()
        main_page.click_by_link_orders_feed()
        orders_page.is_orders_feed_page_opened()
        orders_page.wait_for_orders_in_progress()
        order_in_progress = orders_page.get_number_orders_in_progress()
        assert order_number == order_in_progress




