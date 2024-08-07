import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginLocators, MainPageLocators, RegistrationLocators
from data import Data
from helper import Help


class TestLogin:
    def test_login_main_button(self, main_driver):
        main_driver.find_element(*MainPageLocators.MAIN_LOGIN_BUTTON).click()
        main_driver.find_element(*LoginLocators.EMAIL_INPUT_FIELD).send_keys(Data.login_input)
        main_driver.find_element(*LoginLocators.PASSWORD_INPUT_FIELD).send_keys(Data.password_input)
        main_driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

        WebDriverWait(main_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Оформить заказ']"))
        )

    def test_login_personal_cabinet_button(self, main_driver):
        main_driver.find_element(*MainPageLocators.PERSONAL_CABINET_BUTTON).click()
        main_driver.find_element(*LoginLocators.EMAIL_INPUT_FIELD).send_keys(Data.login_input)
        main_driver.find_element(*LoginLocators.PASSWORD_INPUT_FIELD).send_keys(Data.password_input)
        main_driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

        WebDriverWait(main_driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Оформить заказ']"))
        )

    def test_login_register_button(self, log_driver):
        log_driver.find_element(*LoginLocators.REGISTER_BUTTON).click()
        log_driver.find_element(*RegistrationLocators.REG_NAME_INPUT_FIELD).send_keys('Tester')
        generated_email = Help.generate_email()
        log_driver.find_element(*RegistrationLocators.REG_EMAIL_INPUT_FIELD).send_keys(generated_email)
        log_driver.find_element(*RegistrationLocators.REG_PASSWORD_INPUT_FIELD).send_keys('123456')
        log_driver.find_element(*RegistrationLocators.SUBMIT_BUTTON).click()
        WebDriverWait(log_driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Войти']"))
        )
        log_driver.find_element(*LoginLocators.EMAIL_INPUT_FIELD).send_keys(generated_email)
        log_driver.find_element(*LoginLocators.PASSWORD_INPUT_FIELD).send_keys('123456')
        log_driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

        # Assert: проверяем, что на главной странице появилась кнопка "Оформить заказ"
        WebDriverWait(log_driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Оформить заказ']"))
        )

    def test_login_restore_button(self, log_driver):
        log_driver.find_element(*LoginLocators.RESTORE_PASSWORD).click()
        log_driver.find_element(*LoginLocators.EMAIL_INPUT_FIELD).send_keys(Data.login_input)
        log_driver.find_element(By.XPATH, "//button[text()='Восстановить']").click()

        WebDriverWait(log_driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/reset-password")
        )


