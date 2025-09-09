import allure

from locators.auth_page_locators import LoginPageLocators
from pages.base_page import BasePage
from data.urls import login_site



class AuthPage(BasePage):


    @allure.step('Открыть страницу авторизации')
    def open_login_page(self):
        self.open_page(login_site)

    @allure.step("Авторизоваться")
    def auth(self, email, password):
        self.wait_for_element_clickable(LoginPageLocators.EMAIL)
        self.send_keys_to_input(LoginPageLocators.EMAIL, email)
        self.send_keys_to_input(LoginPageLocators.PASSWORD, password)
        self.click_on_element(LoginPageLocators.BUT_ENTER)