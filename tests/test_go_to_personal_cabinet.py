from conftest import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as ec

class TestPersonalCabinet:
# переход по клику на «Личный кабинет»
    def test_click_personal_cabinet(self,driver):
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a').click()
        WW(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
