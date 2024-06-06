from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from variables import Variables
from locators.login_locators import LoginLocators
from urls import UrlsPage


class TestLogin:

    #  Тест входа в аккаунт через кнопку "Войти в аккаунт" на главной странице
    def test_login_in_account_via_button_on_main_page(self, driver):
        driver.get(UrlsPage.main_page)
        # вход пользователя через кнопку на главной странице "Войти в аккаунт"
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable(LoginLocators.LOGIN_IN_ACCOUNT)).click()
        driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(Variables.login_user)
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(Variables.password_user)
        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
        # переход на страницу профиля пользователя
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable(LoginLocators.PERSONAL_ACCOUNT)).click()
        WebDriverWait(driver, 4).until(EC.visibility_of_element_located(LoginLocators.PROFILE_TITLE))
        login_current_user = driver.find_element(*LoginLocators.LOGIN).get_attribute("value")
        # проверка входа под конкретным пользователем
        assert login_current_user == Variables.login_user

    # Тест входа в аккаунт через кнопку "Личный кабинет"
    def test_login_in_account_via_button_personal_account(self, driver):
        driver.get(UrlsPage.main_page)
        # вход пользователя через кнопку "Личный кабинет"
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable(LoginLocators.PERSONAL_ACCOUNT)).click()
        driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(Variables.login_user)
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(Variables.password_user)
        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
        # переход на страницу профиля пользователя
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable(LoginLocators.PERSONAL_ACCOUNT)).click()
        WebDriverWait(driver, 4).until(EC.visibility_of_element_located(LoginLocators.PROFILE_TITLE))
        login_current_user = driver.find_element(*LoginLocators.LOGIN).get_attribute("value")
        # проверка входа под конкретным пользователем
        assert login_current_user == Variables.login_user

    # Тест входа в аккаунт через кнопку в форме регистрации
    def test_login_in_account_via_button_on_registration_page(self, driver):
        driver.get(UrlsPage.registration_page)
        # вход пользователя по кнопке через форму регистрации
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable(LoginLocators.LOGIN_LINK)).click()
        driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(Variables.login_user)
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(Variables.password_user)
        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
        # переход на страницу профиля пользователя
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable(LoginLocators.PERSONAL_ACCOUNT)).click()
        WebDriverWait(driver, 4).until(EC.visibility_of_element_located(LoginLocators.PROFILE_TITLE))
        login_current_user = driver.find_element(*LoginLocators.LOGIN).get_attribute("value")
        # проверка входа под конкретным пользователем
        assert login_current_user == Variables.login_user

    # Тест входа в аккаунт через кнопку в форме восстановления пароля
    def test_login_in_account_via_button_on_forgot_password_page(self, driver):
        driver.get(UrlsPage.forgot_password_page)
        # вход пользователя по кнопке через форму восстановления пароля
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable(LoginLocators.LOGIN_LINK)).click()
        driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(Variables.login_user)
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(Variables.password_user)
        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
        # переход на страницу профиля пользователя
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable(LoginLocators.PERSONAL_ACCOUNT)).click()
        WebDriverWait(driver, 4).until(EC.visibility_of_element_located(LoginLocators.PROFILE_TITLE))
        login_current_user = driver.find_element(*LoginLocators.LOGIN).get_attribute("value")
        # проверка входа под конкретным пользователем
        assert login_current_user == Variables.login_user

    # Тест перехода в Личный кабинет
    def test_click_button_to_personal_account(self, driver, login):
        # ожидание кликабельности кнопки "Личный кабинет"
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable(LoginLocators.PERSONAL_ACCOUNT)).click()
        WebDriverWait(driver, 4).until(EC.visibility_of_element_located(LoginLocators.PROFILE_TITLE))
        current_url = driver.current_url
        # проверка совпадения адреса текущей страницы с ожидаемым
        assert current_url == UrlsPage.profile_page
