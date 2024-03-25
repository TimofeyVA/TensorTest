import os
from selenium.webdriver.chrome.webdriver import WebDriver
from locators.locators import SbisDownloadLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait


class SbisDownloadPage(BasePage):
    """
    Класс SbisDownloadPage.
    Предназначен для работы со страницей sbis/download
    """
        
    def __init__(self, browser: WebDriver) -> None:
        super().__init__(browser)
        self.__locator = SbisDownloadLocators()

    def __every_downloads_chrome(self, driver):
        '''
        Метод получения скачанных файлов
        '''

        if not driver.current_url.startswith("chrome://downloads"):
            driver.get("chrome://downloads/")

        return driver.execute_script("""
            var items = document.querySelector('downloads-manager')
                .shadowRoot.getElementById('downloadsList').items;
            console.log(items);
            if (items.every(e => e.state === 2))
                return items.map(e => e.filePath);
        """)

    def click_tab_plugin(self):
        '''
        Метод перехода на вкладку "СБИС плагин"
        '''

        a = self.find(*self.__locator.LOCATOR_DOWNLOAD_TAB)
        self._browser.execute_script("arguments[0].click();", a)
        # self.click(*self.__locator.LOCATOR_DOWNLOAD_TAB)


    def download_plugin(self):
        '''
        Метод загрузки и получения размера файла со страницы sbis/download
        '''
        a = self.find(*self.__locator.LOCATOR_DOWNLOAD_FILE)
        self._browser.execute_script("arguments[0].click();", a)

        paths = WebDriverWait(self._browser, 30, 0.5).until(self.__every_downloads_chrome)

        return os.stat(paths[-1]).st_size
