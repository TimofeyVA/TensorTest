from selenium.webdriver.chrome.webdriver import WebDriver
from locators.locators import TensorAboutLocators
from pages.base_page import BasePage


class TensorAboutPage(BasePage):
    def __init__(self, browser: WebDriver) -> None:
        super().__init__(browser)
        self.__locator = TensorAboutLocators()


    
    def check_size_images(self):
        images = self.find_all(*self.__locator.LOCATOR_IMAGE_WORK)

        width = images[0].size.get('width')
        height = images[0].size.get('height')
 
        for img in images:
            if width != img.size.get('width') and height != img.size.get('height'):
                return False
        
        return True