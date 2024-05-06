from conftest import driver
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as ec

class TestConstructor:
#переход к разделу «Соусы»
    def test_select_sauces(self,driver):
        driver.find_element(*Locators.button_sauces).click()
        WW(driver,3).until(ec.visibility_of_element_located(Locators.select_sauces))

        assert driver.find_element(*Locators.select_button).text == 'Соусы'

#переход к разделу «Начинки»
    def test_select_filling(self,driver):
        driver.find_element(*Locators.buttong_filling).click()
        WW(driver, 3).until(ec.visibility_of_element_located(Locators.select_filling))

        assert driver.find_element(*Locators.select_button).text == 'Начинки'

#переход к разделу «Булки» из раздела «Начинки»
    def test_select_bun(self,driver):
        driver.find_element(*Locators.buttong_filling).click()
        WW(driver, 3).until(ec.visibility_of_element_located(Locators.select_filling))
        driver.find_element(*Locators.button_buns).click()
        WW(driver, 3).until(ec.visibility_of_element_located(Locators.select_buns))

        assert driver.find_element(*Locators.select_button).text == 'Булки'
