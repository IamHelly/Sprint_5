from selenium.webdriver.common.by import By


class RegistrationLocators:
    NAME_INPUT = (By.XPATH, './/*[text()="Имя"]/following-sibling::input')  # input для ввода имени юзера
    EMAIL_INPUT = (By.XPATH, './/*[text()="Email"]/following-sibling::input')  # input для ввода почты
    PASSWORD_INPUT = (By.XPATH, './/*[text()="Пароль"]/following-sibling::input')  # input для ввода пароля
    REGISTRATION_BUTTON = (By.XPATH, './/button[contains(text(), "Зарегистрироваться")]')  # кнопка "Зарегистрироваться"
    TITLE_LOGIN = (By.XPATH, './/h2[contains(text(), "Вход")]')  # заголовок "Вход"
    ERROR_MESSAGE = (By.XPATH, './/p[contains(text(), "Некорректный пароль")]')  # сообщение об ошибке "Некорректный пароль"
    TITLE_REGISTRATION = (By.XPATH, './/h2[contains(text(), "Регистрация")]')  # заголовок страницы регистрации
