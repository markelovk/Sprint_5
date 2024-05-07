Спринт 5

Дополнения:

conftest.py - содержит фикстуру с драйвером и переход на тестовый сайт
locators.py - содержит описание всех применяемых локаторов в тестах

Тесты:

test_registration.py - содержит тесты: 
на регистрацию нового пользователя - test_succecfully_registration
на наличие ошибки для некорректного ввода пароля - test_invalid_password

test_login.py - содержит тесты:
вход по кнопке «Войти в аккаунт» на главной странице - test_login_main_page
вход через кнопку «Личный кабинет» - test_login_from_profile
вход через кнопку в форме регистрации - test_login_through_registration_button
вход через кнопку в форме восстановления пароля - test_login_through_password_reset_button

test_logout.py - содержит тесты:
выход по кнопке «Выйти» в личном кабинете - test_click_button_exit_in_personal_cabinet

test_go_to_constructor.py - содержит тесты:
переход по клику на «Конструктор» из Личного кабинета - test_go_to_constructor_from_personal_cabinet
переход по клику на логотип Stellar Burgers из Личного кабинета - test_go_to_logo_from_personal_cabinet

test_go_to_personal_cabinet.py - содержит тесты:
переход по клику на «Личный кабинет» - test_click_personal_cabinet

test_constructor.py - содержит тесты:
переход к разделу «Соусы» - test_select_sauces
переход к разделу «Начинки» - test_select_filling
переход к разделу «Булки» из раздела «Начинки» - test_select_bun
# Sprint_5