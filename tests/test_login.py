import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginLocators, MainPageLocators, RegistrationLocators
from data import Data, TestData
from helper import Help


class TestLogin:
    def test_login_main_button(self, main_driver):
        main_driver.find_element(*MainPageLocators.MAIN_LOGIN_BUTTON).click()
        main_driver.find_element(*LoginLocators.EMAIL_INPUT_FIELD).send_keys(TestData.login_input)
        main_driver.find_element(*LoginLocators.PASSWORD_INPUT_FIELD).send_keys(TestData.password_input)
        main_driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

        order_button = WebDriverWait(main_driver, 10).until(
            EC.presence_of_element_located(LoginLocators.ORDER_BUTTON)
        )
        assert order_button.is_displayed()

    def test_login_personal_cabinet_button(self, main_driver):
        main_driver.find_element(*MainPageLocators.PERSONAL_CABINET_BUTTON).click()
        main_driver.find_element(*LoginLocators.EMAIL_INPUT_FIELD).send_keys(TestData.login_input)
        main_driver.find_element(*LoginLocators.PASSWORD_INPUT_FIELD).send_keys(TestData.password_input)
        main_driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

        order_button = WebDriverWait(main_driver, 10).until(
            EC.presence_of_element_located(LoginLocators.ORDER_BUTTON)
        )
        assert order_button.is_displayed()

    def test_login_register_button(self, log_driver):
        log_driver.find_element(*LoginLocators.REGISTER_BUTTON).click()
        log_driver.find_element(*RegistrationLocators.REG_NAME_INPUT_FIELD).send_keys('Tester')
        generated_email = Help.generate_email()
        log_driver.find_element(*RegistrationLocators.REG_EMAIL_INPUT_FIELD).send_keys(generated_email)
        log_driver.find_element(*RegistrationLocators.REG_PASSWORD_INPUT_FIELD).send_keys('123456')
        log_driver.find_element(*RegistrationLocators.SUBMIT_BUTTON).click()
        WebDriverWait(log_driver, 20).until(
            EC.presence_of_element_located(LoginLocators.LOGIN_BUTTON)
        )
        log_driver.find_element(*LoginLocators.EMAIL_INPUT_FIELD).send_keys(generated_email)
        log_driver.find_element(*LoginLocators.PASSWORD_INPUT_FIELD).send_keys('123456')
        log_driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

        # Assert: проверяем, что на главной странице появилась кнопка "Оформить заказ"
        order_button = WebDriverWait(log_driver, 10).until(
            EC.presence_of_element_located(LoginLocators.ORDER_BUTTON)
        )
        assert order_button.is_displayed()

    def test_login_restore_button(self, log_driver):
        log_driver.find_element(*LoginLocators.RESTORE_PASSWORD).click()
        log_driver.find_element(*LoginLocators.EMAIL_INPUT_FIELD).send_keys(TestData.login_input)
        log_driver.find_element(*LoginLocators.RESTORE_BUTTON).click()

        WebDriverWait(log_driver, 10).until(
            EC.url_to_be(Data.STELLAR_RESET_URL)
        )
        assert log_driver.current_url == Data.STELLAR_RESET_URL
