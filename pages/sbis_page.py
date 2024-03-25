from selenium.webdriver.chrome.webdriver import WebDriver
from locators.locators import SbisLocators
from pages.base_page import BasePage


class SbisPage(BasePage):
    """
    Класс SbisPage.
    Предназначен для работы с главной страницей sbis
    """
    
    def __init__(self, browser: WebDriver) -> None:
        super().__init__(browser)

        self.__base_url = 'https://sbis.ru/'
        self.__locator = SbisLocators()
    
    def go_to_sbis_page(self):
        '''
        Метод перехода на страницу
        '''

        self.go_to(self.__base_url)

    
    def go_to_contacts(self):
        '''
        Метод перехода на страницу с контактами
        '''

        self.click(*self.__locator.LOCATOR_SBIS_CONTACTS)

    
    def got_to_download(self):
        '''
        Метод перехода на страницу с загрузками
        '''

        a = self.find(*self.__locator.LOCATOR_SBIS_DOWNLOAD)
        self._browser.execute_script("arguments[0].click();", a)
        # self.click(*self.__locator.LOCATOR_SBIS_DOWNLOAD)

