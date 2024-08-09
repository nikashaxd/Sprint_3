import pytest
from locators import MainPageLocators, LoginLocators, RegistrationLocators, ConstructorPageLocators
from data import Data
from conftest import register_user, login_user


@pytest.mark.usefixtures("register_user", "login_user")
class TestNavigation:
    def test_navigate_to_personal_cabinet(self, driver):
        profile_button = driver.find_element(*MainPageLocators.PERSONAL_CABINET_BUTTON)
        profile_button.click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account"

    def test_navigate_to_constructor_from_personal_cabinet(self, driver):
        driver.find_element(*MainPageLocators.PERSONAL_CABINET_BUTTON).click()
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_navigate_to_logo_from_personal_cabinet(self, driver):
        driver.find_element(*MainPageLocators.PERSONAL_CABINET_BUTTON).click()
        driver.find_element(*MainPageLocators.LOGO_BUTTON).click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
