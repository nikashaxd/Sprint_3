import pytest
from selenium import webdriver
from locators import RegistrationLocators, LoginLocators
from data import Data, TestData


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope='function')
def reg_driver(driver):
    driver.get(Data.STELLAR_REG_URL)
    return driver

@pytest.fixture(scope='function')
def log_driver(driver):
    driver.get(Data.STELLAR_LOG_URL)
    return driver

@pytest.fixture(scope='function')
def main_driver(driver):
    driver.get(Data.STELLAR_MAIN_URL)
    return driver


@pytest.fixture(scope='function')
def cabinet_driver(driver):
    driver.get(Data.STELLAR_CAB_URL)
    return driver

@pytest.fixture
def register_user(driver):
    driver.get(Data.STELLAR_REG_URL)
    driver.find_element(*RegistrationLocators.REG_NAME_INPUT_FIELD).send_keys('Tester')
    driver.find_element(*RegistrationLocators.REG_EMAIL_INPUT_FIELD).send_keys(TestData.login_input)
    driver.find_element(*RegistrationLocators.REG_PASSWORD_INPUT_FIELD).send_keys(TestData.password_input)
    driver.find_element(*RegistrationLocators.SUBMIT_BUTTON).click()


@pytest.fixture
def login_user(driver):
    driver.get(Data.STELLAR_LOG_URL)
    driver.find_element(*LoginLocators.EMAIL_INPUT_FIELD).send_keys(TestData.login_input)
    driver.find_element(*LoginLocators.PASSWORD_INPUT_FIELD).send_keys(TestData.password_input)
    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
