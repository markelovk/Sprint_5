from conftest import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as ec

class TestConstructor:
#переход к разделу «Соусы»
    def test_select_sauces(self,driver):
        driver.find_element(By.XPATH,'//*[@id="root"]/div/main/section[1]/div[1]/div[2]').click()
        WW(driver,3).until(ec.visibility_of_element_located((By.XPATH,"//div[contains(@class,'current')]/span[text()='Соусы']")))

        assert driver.find_element(By.XPATH,"//div[contains(@class,'current')]/span").text == 'Соусы'

#переход к разделу «Начинки»
    def test_select_filling(self,driver):
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]').click()
        WW(driver, 3).until(ec.visibility_of_element_located((By.XPATH, "//div[contains(@class,'current')]/span[text()='Начинки']")))

        assert driver.find_element(By.XPATH, "//div[contains(@class,'current')]/span").text == 'Начинки'

#переход к разделу «Булки» из раздела «Начинки»
    def test_select_bun(self,driver):
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]').click()
        WW(driver, 3).until(ec.visibility_of_element_located((By.XPATH, "//div[contains(@class,'current')]/span[text()='Начинки']")))
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]').click()
        WW(driver, 3).until(ec.visibility_of_element_located((By.XPATH, "//div[contains(@class,'current')]/span[text()='Булки']")))

        assert driver.find_element(By.XPATH, "//div[contains(@class,'current')]/span").text == 'Булки'
