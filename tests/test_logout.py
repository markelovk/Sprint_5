from conftest import driver
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as ec

class TestLogout:
#выход по кнопке «Выйти» в личном кабинете
    def test_click_button_exit_in_personal_cabinet(self,driver):
        driver.find_element(*Locators.button_pers_cabinet).click()
        WW(driver, 10).until(ec.visibility_of_element_located(Locators.title_sign_in))
        driver.find_element(*Locators.field_email_page_sign_in).send_keys('konstantin_markelov_8_014@ya.ru')
        driver.find_element(*Locators.field_password_page_sign_in).send_keys('123456')
        driver.find_element(*Locators.button_sign_in).click()
        WW(driver, 10).until(ec.visibility_of_element_located(Locators.button_create_order))
        driver.find_element(*Locators.button_pers_cabinet).click()
        WW(driver,10).until(ec.visibility_of_element_located(Locators.button_profile))
        driver.find_element(*Locators.button_logout).click()
        WW(driver, 10).until(ec.visibility_of_element_located(Locators.title_sign_in))

        assert driver.find_element(*Locators.title_h2).text == 'Вход' and driver.current_url == 'https://stellarburgers.nomoreparties.site/login'