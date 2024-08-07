import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from helper import Help
from locators import RegistrationLocators

class TestRegistration:
    def test_successful_registration(self, driver):
        name_input = driver.find_element(*RegistrationLocators.REG_NAME_INPUT_FIELD)
        name_input.send_keys('Tester')
        assert name_input.get_attribute('value') != ''
        email_input = driver.find_element(*RegistrationLocators.REG_EMAIL_INPUT_FIELD)
        generated_email = Help.generate_email()
        email_input.send_keys(generated_email)
        assert '@' in generated_email and '.' in generated_email.split('@')[1]
        password_input =driver.find_element(*RegistrationLocators.REG_PASSWORD_INPUT_FIELD)
        password_input.send_keys('123456')
        assert len(password_input.get_attribute('value')) >= 6
        submit_button = driver.find_element(*RegistrationLocators.SUBMIT_BUTTON).click()

    def test_invalid_password_registration(self, driver):
        name_input = driver.find_element(*RegistrationLocators.REG_NAME_INPUT_FIELD)
        name_input.send_keys('Tester')
        email_input = driver.find_element(*RegistrationLocators.REG_EMAIL_INPUT_FIELD)
        email_input.send_keys(Help.generate_email())
        password_input = driver.find_element(*RegistrationLocators.REG_PASSWORD_INPUT_FIELD)
        password_input.send_keys('pass')
        submit_button = driver.find_element(*RegistrationLocators.SUBMIT_BUTTON)
        submit_button.click()

        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationLocators.REG_INCORRECT_PASSWORD)
        ).text
        assert "Некорректный пароль" in error_message
