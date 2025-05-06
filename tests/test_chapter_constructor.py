from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

# Переход к разделам "Булки"
class TestChapterBuns:
    def test_chapter_buns_activate(self, driver):
        buns_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((Locators.BUNS_BUTTON)))
        driver.execute_script("arguments[0].click();", buns_tab)
        active_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class, 'tab_type_current')]//span[text()='Булки']"))
        )
        assert active_tab.is_displayed(), "Таб 'Булки' не стал активным"

# Переход к разделу "Соусы"
class TestChapterSauces:
    def test_chapter_sauces_activate(self, driver):
        sau_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.SAUCES_BUTTON))
        driver.execute_script("arguments[0].click();", sau_tab)
        active_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class, 'tab_type_current')]//span[text()='Соусы']"))
        )
        assert active_tab.is_displayed(), "Таб 'Соусы' не стал активным"

    # Переход к разделу "Начинки"
class TestChapterFillings:
    def test_chapter_fillings_activate(self, driver):
        fil_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.FILLINGS_BUTTON))
        driver.execute_script("arguments[0].click();", fil_tab)
        active_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class, 'tab_type_current')]//span[text()='Начинки']"))
        )
        assert active_tab.is_displayed(), "Таб 'Начинки' не стал активным"