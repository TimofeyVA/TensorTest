from selenium.webdriver.chrome.webdriver import WebDriver

from pages.sbis_about_page import SbisAboutPage
from pages.sbis_page import SbisPage


def test_second_scenario(browser: WebDriver):
    '''
    Второй сценарий
    '''

    sbisPage = SbisPage(browser)

    # Шаг 1. Переход на https://sbis.ru/ в раздел "Контакты"
    sbisPage.go_to_sbis_page()
    sbisPage.go_to_contacts()

    sbisAboutPage = SbisAboutPage(browser)


    # Шаг 2.1. Проверка существования списка партнёров
    assert sbisAboutPage.is_exist_list_partners(), "Список партёров не определён"


    # Шаг 2.2. Проверка текущего региона
    assert sbisAboutPage.get_region_name() == 'Республика Башкортостан', "Регион определён неверно"


    # Шаг 3. Изменение региона на Камчатский край 
    partner_list_before = sbisAboutPage.get_list_partners() # Список партнёров перед изменением региона
    sbisAboutPage.region_change()
    partner_list_after = sbisAboutPage.get_list_partners() # Список партнёров после изменением региона


    # Шаг 4.1  Проверка текущего региона с учётом изменения региона
    assert sbisAboutPage.get_region_name() == 'Камчатский край', "Регион определён неверно"


    # Шаг 4.2 Проверка соответствия url адреса выбранному региону
    assert 'kamchatskij-kraj' in browser.current_url, "Неверный URL адрес"

    # Шаг 4.3 Проверка изменения списка партнёров
    assert partner_list_before != partner_list_after, "Список партнёров не изменился"

    # Шаг 4.4 Проверка соответствия title выбранному региону
    assert 'Камчатский край' in browser.title, "Не изменился title"