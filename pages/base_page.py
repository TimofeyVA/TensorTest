from typing import List
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self, browser: WebDriver) -> None:
        self._browser = browser

    
    def go_to(self, url: str):
        '''
        Метод перехода на страницу по указанному url
        '''
        self._browser.get(url)
    

    def find(self, *args) -> WebElement:
        '''
        Поиск элемента в DOM-дереве
        '''
        return self._browser.find_element(*args)
    

    def find_all(self, *args) -> List[WebElement]:
        '''
        Поиск всех подходящих элементов в DOM-дереве
        '''
        return self._browser.find_elements(*args)


    def click(self, *args):
        '''
        Клик по элементу
        '''
        self.find(*args).click()

    
    def exist(self, *args) -> bool:
        '''
        Проверка сущестовование элемента
        '''
        try:
            status =  self.find(*args).is_displayed()
            return status
        except:
            return False
