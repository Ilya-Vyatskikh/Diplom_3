from selenium.webdriver.common.by import By

class LoginPageLocators:
    # локаторы для страницы авторизации:
    EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input[1]") # поле ввода емаил для страницы авторизации и регистрации
    PASSWORD = (By.XPATH, "//label[(text()='Пароль')]/following-sibling::input[1]") #поле ввода пароля для страницы авторизации и регистрации
    BUT_ENTER = (By.XPATH, "//button[text()='Войти']")  # кнопка "Войти"
