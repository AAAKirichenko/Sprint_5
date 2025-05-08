
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Credentials
from locators import Locators

# Переход по клику на конструктор из Личного Кабинета
class TestTransferInConstructor:
    def test_transfer_in_constructor_sucsess(self, driver):
        driver.find_element(*Locators.ENTER_BUTTON).click()
        driver.find_element(*Locators.EMAIL_ENTER).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD_ENTER).send_keys(Credentials.password)
        driver.find_element(*Locators.BUTTON_ENTER).click()
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.BUTTON_CONSTRUCTOR).click()
        text_form = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.TEXT_ENTER)).text
        assert text_form == 'Соберите бургер'

# Переход на логотип Stellar Burgers из Личного Кабинета
class TestTransferOnLogotip:
    def test_transfer_on_logotip_sucsess(self, driver):
        driver.find_element(*Locators.ENTER_BUTTON).click()
        driver.find_element(*Locators.EMAIL_ENTER).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD_ENTER).send_keys(Credentials.password)
        driver.find_element(*Locators.BUTTON_ENTER).click()
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.LOGOTIP).click()
        text_form = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.TEXT_ENTER)).text
        assert text_form == 'Соберите бургер'