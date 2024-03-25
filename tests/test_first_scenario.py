
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.sbis_about_page import SbisAboutPage
from pages.sbis_page import SbisPage
from pages.tensor_about_page import TensorAboutPage
from pages.tensor_page import TensorPage


def test_first_scenario(browser: WebDriver):

    sbisPage = SbisPage(browser)
    sbisPage.go_to_sbis_page()
    sbisPage.go_to_contacts()

    sbisAboutPage = SbisAboutPage(browser)
    sbisAboutPage.click_banner_tensor()


    tensorPage = TensorPage(browser)
    assert tensorPage.is_exist_block_power_people(), "Не найден блок 'Сила в людях'"
    tensorPage.go_to_about()


    tensorAboutPage = TensorAboutPage(browser)
    assert tensorAboutPage.check_size_images(), "У фотографий разные размеры"

