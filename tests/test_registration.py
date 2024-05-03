import random
from faker import Faker
from conftest import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as ec

class TestRegistration:
#регистрация нового пользователя
    def test_succecfully_registration(self,driver):
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()
        WW(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))
        driver.find_element(By.XPATH, "//a[text()='Зарегистрироваться']").click()
        WW(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//h2[text()='Регистрация']")))
        driver.find_element(By.XPATH, "//fieldset[1]//input[@name='name']").send_keys(Faker().name())
        driver.find_element(By.XPATH, "//fieldset[2]//input[@name='name']").send_keys(
            f'konstantin_markelov_8_{random.randint(100, 999)}@ya.ru')
        driver.find_element(By.NAME, 'Пароль').send_keys(f'{random.randint(100000, 999999)}')
        driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
        WW(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))

        assert driver.find_element(By.XPATH, "//h2").text == 'Вход'


#Ошибка для некорректного пароля
    def test_invalid_password(self, driver):
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()
        WW(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))
        driver.find_element(By.XPATH, "//a[text()='Зарегистрироваться']").click()
        WW(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//h2[text()='Регистрация']")))
        driver.find_element(By.XPATH, "//fieldset[1]//input[@name='name']").send_keys(Faker().name())
        driver.find_element(By.XPATH, "//fieldset[2]//input[@name='name']").send_keys(
            f'konstantin_markelov_8_{random.randint(100, 999)}@ya.ru')
        driver.find_element(By.NAME, 'Пароль').send_keys(f'{random.randint(100, 9999)}')
        driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

        assert driver.find_element(By.XPATH, "//fieldset/div/p").text == 'Некорректный пароль'
