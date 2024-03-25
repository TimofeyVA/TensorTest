import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    chrome_browser = webdriver.Chrome()
    # chrome_browser.implicitly_wait(10)

    yield chrome_browser
    logs = chrome_browser.get_log('browser')

    with open('logs.txt', 'w') as f:
        for log in logs:
            print(log, file=f)
        
    chrome_browser.quit()