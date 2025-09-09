from selenium.webdriver.common.by import By

class SuccessOrderModalLocators:

    # Модальное окно после оформления заказа
    ORDER_SUCCESS_MODAL = (By.XPATH, "//p[contains(text(), 'Ваш заказ начали готовить')]")  # Заголовок модального окна
    ORDER_SUCCESS_ICON = (By.XPATH, "//img[@alt='идентификатор заказа']")  # Иконка идентификатора
    ORDER_SUCCESS_MESSAGE = (By.XPATH, "//p[contains(text(), 'Дождитесь готовности на орбитальной станции')]") # Сообщение в моадльном окне
    BUTTON_CLOSE_MODAL_ORDER = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    LOADING_ANIMATION = (By.XPATH, "//img[contains(@src, 'loading.89540200')]")



    ORDER_SUCCESS_NUMBER = (By. XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq') and contains(@class, 'digits-large mb-8')]") # номер заказа