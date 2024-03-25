from selenium.webdriver.chrome.webdriver import WebDriver

from pages.sbis_download_page import SbisDownloadPage
from pages.sbis_page import SbisPage


def test_third_scenario(browser: WebDriver):
    '''
    Третий сценарий
    '''

    sbisPage = SbisPage(browser)


    # Шаг 1. Переход на https://sbis.ru/
    sbisPage.go_to_sbis_page()

    # Шаг 2. Переход в "Скачать СБИС"
    sbisPage.got_to_download()

    sbisDownloadPage = SbisDownloadPage(browser)

    # Шаг 3. Переход на вкладку "СБИС Плагин"
    sbisDownloadPage.click_tab_plugin()

    # Шаг 4. Загрузка файла
    size = sbisDownloadPage.download_plugin()

    # Шаг 5. Проверка размера файла
    assert round(size / (2**20), 1) == 8.3, "Указан неверный размер файла"