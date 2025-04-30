from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials
from helper import generate_registration_data
from locators import Locators
#from curl import *

class TestRegistrationWithNewCredentials:

    def test_sucsess_registration(self, driver):
        #arrange
        name, email, password = generate_registration_data()
        driver.find_element(*Locators.ENTER_BUTTON).click()
        driver.find_element(*Locators.REG_LINK).click()
        #WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.NAME))

        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        #act
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        reg_text = WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(Locators.REG_TITLE, "Вход")
        )
        #assert
        assert reg_text == 'Вход'
        assert 'login' in driver.current_url


#class TestCheckingCreationExistingAccount:

    #def test_failed_registration(self, driver):
        #driver.find_element(*Locators.ENTER_BUTTON).click()
        #driver.find_element(*Locators.REG_LINK).click()
        #driver.find_element(*Locators.NAME).send_keys(Credentials.name)


        #driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        #driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        #driver.find_element(*Locators.REGISTER_BUTTON).click()
        #reg_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.REG_POPUP)).text
        #assert reg_text == 'Что-то пошло не так!\nПопробуйте ещё раз.'
