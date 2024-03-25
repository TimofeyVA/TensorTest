from selenium.webdriver.chrome.webdriver import WebDriver
from locators.locators import TensorLocators
from pages.base_page import BasePage


class TensorPage(BasePage):
    def __init__(self, browser: WebDriver) -> None:
        super().__init__(browser)
        self.__locator = TensorLocators()

    def is_exist_block_power_people(self):
        return self.exist(*self.__locator.LOCATOR_BLOCK_POWER_PEOPLE)

    
    def go_to_about(self):
        self.click(*self.__locator.LOCATOR_HREF_ABOUT)