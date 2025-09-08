from selenium.webdriver.common.by import By

class SuccessOrderModalLocators:

    # Модальное окно после оформления заказа
    ORDER_SUCCESS_MODAL = (By.XPATH, "//p[text()='Ваш заказ начали готовить']")  # Заголовок модального окна
    ORDER_SUCCESS_ICON = (By.XPATH, "//img[@alt='идентификатор заказа']")  # Иконка идентификатора
    ORDER_SUCCESS_MESSAGE = (By.XPATH, "//p[text()='Дождитесь готовности на орбитальной станции']") # Сообщение в моадльном окне
    BUTTON_CLOSE_MODAL_ORDER = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    LOADING_ANIMATION = (By.XPATH, './/img[@src="./static/media/loading.89540200.svg"]')



    ORDER_SUCCESS_NUMBER = (By. XPATH, ".//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']") # номер заказа
    #OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")