import pytest

from appium import webdriver
from config.options import desired_capabilities, options


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Remote(options["appium_url"], desired_capabilities)
    yield driver
    driver.quit()


def test_text_appear_after_add_button_pressed(driver):

    text_button = driver.find_elements_by_accessibility_id("Text")[0]
    text_button.click()
    elements = ["Linkify", "LogTextBox", "Marquee"]
    menu_objects = []
    add_btn_press_count = 3
    for element in elements:
        menu_objects.append(driver.find_elements_by_accessibility_id(element)[0])
    assert len(menu_objects) == add_btn_press_count
    menu_objects[1].click()
    add_button = driver.find_elements_by_accessibility_id("Add")[0]
    text_view = driver.find_element_by_id("io.appium.android.apis:id/text")
    text_view_texts = []
    for i in range(add_btn_press_count):
        add_button.click()
        text_view_texts.append(text_view.text)
    assert len(text_view_texts) == add_btn_press_count
    assert text_view_texts[0].replace("\n","") == "This is a test"
