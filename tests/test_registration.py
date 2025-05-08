from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper import generate_registration_data_for_error_password
from helper import generate_registration_data
from locators import Locators


class TestRegistrationWithNewCredentials:
    def test_sucsess_registration(self, driver):
        #arrange
        name, email, password = generate_registration_data()
        driver.find_element(*Locators.ENTER_BUTTON).click()
        driver.find_element(*Locators.REG_LINK).click()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        #act
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(Locators.REG_TITLE, "Вход"))
        reg_text = driver.find_element(*Locators.REG_TITLE).text
        #assert
        assert reg_text == 'Вход'
        assert 'login' in driver.current_url


class TestRegistrationIncorrectPassword:
    def test_filed_registration(self, driver):
        # arrange
        name, email, password = generate_registration_data_for_error_password()
        driver.find_element(*Locators.ENTER_BUTTON).click()
        driver.find_element(*Locators.REG_LINK).click()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        # act
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        error_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.TEXT_REG_ERROR)).text
        # assert
        assert error_text == 'Некорректный пароль'

