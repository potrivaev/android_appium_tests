import pytest

from appium import webdriver
from config.options import desired_capabilities, options


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Remote(options["appium_url"], desired_capabilities)
    yield
    driver.quit()


def test_text_appear_after_add_button_pressed(driver):
    pass
