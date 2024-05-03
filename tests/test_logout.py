from conftest import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as ec

class TestLogout:
#выход по кнопке «Выйти» в личном кабинете
    def test_click_button_exit_in_personal_cabinet(self,driver):
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()
        WW(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))
        driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input").send_keys('konstantin_markelov_8_014@ya.ru')
        driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input").send_keys('123456')
        driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/button").click()
        WW(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/main/section[2]/div/button")))
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()
        WW(driver,10).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='root']/div/main/div/nav/ul/li[1]/a")))
        driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/nav/ul/li[3]/button').click()
        WW(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))

        assert driver.find_element(By.XPATH,'//h2').text == 'Вход' and driver.current_url == 'https://stellarburgers.nomoreparties.site/login'