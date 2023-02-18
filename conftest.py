from selenium.webdriver.chrome.options import Options

import pytest as pytest
from selenium import webdriver

@pytest.fixture(params=['firefox', 'chrome'], scope='function')
def init_driver(request):
    options = Options()
    options.add_argument("--window-size=1600,800")

    if request.param == 'firefox':
        web_driver = webdriver.Firefox(executable_path='.\geckodriver')

    elif request.param == 'chrome':
        web_driver = webdriver.Chrome(executable_path='.\gchromedriver')

    yield web_driver
    web_driver.quit()

