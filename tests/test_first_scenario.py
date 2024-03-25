from pages.sbis_about_page import SbisAboutPage
from pages.sbis_page import SbisPage
from pages.tensor_about_page import TensorAboutPage
from pages.tensor_page import TensorPage


def test_first_scenario(browser):
    '''
    Первый сценарий
    '''

    sbisPage = SbisPage(browser)

    # Шаг 1.1 Переход на страницу https://sbis.ru/
    sbisPage.go_to_sbis_page()

    # Шаг 1.2 Переход в раздел с контактами
    sbisPage.go_to_contacts()

    sbisAboutPage = SbisAboutPage(browser)

    # Шаг 2. Клик по баннеру "Тензор"
    sbisAboutPage.click_banner_tensor()

    tensorPage = TensorPage(browser)

    # Шаг 3. Проверка существование блока "Сила в людях"
    assert tensorPage.is_exist_block_power_people(), "Не найден блок 'Сила в людях'"

    # Шаг 4. Переход в раздел about через ссылку в блоке "Сила в людях"
    tensorPage.go_to_about()

    # Шаг 5. Проверка адреса
    assert browser.current_url == 'https://tensor.ru/about', "Не изменился адрес url после перехода"


    tensorAboutPage = TensorAboutPage(browser)

    # Шаг 6. Проверка размеров фотографий в разделе "Работаем"
    assert tensorAboutPage.check_size_images(), "Разные размеры у фотографий"

