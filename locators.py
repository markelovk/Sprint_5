from selenium.webdriver.common.by import By
class Locators:
    personal_cabinet = By.XPATH, "//p[text()='Личный Кабинет']"#Заголовок "Личный Кабинет"
    button_pers_cabinet = By.XPATH, '//*[@id="root"]/div/header/nav/a' # Кнопка "Личный кабинет"
    title_sign_in = By.XPATH, "//h2[text()='Вход']" #Заголовок "Вход"
    button_registration_page_pers_cab = By.XPATH, "//a[text()='Зарегистрироваться']" #Кнопка Зарегистрироваться на странице ЛК
    title_registration = By.XPATH, "//h2[text()='Регистрация']" #Заголовок "Регистрация"
    field_name = By.XPATH, "//label[text()='Имя']/following-sibling::input"#Поле ввода Имя
    field_email = By.XPATH, "//label[text()='Email']/following-sibling::input"#Поле ввода Email
    field_password = By.NAME, 'Пароль'#Поле ввода Пароль
    button_registration = By.XPATH, "//button[text()='Зарегистрироваться']"#Кнопка Зарегистрироваться
    title_h2 = By.XPATH, "//h2"#Заголовок h2
    message_wrong_password = By.XPATH, "//fieldset/div/p"#Сообщение Некорректный пароль
    button_sign_in_to_account = By.XPATH, "//main//button[text()='Войти в аккаунт']"#Кнопка Войти в аккаунт
    field_email_page_sign_in = By.XPATH,"//*[@class='input__container']//label[text()='Email']/following-sibling::input"#Поле ввода Email на странице входа
    field_password_page_sign_in = By.XPATH,"//*[@class='input__container']//label[text()='Пароль']/following-sibling::input"#Поле ввода Пароль на странице входа
    button_sign_in = By.XPATH,"//*[@id='root']/div/main/div/form/button"#Кнопка Войти
    button_create_order_text = By.XPATH,"//main//button[text()='Оформить заказ']"#Кнопка с текстом Оформить заказ
    button_sign_in_page_registration = By.XPATH,"//main//p/a[text()='Войти']"#Кнопка Войти на странице Регистрация
    button_restore_password = By.XPATH, "//a[text()='Восстановить пароль']"#Кнопка Восстановить пароль
    title_restore_password = By.XPATH, "//h2[text()='Восстановление пароля']"#Заголовок "Восстановление пароля"
    button_sign_in_page_restore_password = By.XPATH, "//a[text()='Войти']"#Кнопка Войти на странице Восстановление пароля
    button_constructor = By.XPATH, "//*[text()='Конструктор']/parent::*"#Кнопка Конструктор на странице ЛК
    title_take_burger = By.XPATH, "//h1[text()='Соберите бургер']"#Заголовок "Соберите бургер"
    title_h1 = By.XPATH, "//h1"#Заголовок h1
    button_logo = By.XPATH, '//*[@id="root"]/div/header/nav/div/a'#Кнопка Логотип
    button_profile = By.XPATH,"//main//a[text()='Профиль']"#Кнопка Профиль
    button_logout = By.XPATH,"//main//li/button[text()='Выход']"#Кнопка Выход
    button_buns = By.XPATH, "//span[text()='Булки']/parent::*"#Кнопка "Булки"
    button_sauces = By.XPATH,"//span[text()='Соусы']/parent::*"#Кнопка "Соусы"
    buttong_filling = By.XPATH,"//span[text()='Начинки']/parent::*"#Кнопка"Начинки"
    select_buns = By.XPATH, "//div[contains(@class,'current')]/span[text()='Булки']"#Выбран раздел "Булки"
    select_sauces = By.XPATH,"//div[contains(@class,'current')]/span[text()='Соусы']"#Выбран раздел "Соусы"
    select_filling = By.XPATH, "//div[contains(@class,'current')]/span[text()='Начинки']"#Выбран раздел "Начинки"
    select_button = By.XPATH,"//div[contains(@class,'current')]/span"#Выбранный раздел
    button_create_order = By.XPATH,"//button[contains(@class,'button_button__33qZ0')]"#Кнопка Оформить заказ
