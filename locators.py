from selenium.webdriver.common.by import By

class RegistrationLocators:
    REG_NAME_INPUT_FIELD = (By.XPATH, "//label[text()='Имя']/parent::*/input") #Поле Имя в Регистарции
    REG_EMAIL_INPUT_FIELD = (By.XPATH, "//label[text()='Email']/parent::*/input") #Поле Имэйл в Регистрации
    REG_PASSWORD_INPUT_FIELD = (By.XPATH, "//input[@name='Пароль']") #Поле Пароля в Регистрации
    SUBMIT_BUTTON = (By.XPATH,"//button[text()='Зарегистрироваться']") #Кнопка Зарегистрироваться в окне регистрации
    REG_INCORRECT_PASSWORD = (By.XPATH, "//p[@class='input__error text_type_main-default' and text()='Некорректный пароль']") #Надпись Некорректный пароль

class LoginLocators:
    EMAIL_INPUT_FIELD = (By.XPATH, "//label[text()='Email']/parent::*/input") #Поле ввода Имэйл
    PASSWORD_INPUT_FIELD = (By.XPATH, "//input[@name='Пароль']") #Поле ввода Пароля
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']") #Кнопка Войти
    REGISTER_BUTTON = (By.XPATH, "//a[text()= 'Зарегистрироваться']") #Кнопка Зарегистрироваться в окне входа в аккаунт
    RESTORE_PASSWORD = (By.XPATH, "//a[text()= 'Восстановить пароль']") #Переход на окно Восстановления пароля
    EMAIL_RESTORE_FIELD = (By.XPATH, "//label[text()= 'Email']") #Поле ввода Имэйла в окне восстановления пароля
    RESTORE_BUTTON = (By.XPATH, "//button[text()= 'Восстановить']") #Кнопка Восстановить

class MainPageLocators:
    MAIN_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") #Кнопка Войти в аккаунт на главной странице сайта
    PERSONAL_CABINET_BUTTON = (By.XPATH, "//p[text()= 'Личный Кабинет']") #Раздел Личный Кабинет
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()= 'Конструктор']") #Раздел Конструктор
    LOGO_BUTTON = (By.XPATH, "//div[contains(@class, 'logo')]") #Раздел Логотип

class CabinetPageLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']") #Кнопка Выход в Личном Кабинете

class ConstructorPageLocators:
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']") #Раздел с Булками
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']") #Раздел с Соусами
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']") #Раздел с Начинками
    CURRENT_SECTION = (By.XPATH, "//div[contains(@class, 'current')]") #Класс, показывающий какой элемент выбран на странице