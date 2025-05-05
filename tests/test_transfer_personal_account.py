
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Credentials
from locators import Locators

# Переход по клику на «Личный кабинет»
class TestTransferPersonalAccount:
    def test_transfer_personal_account_sucsess(self, driver):
        driver.find_element(*Locators.ENTER_BUTTON).click()
        driver.find_element(*Locators.EMAIL_ENTER).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD_ENTER).send_keys(Credentials.password)
        driver.find_element(*Locators.BUTTON_ENTER).click()
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        text_form = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.TEXT_ON_PERSONAL_ACCOUNT)).text
        assert text_form == 'Профиль'
        assert 'profile' in driver.current_url