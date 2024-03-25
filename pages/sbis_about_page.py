
import copy
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from locators.locators import SbisAboutLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SbisAboutPage(BasePage):
    """
    Класс SbisAboutPage.
    Предназначен для работы со страницей sbis/about
    """

    def __init__(self, browser: WebDriver) -> None:
        super().__init__(browser)
        self.__locator = SbisAboutLocators()


    def click_banner_tensor(self):
        '''
        Метод клика по баннеру "Тензор"
        '''
        window_before = self._browser.window_handles[0]

        self.click(*self.__locator.LOCATOR_BANNER_TENSOR)

        window_after = self._browser.window_handles[1]

        self._browser.switch_to.window(window_after)

    
    def get_region_name(self) -> str:
        '''
        Метод получения названия текущего региона
        '''

        return self.find(*self.__locator.LOCATOR_REGION_NAME).text
    

    def get_list_partners(self):
        '''
        Метод получения списка партнёров
        '''

        partners = set()
        for item in self.find_all(*self.__locator.LOCATOR_LIST_PARTNERS_ITEM):
            partners.add(item.get_attribute('title'))
        
        return partners
        
    

    def is_exist_list_partners(self) -> bool:
        '''
        Проверка сущестовования списка партнёров
        '''

        return self.exist(*self.__locator.LOCATOR_LIST_PARTNERS)
    

    def region_change(self):
        '''
        Метод смены региона
        '''

        self.click(*self.__locator.LOCATOR_REGION_NAME)
        time.sleep(2)
        self.click(*self.__locator.LOCATOR_REGION_KAMCHATKA)
        time.sleep(2)

