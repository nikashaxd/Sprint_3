import pytest
from selenium import webdriver
from locators import RegistrationLocators, LoginLocators
from data import Data


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(Data.Stellar_REG_url)

    yield chrome_driver
    chrome_driver.quit()

@pytest.fixture(scope='function')
def log_driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(Data.Stellar_LOG_url)

    yield chrome_driver
    chrome_driver.quit()

@pytest.fixture(scope='function')
def main_driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(Data.Stellar_Main_url)

    yield chrome_driver
    chrome_driver.quit()

@pytest.fixture(scope='function')
def cabinet_driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(Data.Stellar_CAB_url)

    yield chrome_driver
    chrome_driver.quit()

@pytest.fixture
def register_user(driver):
    driver.get(Data.Stellar_REG_url)
    driver.find_element(*RegistrationLocators.REG_NAME_INPUT_FIELD).send_keys('Tester')
    driver.find_element(*RegistrationLocators.REG_EMAIL_INPUT_FIELD).send_keys(Data.login_input)
    driver.find_element(*RegistrationLocators.REG_PASSWORD_INPUT_FIELD).send_keys(Data.password_input)
    driver.find_element(*RegistrationLocators.SUBMIT_BUTTON).click()

@pytest.fixture
def login_user(driver):
    driver.get(Data.Stellar_LOG_url)
    driver.find_element(*LoginLocators.EMAIL_INPUT_FIELD).send_keys(Data.login_input)
    driver.find_element(*LoginLocators.PASSWORD_INPUT_FIELD).send_keys(Data.password_input)
    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()