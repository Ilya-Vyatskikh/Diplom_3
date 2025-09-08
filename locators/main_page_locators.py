from selenium.webdriver.common.by import By

class MainPageLocators:

    # Кнопка войти для авторизации
    BUT_ENTER_ACC = (By.XPATH, "//button[text()='Войти в аккаунт']")

    # Кнопка Оформить заказ
    BUT_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")

    # Текст названий конпок
    #NAME_LINK_ORDER_FEED = (By.XPATH, "//p[text()='Лента Заказов']")

    # Ссылки в навигации
    LINK_CONSTRUCT = (By.XPATH,"//p[text()='Конструктор']/parent::a[1]")  # ссылка "Конструктор"
    LINK_ORDER_FEED = (By.XPATH,"//p[text()='Лента Заказов']/parent::a[1]") # ссылка "Лента заказов"

    # Ингредиенты
    BUN_KRATOR = (By.XPATH,"//p[text()='Краторная булка N-200i']/parent::a[1]") # Краторная булка
    #SAUSE_SPACE = (By.XPATH,"//p[text()='Соус фирменный Space Sauce']/parent::a[1]") # Соус фирменный Space Sauce +
    #FILLING_STEAK = (By.XPATH,"//p[text()='Говяжий метеорит (отбивная)']/parent::a[1]") # Начинка Говяжий метеорит +

    # Счётчики у ингредиентов:
    ## Счетчик булки "Краторная булка"
    COUNTER_BUN = (By.XPATH, "//p[text()='Краторная булка N-200i']/ancestor::a//p[contains(@class, 'counter_counter__num')]") # Счетчик булки "Краторная булка" +
    #COUNTER_SAUCE = (By.XPATH, "//p[text()='Соус фирменный Space Sauce']/ancestor::a//p[contains(@class, 'counter_counter__num')]") # Счетчик соуса "Space Sauce" +
    #COUNTER_FILLING = (By.XPATH, "//p[text()='Говяжий метеорит (отбивная)']/ancestor::a//p[contains(@class, 'counter_counter__num')]") # Счетчик начинки "Говяжий метеорит" +

    # Верхняя позиция в корзине
    POS_TOP_BASKET = (By.XPATH, "//div[contains(@class, 'constructor-element_pos_top')]")

    # Оверлей для закрытия модального окна
    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")


