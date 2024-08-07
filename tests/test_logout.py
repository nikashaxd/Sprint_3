import pytest
from locators import MainPageLocators, CabinetPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("register_user", "login_user")
class TestLogout:
    def test_logout_from_personal_cabinet(self, driver):
        profile_button = driver.find_element(*MainPageLocators.PERSONAL_CABINET_BUTTON)
        profile_button.click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(CabinetPageLocators.LOGOUT_BUTTON)
        )

        logout_button = driver.find_element(*CabinetPageLocators.LOGOUT_BUTTON)
        logout_button.click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
        )
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"