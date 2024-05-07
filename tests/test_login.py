from conftest import driver
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as ec

class TestLogin:
#вход по кнопке «Войти в аккаунт» на главной странице
    def test_login_main_page(self,driver):
        driver.find_element(*Locators.button_sign_in_to_account).click()
        WW(driver,10).until(ec.visibility_of_element_located(Locators.title_sign_in))
        driver.find_element(*Locators.field_email_page_sign_in).send_keys('konstantin_markelov_8_014@ya.ru')
        driver.find_element(*Locators.field_password_page_sign_in).send_keys('123456')
        driver.find_element(*Locators.button_sign_in).click()
        WW(driver,10).until(ec.visibility_of_element_located(Locators.button_create_order_text))

        assert driver.find_element(*Locators.button_create_order).text == 'Оформить заказ'


#вход через кнопку «Личный кабинет»
    def test_login_from_profile(self, driver):
        driver.find_element(*Locators.button_pers_cabinet).click()
        WW(driver, 10).until(ec.visibility_of_element_located(Locators.title_sign_in))
        driver.find_element(*Locators.field_email_page_sign_in).send_keys('konstantin_markelov_8_014@ya.ru')
        driver.find_element(*Locators.field_password_page_sign_in).send_keys('123456')
        driver.find_element(*Locators.button_sign_in).click()
        WW(driver,10).until(ec.visibility_of_element_located(Locators.button_create_order_text))

        assert driver.find_element(*Locators.button_create_order).text == 'Оформить заказ'


#вход через кнопку в форме регистрации
    def test_login_through_registration_button(self,driver):
        driver.find_element(*Locators.button_pers_cabinet).click()
        WW(driver, 10).until(ec.visibility_of_element_located(Locators.title_sign_in))
        driver.find_element(*Locators.button_registration_page_pers_cab).click()
        WW(driver, 10).until(ec.visibility_of_element_located(Locators.title_registration))
        driver.find_element(*Locators.button_sign_in_page_registration).click()
        WW(driver, 10).until(ec.visibility_of_element_located(Locators.title_sign_in))
        driver.find_element(*Locators.field_email_page_sign_in).send_keys('konstantin_markelov_8_014@ya.ru')
        driver.find_element(*Locators.field_password_page_sign_in).send_keys('123456')
        driver.find_element(*Locators.button_sign_in).click()
        WW(driver,10).until(ec.visibility_of_element_located(Locators.button_create_order_text))

        assert driver.find_element(*Locators.button_create_order).text == 'Оформить заказ'


#вход через кнопку в форме восстановления пароля
    def test_login_through_password_reset_button(self,driver):
        driver.find_element(*Locators.button_pers_cabinet).click()
        WW(driver, 10).until(ec.visibility_of_element_located(Locators.title_sign_in))
        driver.find_element(*Locators.button_restore_password).click()
        WW(driver, 10).until(ec.visibility_of_element_located(Locators.title_restore_password))
        driver.find_element(*Locators.button_sign_in_page_restore_password).click()
        WW(driver, 10).until(ec.visibility_of_element_located(Locators.title_sign_in))
        driver.find_element(*Locators.field_email_page_sign_in).send_keys('konstantin_markelov_8_014@ya.ru')
        driver.find_element(*Locators.field_password_page_sign_in).send_keys('123456')
        driver.find_element(*Locators.button_sign_in).click()
        WW(driver,10).until(ec.visibility_of_element_located(Locators.button_create_order_text))

        assert driver.find_element(*Locators.button_create_order).text == 'Оформить заказ'
