from conftest import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as ec

class TestPersonalCabinetNavigation:
#переход по клику на «Конструктор» из Личного кабинета
    def test_go_to_constructor_from_personal_cabinet(self,driver):
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()
        WW(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a').click()
        WW(driver,10).until(ec.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))

        assert driver.find_element(By.XPATH,"//h1").text == 'Соберите бургер' and driver.current_url == 'https://stellarburgers.nomoreparties.site/'


#переход по клику на логотип Stellar Burgers из Личного кабинета
    def test_go_to_logo_from_personal_cabinet(self,driver):
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()
        WW(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/div/a').click()
        WW(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))

        assert driver.find_element(By.XPATH, "//h1").text == 'Соберите бургер' and driver.current_url == 'https://stellarburgers.nomoreparties.site/'
