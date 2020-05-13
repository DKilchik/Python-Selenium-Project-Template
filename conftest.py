import pytest
from selenium import webdriver


@pytest.fixture()
def browser(request):
    browser = webdriver.Chrome()

    # Close browser
    yield browser
    browser.quit()
