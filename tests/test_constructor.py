import pytest
from locators import ConstructorPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestConstructor:
    def test_navigate_to_buns_section(self, main_driver):
        main_driver.find_element(*ConstructorPageLocators.SAUCES_SECTION).click()
        main_driver.find_element(*ConstructorPageLocators.BUNS_SECTION).click()

        current_section = WebDriverWait(main_driver, 10).until(
            EC.presence_of_element_located(ConstructorPageLocators.CURRENT_SECTION)
        )

        buns_section_class = main_driver.find_element(*ConstructorPageLocators.BUNS_SECTION).get_attribute('class')
        sauces_section_class = main_driver.find_element(*ConstructorPageLocators.SAUCES_SECTION).get_attribute('class')
        fillings_section_class = main_driver.find_element(*ConstructorPageLocators.FILLINGS_SECTION).get_attribute(
            'class')

        assert 'tab_tab_type_current__2BEPc' in buns_section_class
        assert 'noselect' in sauces_section_class
        assert 'noselect' in fillings_section_class

    def test_navigate_to_sauces_section(self, main_driver):
        main_driver.find_element(*ConstructorPageLocators.SAUCES_SECTION).click()

        current_section = WebDriverWait(main_driver, 10).until(
            EC.presence_of_element_located(ConstructorPageLocators.CURRENT_SECTION)
        )

        buns_section_class = main_driver.find_element(*ConstructorPageLocators.BUNS_SECTION).get_attribute('class')
        sauces_section_class = main_driver.find_element(*ConstructorPageLocators.SAUCES_SECTION).get_attribute('class')
        fillings_section_class = main_driver.find_element(*ConstructorPageLocators.FILLINGS_SECTION).get_attribute(
            'class')

        assert 'tab_tab_type_current__2BEPc' in sauces_section_class
        assert 'noselect' in buns_section_class
        assert 'noselect' in fillings_section_class

    def test_navigate_to_fillings_section(self, main_driver):
        main_driver.find_element(*ConstructorPageLocators.FILLINGS_SECTION).click()

        current_section = WebDriverWait(main_driver, 10).until(
            EC.presence_of_element_located(ConstructorPageLocators.CURRENT_SECTION)
        )

        buns_section_class = main_driver.find_element(*ConstructorPageLocators.BUNS_SECTION).get_attribute('class')
        sauces_section_class = main_driver.find_element(*ConstructorPageLocators.SAUCES_SECTION).get_attribute('class')
        fillings_section_class = main_driver.find_element(*ConstructorPageLocators.FILLINGS_SECTION).get_attribute(
            'class')

        assert 'tab_tab_type_current__2BEPc' in fillings_section_class
        assert 'noselect' in buns_section_class
        assert 'noselect' in sauces_section_class
