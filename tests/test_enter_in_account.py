from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Credentials
from locators import Locators

# Вход по кнопке «Войти в аккаунт» на главной
class TestEnterToAccountButtonInMain:
    def test_sucsess_enter(self, driver):
        driver.find_element(*Locators.ENTER_BUTTON).click()
        driver.find_element(*Locators.EMAIL_ENTER).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD_ENTER).send_keys(Credentials.password)
        driver.find_element(*Locators.BUTTON_ENTER).click()
        text_enter = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.TEXT_ENTER)).text
        assert text_enter == 'Соберите бургер'

# вход через кнопку «Личный кабинет»
class TestEnterToAccountButtonPersonalAccount:
    def test_sucsess_enter_personal_account(self, driver):
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL_ENTER).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD_ENTER).send_keys(Credentials.password)
        driver.find_element(*Locators.BUTTON_ENTER).click()
        text_enter = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.TEXT_ENTER)).text
        assert text_enter == 'Соберите бургер'

# Вход через кнопку в форме регистрации
class TestEnterToAccountButtonEnterFormRegistration:
    def test_sucsess_enter_form_registration(self, driver):
        driver.find_element(*Locators.ENTER_BUTTON).click()
        driver.find_element(*Locators.REG_LINK).click()
        driver.find_element(*Locators.ENTER_LINK_FOR_REGISTRATOIN).click()
        driver.find_element(*Locators.EMAIL_ENTER).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD_ENTER).send_keys(Credentials.password)
        driver.find_element(*Locators.BUTTON_ENTER).click()
        text_enter = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.TEXT_ENTER)).text
        assert text_enter == 'Соберите бургер'

# Вход через кнопку в форме восстановления пароля
class TestEnterToAccountFormRecoverPassword:
    def test_sucsess_enter_form_recover_password(self, driver):
        driver.find_element(*Locators.ENTER_BUTTON).click()
        driver.find_element(*Locators.RECOVER_PASSWORD).click()
        driver.find_element(*Locators. ENTER_FORM_RECOVER_PASSWORD).click()
        driver.find_element(*Locators.EMAIL_ENTER).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD_ENTER).send_keys(Credentials.password)
        driver.find_element(*Locators.BUTTON_ENTER).click()
        text_enter = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.TEXT_ENTER)).text
        assert text_enter == 'Соберите бургер'