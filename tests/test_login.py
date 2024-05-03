from conftest import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as ec

class TestLogin:
#вход по кнопке «Войти в аккаунт» на главной странице
    def test_login_main_page(self,driver):
        driver.find_element(By.XPATH, "//main//button[text()='Войти в аккаунт']").click()
        WW(driver,10).until(ec.visibility_of_element_located((By.XPATH,"//h2[text()='Вход']")))
        driver.find_element(By.XPATH,"//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input").send_keys('konstantin_markelov_8_014@ya.ru')
        driver.find_element(By.XPATH,"//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input").send_keys('123456')
        driver.find_element(By.XPATH,"//*[@id='root']/div/main/div/form/button").click()
        WW(driver,10).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='root']/div/main/section[2]/div/button[text()='Оформить заказ']")))

        assert driver.find_element(By.XPATH,'//*[@id="root"]/div/main/section[2]/div/button').text == 'Оформить заказ'


#вход через кнопку «Личный кабинет»
    def test_login_from_profile(self, driver):
        driver.find_element(By.XPATH,'//*[@id="root"]/div/header/nav/a').click()
        WW(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))
        driver.find_element(By.XPATH,"//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input").send_keys('konstantin_markelov_8_014@ya.ru')
        driver.find_element(By.XPATH,"//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input").send_keys('123456')
        driver.find_element(By.XPATH,"//*[@id='root']/div/main/div/form/button").click()
        WW(driver,10).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='root']/div/main/section[2]/div/button[text()='Оформить заказ']")))

        assert driver.find_element(By.XPATH,'//*[@id="root"]/div/main/section[2]/div/button').text == 'Оформить заказ'


#вход через кнопку в форме регистрации
    def test_login_through_registration_button(self,driver):
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()
        WW(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))
        driver.find_element(By.XPATH, "//a[text()='Зарегистрироваться']").click()
        WW(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//h2[text()='Регистрация']")))
        driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/div/p/a').click()
        WW(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))
        driver.find_element(By.XPATH,"//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input").send_keys('konstantin_markelov_8_014@ya.ru')
        driver.find_element(By.XPATH,"//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input").send_keys('123456')
        driver.find_element(By.XPATH,"//*[@id='root']/div/main/div/form/button").click()
        WW(driver,10).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='root']/div/main/section[2]/div/button[text()='Оформить заказ']")))

        assert driver.find_element(By.XPATH,'//*[@id="root"]/div/main/section[2]/div/button').text == 'Оформить заказ'


#вход через кнопку в форме восстановления пароля
    def test_login_through_password_reset_button(self,driver):
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()
        WW(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))
        driver.find_element(By.XPATH, "//a[text()='Восстановить пароль']").click()
        WW(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//h2[text()='Восстановление пароля']")))
        driver.find_element(By.XPATH, "//a[text()='Войти']").click()
        WW(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))
        driver.find_element(By.XPATH,"//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input").send_keys('konstantin_markelov_8_014@ya.ru')
        driver.find_element(By.XPATH,"//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input").send_keys('123456')
        driver.find_element(By.XPATH,"//*[@id='root']/div/main/div/form/button").click()
        WW(driver,10).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='root']/div/main/section[2]/div/button[text()='Оформить заказ']")))

        assert driver.find_element(By.XPATH,'//*[@id="root"]/div/main/section[2]/div/button').text == 'Оформить заказ'
