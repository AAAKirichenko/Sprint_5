import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Credentials
from locators import Locators

# Выход по кнопке «Выход» в личном кабинете
class TestExitPersonalAccaunt:
    def test_exit_from_personal_account_sucsess(self, driver):
        driver.find_element(*Locators.ENTER_BUTTON).click()
        driver.find_element(*Locators.EMAIL_ENTER).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD_ENTER).send_keys(Credentials.password)
        driver.find_element(*Locators.BUTTON_ENTER).click()
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.BUTTON_EXIT))
        driver.find_element(*Locators.BUTTON_EXIT).click()
        text_form = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.REG_TITLE)).text
        assert text_form == 'Вход'
