import pytest
from locators import ConstructorPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestConstructor:
    def test_navigate_to_buns_section(self, main_driver):
        main_driver.find_element(*ConstructorPageLocators.SAUCES_SECTION).click()
        main_driver.find_element(*ConstructorPageLocators.BUNS_SECTION).click()

        current_section = WebDriverWait(main_driver, 10).until(
            EC.presence_of_element_located(ConstructorPageLocators.CURRENT_SECTION)
        )

        assert 'Булки' in current_section.text

    def test_navigate_to_sauces_section(self, main_driver):
        main_driver.find_element(*ConstructorPageLocators.SAUCES_SECTION).click()
        current_section = WebDriverWait(main_driver, 10).until(
            EC.presence_of_element_located(ConstructorPageLocators.CURRENT_SECTION)
        )

        assert 'Соусы' in current_section.text

    def test_navigate_to_fillings_section(self, main_driver):
        main_driver.find_element(*ConstructorPageLocators.FILLINGS_SECTION).click()
        current_section = WebDriverWait(main_driver, 10).until(
            EC.presence_of_element_located(ConstructorPageLocators.CURRENT_SECTION)
        )

        assert 'Начинки' in current_section.text
