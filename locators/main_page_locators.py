from selenium.webdriver.common.by import By

class MainPageLocators:

    # Кнопка войти для авторизации
    BUT_ENTER_ACC = (By.XPATH, "//button[text()='Войти в аккаунт']")

    # Кнопка Оформить заказ
    BUT_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")

    # Ссылки в навигации
    LINK_CONSTRUCT = (By.XPATH,"//a[p[text()='Конструктор']]")  # ссылка "Конструктор"
    LINK_ORDER_FEED = (By.XPATH,"//a[p[text()='Лента Заказов']]") # ссылка "Лента заказов"

    # Ингредиенты
    BUN_KRATOR = (By.XPATH,"//a[p[text()='Краторная булка N-200i']]") # Краторная булка

    # Счётчики у ингредиентов:
    ## Счетчик булки "Краторная булка"
    COUNTER_BUN = (By.XPATH, "//p[text()='Краторная булка N-200i']/ancestor::a//p[contains(@class, 'counter_counter__num')]")

    # Верхняя позиция в корзине
    POS_TOP_BASKET = (By.XPATH, "//div[contains(@class, 'constructor-element_pos_top')]")

    # Оверлей для закрытия модального окна
    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")


