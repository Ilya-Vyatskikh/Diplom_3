from selenium.webdriver.common.by import By

class OrderFeedLocators:

    #HEADER_ORDER_FEED = (By.XPATH, "//h1[text()='Лента заказов']") # Заголовок экрана Лента заказов, для подтверждения что находимся здесь

    # Счётчики в правом верхнем углу
    COUNTER_TOTAL = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'text_type_digits-large')]")
    COUNTER_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'text_type_digits-large')]")

    # Список заказов в ленте
    #ORDERS_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList')]/li[contains(@class, 'OrderFeed_orderListItem')]")

    # Название заказа (внутри элемента ленты)
    #ORDER_NAME = (By.XPATH, ".//p[contains(@class, 'OrderText')]")

    # Статус "В работе" — заказы, которые готовятся
    #IN_PROGRESS_BADGE = (By.XPATH, "//p[text()='В работе:']")

    # Раздел "В работе" (номера заказов, которые в процессе)
    IN_PROGRESS_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]//li")

    # Оверлей для закрытия модального окна
    OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")  # клик по фону закрывает окно