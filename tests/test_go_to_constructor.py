from conftest import driver
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as ec

class TestPersonalCabinetNavigation:
#переход по клику на «Конструктор» из Личного кабинета
    def test_go_to_constructor_from_personal_cabinet(self,driver):
        driver.find_element(*Locators.button_pers_cabinet).click()
        WW(driver, 10).until(ec.visibility_of_element_located(Locators.title_sign_in))
        driver.find_element(*Locators.button_constructor).click()
        WW(driver,10).until(ec.visibility_of_element_located(Locators.title_take_burger))

        assert driver.find_element(*Locators.title_h1).text == 'Соберите бургер' and driver.current_url == 'https://stellarburgers.nomoreparties.site/'


#переход по клику на логотип Stellar Burgers из Личного кабинета
    def test_go_to_logo_from_personal_cabinet(self,driver):
        driver.find_element(*Locators.button_pers_cabinet).click()
        WW(driver, 10).until(ec.visibility_of_element_located(Locators.title_sign_in))
        driver.find_element(*Locators.button_logo).click()
        WW(driver, 10).until(ec.visibility_of_element_located(Locators.title_take_burger))

        assert driver.find_element(*Locators.title_h1).text == 'Соберите бургер' and driver.current_url == 'https://stellarburgers.nomoreparties.site/'
