import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from helper import Help
from locators import RegistrationLocators


class TestRegistration:
    def test_successful_registration(self, reg_driver):
        name_input = reg_driver.find_element(*RegistrationLocators.REG_NAME_INPUT_FIELD)
        name_input.send_keys('Tester')

        email_input = reg_driver.find_element(*RegistrationLocators.REG_EMAIL_INPUT_FIELD)
        generated_email = Help.generate_email()
        email_input.send_keys(generated_email)

        password_input = reg_driver.find_element(*RegistrationLocators.REG_PASSWORD_INPUT_FIELD)
        password_input.send_keys('123456')

        submit_button = reg_driver.find_element(*RegistrationLocators.SUBMIT_BUTTON)
        submit_button.click()

        WebDriverWait(reg_driver, 10).until(
            EC.url_to_be(Data.STELLAR_LOG_URL)
        )

        assert reg_driver.current_url == Data.STELLAR_LOG_URL

    def test_invalid_password_registration(self, reg_driver):
        name_input = reg_driver.find_element(*RegistrationLocators.REG_NAME_INPUT_FIELD)
        name_input.send_keys('Tester')

        email_input = reg_driver.find_element(*RegistrationLocators.REG_EMAIL_INPUT_FIELD)
        email_input.send_keys(Help.generate_email())

        password_input = reg_driver.find_element(*RegistrationLocators.REG_PASSWORD_INPUT_FIELD)
        password_input.send_keys('pass')

        submit_button = reg_driver.find_element(*RegistrationLocators.SUBMIT_BUTTON)
        submit_button.click()

        error_message_element = WebDriverWait(reg_driver, 10).until(
            EC.presence_of_element_located(RegistrationLocators.REG_INCORRECT_PASSWORD)
        )

        assert error_message_element.is_displayed()
