import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    chrome_browser = webdriver.Chrome()
    # chrome_browser.implicitly_wait(10)

    yield chrome_browser

    chrome_browser.quit()