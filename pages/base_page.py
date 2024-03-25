from typing import List
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self, browser: WebDriver) -> None:
        self._browser = browser


    def go_to(self, url: str):
        self._browser.get(url)
    

    def find(self, *args) -> WebElement:
        return self._browser.find_element(*args)
    

    def find_all(self, *args) -> List[WebElement]:
        return self._browser.find_elements(*args)


    def click(self, *args):
        self.find(*args).click()

    
    def exist(self, *args) -> bool:
        try:
            status =  self.find(*args).is_displayed()
            return status
        except:
            return False
