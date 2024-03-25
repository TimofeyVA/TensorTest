from selenium.webdriver.chrome.webdriver import WebDriver

from pages.sbis_about_page import SbisAboutPage
from pages.sbis_page import SbisPage


def test_second_scenario(browser: WebDriver):
    sbisPage = SbisPage(browser)
    sbisPage.go_to_sbis_page()
    sbisPage.go_to_contacts()

    sbisAboutPage = SbisAboutPage(browser)

    assert sbisAboutPage.is_exist_list_partners(), "Список партёров не определён"

    assert sbisAboutPage.get_region_name() == 'Республика Башкортостан', "Регион определён неверно"

    sbisAboutPage.region_change()
    # assert sbisAboutPage.check(), "Dialog"
    # sbisAboutPage.region_change()

    # assert sbisAboutPage.get_region_name() == 'Камчатский край', "Регион определён неверно2"