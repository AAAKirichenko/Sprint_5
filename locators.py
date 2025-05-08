from selenium.webdriver.common.by import By

class Locators:

    #1 Локаторы для регистрации
    # Кнопка "Войти в аккаунт"
    ENTER_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    # Ссылка "Зарегистрироваться"
    REG_LINK = (By.XPATH, "//a[@class='Auth_link__1fOlj']")
    # Поле "Имя"
    NAME = (By.XPATH, "//div[label[contains(text(), 'Имя')]]//input")
    # Поле "Email"
    EMAIL = (By.XPATH, "//div[label[contains(text(), 'Email')]]//input")
    # Поле "Пароль"
    PASSWORD = (By.CSS_SELECTOR, "input[name='Пароль']")
    # Кнопка "Зарегистрироваться"
    REGISTER_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    # Заголовок "Вход"
    REG_TITLE = (By.XPATH, "//h2[text()='Вход']")
    # Текст ошибки пароля
    TEXT_REG_ERROR = (By.XPATH, "//p[@class='input__error text_type_main-default']")


    #2 Вход
    # Поле Email на форме для входа после регистрации
    EMAIL_ENTER = (By.XPATH, "//div[label[contains(text(), 'Email')]]//input")
    # Поле Пароль на форме для входа после регистрации
    PASSWORD_ENTER = (By.XPATH, "//div[label[contains(text(), 'Пароль')]]//input")
    #Кнопка "Войти"
    BUTTON_ENTER = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    # Текст проверки после входа на форму - собери бургер
    TEXT_ENTER = (By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10']")
    # Кнопка "Личный кабинет"
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")
    # Ссылка "Войти" в форме регистрации
    ENTER_LINK_FOR_REGISTRATOIN = (By.XPATH, "//a[@class='Auth_link__1fOlj']")
    # Кнопка "Восстановить пароль"
    RECOVER_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']")
    # Кнопка "Войти" на форме восстановления пароля
    ENTER_FORM_RECOVER_PASSWORD = (By.XPATH, "//a[text()='Войти']")

    #3 Переход в личный кабинет
    # Текст "Профиль" в личном кабинете
    TEXT_ON_PERSONAL_ACCOUNT = (By.XPATH, "//a[text()='Профиль']")

    #4 Переход из личного кабинета в конструктор и на логотип
    # Кнопка "Конструктор" в личном кабинете
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")
    # Логотип
    LOGOTIP = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")

    #5 Выход из аккаунта
    # Кнопка "Выход" в личном кабинете
    BUTTON_EXIT = (By.XPATH, "//button[text()='Выход']")

    #6 Раздел "Конструктор"
    # Кнопка "Булки"
    BUNS_BUTTON = (By.XPATH, ".//span[contains(text(), 'Булки')]")
    # Проверка активности раздела "Булки"
    ACTIV_BUNS_BUTTON = (By.XPATH, "//div[contains(@class, 'tab_type_current')]//span[text()='Булки']")
    # Кнопка "Соусы"
    SAUCES_BUTTON = (By.XPATH, "//span[text()='Соусы']")
    # Проверка активности раздела "Соусы"
    ACTIV_SAUCES_BUTTON = (By.XPATH, "//div[contains(@class, 'tab_type_current')]//span[text()='Соусы']")
    #Кнопка "Начинки"
    FILLINGS_BUTTON = (By.XPATH, "//span[text()='Начинки']")
    # Проверка активности раздела "Начинки"
    ACTIV_FILLINGS_BUTTON = (By.XPATH, "//div[contains(@class, 'tab_type_current')]//span[text()='Начинки']")
