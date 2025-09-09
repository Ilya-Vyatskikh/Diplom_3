from selenium.webdriver.common.by import By


class IngredientLocators:

    """Модальное окно 'Детали ингридиента'"""
    WINDOW_MODAL_ING = (By.XPATH, "//h2[text()='Детали ингредиента']/parent::div")

    """Заголовок модального окна 'Детали ингредиентов'"""
    HEADER_MODAL_ING = (By.XPATH,"//h2[text()='Детали ингредиента']")

    """Кнопка закрытия модального окна 'Детали ингридиента'"""
    BUTTON_CLOSE_MODAL_ING = (By.XPATH,"//button[contains(@class, 'Modal_modal__close')]")
