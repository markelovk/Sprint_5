from conftest import driver
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as ec

class TestPersonalCabinet:
# переход по клику на «Личный кабинет»
    def test_click_personal_cabinet(self,driver):
        driver.find_element(*Locators.button_pers_cabinet).click()
        WW(driver, 10).until(ec.visibility_of_element_located(Locators.title_sign_in))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
