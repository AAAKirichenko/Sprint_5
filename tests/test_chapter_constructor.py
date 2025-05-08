from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

# Переход между разделами в Конструкторе
class TestChaptersConstructor:

    # Переход к разделам "Булки"
    def test_chapter_buns_activate(self, driver):
        buns_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((Locators.BUNS_BUTTON)))
        driver.execute_script("arguments[0].click();", buns_tab)
        active_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (Locators.ACTIV_BUNS_BUTTON))
        )
        assert active_tab.is_displayed(), "Таб 'Булки' не стал активным"

    # Переход к разделу "Соусы"
    def test_chapter_sauces_activate(self, driver):
        sau_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.SAUCES_BUTTON))
        driver.execute_script("arguments[0].click();", sau_tab)
        active_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (Locators.ACTIV_SAUCES_BUTTON))
        )
        assert active_tab.is_displayed(), "Таб 'Соусы' не стал активным"

    # Переход к разделу "Начинки"
    def test_chapter_fillings_activate(self, driver):
        fil_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.FILLINGS_BUTTON))
        driver.execute_script("arguments[0].click();", fil_tab)
        active_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (Locators.ACTIV_FILLINGS_BUTTON))
        )
        assert active_tab.is_displayed(), "Таб 'Начинки' не стал активным"