from selenium.webdriver.common.by import By


class SbisLocators:
    LOCATOR_SBIS_CONTACTS = (By.CLASS_NAME, 'sbisru-Header__menu-item-1')
    LOCATOR_SBIS_DOWNLOAD = (By.XPATH, "//a[@href='/download']")


class SbisDownloadLocators:
    LOCATOR_DOWNLOAD_TAB = (By.XPATH, "//*[@data-id='plugin']")
    LOCATOR_DOWNLOAD_FILE = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/a")

class SbisAboutLocators:
    LOCATOR_BANNER_TENSOR = (By.CLASS_NAME, 'sbisru-Contacts__logo-tensor')
    LOCATOR_REGION_NAME = (By.XPATH, "//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']")
    LOCATOR_LIST_PARTNERS = (By.NAME, 'itemsContainer')
    LOCATOR_REGION_KAMCHATKA = (By.XPATH, "//*[@title='Камчатский край']")
    LOCATOR_LIST_PARTNERS_ITEM = (By.XPATH, "//div[@name='itemsContainer']/div/div/div/div/div")

class TensorLocators:
    LOCATOR_BLOCK_POWER_PEOPLE = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-content.tensor_ru-Index__card")
    LOCATOR_HREF_ABOUT = (By.XPATH, "//a[@href='/about']")


class TensorAboutLocators:
    LOCATOR_IMAGE_WORK = (By.CSS_SELECTOR, "img.tensor_ru-About__block3-image")