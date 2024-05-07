import random
from faker import Faker
from conftest import driver
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as ec

class TestRegistration:
#регистрация нового пользователя
    def test_succecfully_registration(self,driver):
        driver.find_element(*Locators.button_pers_cabinet).click()
        WW(driver, 10).until(ec.visibility_of_element_located(Locators.title_sign_in))
        driver.find_element(*Locators.button_registration_page_pers_cab).click()
        WW(driver, 10).until(ec.visibility_of_element_located(Locators.title_registration))
        driver.find_element(*Locators.field_name).send_keys(Faker().name())
        driver.find_element(*Locators.field_email).send_keys(
            f'konstantin_markelov_8_{random.randint(100, 999)}@ya.ru')
        driver.find_element(*Locators.field_password).send_keys(f'{random.randint(100000, 999999)}')
        driver.find_element(*Locators.button_registration).click()
        WW(driver, 10).until(ec.visibility_of_element_located(Locators.title_sign_in))

        assert driver.find_element(*Locators.title_h2).text == 'Вход'


#Ошибка для некорректного пароля
    def test_invalid_password(self, driver):
        driver.find_element(*Locators.button_pers_cabinet).click()
        WW(driver, 10).until(ec.visibility_of_element_located(Locators.title_sign_in))
        driver.find_element(*Locators.button_registration_page_pers_cab).click()
        WW(driver, 10).until(ec.visibility_of_element_located(Locators.title_registration))
        driver.find_element(*Locators.field_name).send_keys(Faker().name())
        driver.find_element(*Locators.field_email).send_keys(
            f'konstantin_markelov_8_{random.randint(100, 999)}@ya.ru')
        driver.find_element(*Locators.field_password).send_keys(f'{random.randint(100, 9999)}')
        driver.find_element(*Locators.button_registration).click()

        assert driver.find_element(*Locators.message_wrong_password).text == 'Некорректный пароль'
