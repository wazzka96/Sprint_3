Проект спринта 3.

**В файле tests/registration тесты по заданаию:**

Регистрация.
Проверь:
* Успешную регистрацию. Поле «Имя» должно быть не пустым; в поле Email введён email в формате логин@домен: например, 123@ya.ru. Минимальный пароль — шесть символов. (test_registration_success)
* Ошибку для некорректного пароля. (test_registration_invalid_password)

**В файле tests/login тесты по заданаию:**

Вход.
Проверь:
* вход по кнопке «Войти в аккаунт» на главной, (test_login_from_button_login)
* вход через кнопку «Личный кабинет», (test_login_from_button_account)
* вход через кнопку в форме регистрации, (test_loginh_from_register_page)
* вход через кнопку в форме восстановления пароля.(test_login_from_forgot_password_page)

**В файле tests/profile тесты по заданаию:**

Переход в личный кабинет 

* Проверь переход по клику на «Личный кабинет». (test_open_profile_page)

**В файле tests/constructor тесты по заданаию:**

Переход из личного кабинета в конструктор 

* Проверь переход по клику на «Конструктор» (test_open_constructor_from_register_page)
* и на логотип Stellar Burgers. (test_open_constructor_from_register_page)

Раздел «Конструктор»

Проверь, что работают переходы к разделам:
* «Булки», (test_switch_tab_buns)
* «Соусы», (test_switch_tab_sauces)
* «Начинки». (test_switch_tab_toppings)

**В файле tests/logout тесты по заданаию:**
Выход из аккаунта
* Проверь выход по кнопке «Выйти» в личном кабинете. (test_logout)

Локаторы описаны в файле lokators/lokators

Все тесты воспроизводятся успешно в двух браузерах (Chrome и Mozilla), проработаны ожидания загрузки страницы (спиннер), так что можно запускать тесты сразу все.#   S p r i n t _ 3  
 #   S p r i n t _ 3  
 