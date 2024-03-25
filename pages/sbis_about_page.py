
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from locators.locators import SbisAboutLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SbisAboutPage(BasePage):
    def __init__(self, browser: WebDriver) -> None:
        super().__init__(browser)
        self.__locator = SbisAboutLocators()


    def click_banner_tensor(self):

        window_before = self._browser.window_handles[0]

        self.click(*self.__locator.LOCATOR_BANNER_TENSOR)

        window_after = self._browser.window_handles[1]

        self._browser.switch_to.window(window_after)

    
    def get_region_name(self) -> str:
        return self.find(*self.__locator.LOCATOR_REGION_NAME).text
    

    def is_exist_list_partners(self) -> bool:
        return self.exist(*self.__locator.LOCATOR_LIST_PARTNERS)
    

    def region_change(self):
        self.click(*self.__locator.LOCATOR_REGION_NAME)

        time.sleep(2)
        c = self.find(*self.__locator.LOCATOR_DIALOG)


        # z = self._browser.find_elements(By.NAME, 'dialog')

        xx = self._browser.find_elements(By.XPATH, "//*[@title='Камчатский край']")
   
        a = self.check()
        1+1
        # self.click(*self.__locator.LOCATOR_REGION_KAMCHATKA) 

    def check(self):
        return self.exist(*self.__locator.LOCATOR_DIALOG)