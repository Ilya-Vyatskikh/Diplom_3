from selenium.webdriver.common.by import By

class OrderFeedLocators:

    # Счётчики в правом верхнем углу
    COUNTER_TOTAL = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'text_type_digits-large')]")
    COUNTER_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'text_type_digits-large')]")

    # Раздел "В работе" (номера заказов, которые в процессе)
    IN_PROGRESS_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]//li")

    # Оверлей для закрытия модального окна
    OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")  # клик по фону закрывает окно