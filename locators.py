from selenium.webdriver.common.by import By


class Locators:
    # Локаторы для регистрации

    # Кнопка "Войти в аккаунт"
    ENTER_BUTTON = By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"
    # Ссылка "Зарегистрироваться"
    REG_LINK = By.XPATH, "//a[@class='Auth_link__1fOlj']"
    #REG_POPUP = (By.XPATH, "//p[@class='popup__status-message']")
    # Поле "Имя"
    NAME = By.XPATH, "//div[label[contains(text(), 'Имя')]]//input"
    # Поле "Email"
    EMAIL = (By.XPATH, "//div[label[contains(text(), 'Email')]]//input")
    # Поле "Пароль"
    PASSWORD = (By.CSS_SELECTOR, "input[name='Пароль']")
    # Кнопка "Зарегистрироваться"
    REGISTER_BUTTON = By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
    # Заголовок Вход
    REG_TITLE = By.XPATH, "//h2[text()='Вход']"
    # Текст ошибки пароля
    TEXT_REG_ERROR = By.XPATH, "//p[@class='input__error text_type_main-default']"



    # Поле Email на форме для входа после регистрации
    EMAIL_ENTER = (By.XPATH, "//form[@class='Auth_form__3qKeq mb-20']//label[text()='Email']")
    PASSWORD_ENTER = (By.XPATH, "//form[@class='Auth_form__3qKeq mb-20']//label[text()='Пароль']")
    BUTTON_ENTER = By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"

    # Текст при повторной попытке зарегистрироваться
    REG_POPUP = (By.XPATH, "//p[@class='input__error text_type_main-default']") # Такой пользователь уже существует

    # Локаторы для изменения аватара
    #PROFILE_IMAGE = (By.XPATH, "//div[@class='profile__image']")
    #AVATAR_INPUT = (By.ID, "owner-avatar")
    #UPDATE_AVATAR_BUTTON = (By.XPATH, "//form[@name='edit-avatar']/button[@class='button popup__button']")
    #CARDS = (By.CLASS_NAME, "card__image")