from selenium.webdriver.common.by import By


class SectionConstructionLocators:
    ROLLS_SECTION = (By.XPATH, './/span[contains(text(), "Булки")]/parent::div')  # раздел "Булки"
    SAUCES_SECTION = (By.XPATH, './/span[contains(text(), "Соусы")]/parent::div')  # раздел "Соусы"
    FILLINGS_SECTION = (By.XPATH, './/span[contains(text(), "Начинки")]/parent::div')  # раздел "Начинки"
    LINK_CONSTRUCTOR = (By.XPATH, './/p[contains(text(), "Конструктор")]/parent::a')  # переход в раздел "Конструктор"
    LOGO_CONSTRUCTOR = (By.XPATH, './/div[@class="AppHeader_header__logo__2D0X2"]/a')  # лого
    TITLE_CONSTRUCTOR = (By.XPATH, './/h1[contains(text(), "Соберите бургер")]')  # заголовок конструктора
