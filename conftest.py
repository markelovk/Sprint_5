import pytest
from selenium import webdriver
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as ec

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://stellarburgers.nomoreparties.site/")
    WW(driver, 10).until(ec.visibility_of_element_located(Locators.personal_cabinet))
    yield driver
    driver.quit()
