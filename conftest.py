import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as ec

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://stellarburgers.nomoreparties.site/")
    WW(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//p[text()='Личный Кабинет']")))
    yield driver
    driver.quit()
