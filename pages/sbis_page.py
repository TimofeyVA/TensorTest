from selenium.webdriver.chrome.webdriver import WebDriver
from locators.locators import SbisLocators
from pages.base_page import BasePage


class SbisPage(BasePage):
    def __init__(self, browser: WebDriver) -> None:
        super().__init__(browser)

        self.__base_url = 'https://sbis.ru/'
        self.__locator = SbisLocators()
    
    def go_to_sbis_page(self):
        self.go_to(self.__base_url)

    
    def go_to_contacts(self):
        self.click(*self.__locator.LOCATOR_SBIS_CONTACTS)

