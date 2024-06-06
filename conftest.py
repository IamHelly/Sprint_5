import pytest
import string
import random
from selenium import webdriver
from variables import Variables
from locators.login_locators import LoginLocators
from urls import UrlsPage


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def login(driver):
    driver.get(UrlsPage.login_page)
    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(Variables.login_user)
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(Variables.password_user)
    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()


@pytest.fixture()
# Генератор логина
def generate_login_user():
    first_names = ['olga', 'mariya', 'anna', 'petr', 'vasilij']
    last_names = ['ivanov', 'petrov', 'sidorov', 'petrenko', 'lomova']
    domains = ['@ya.ru', '@gmail.com']
    return random.choice(first_names) + random.choice(last_names) + '9' + str(
        random.randrange(100, 999)) + random.choice(domains)


@pytest.fixture()
# Генератор пароля
def generate_password_user():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(1, 7))
    return password
