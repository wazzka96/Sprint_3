from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

test_email = "qqqq@ana.st"
test_password = "qqqqQQQQ"
start_page_url = 'https://stellarburgers.nomoreparties.site'
login_url = 'https://stellarburgers.nomoreparties.site/login'
register_url = 'https://stellarburgers.nomoreparties.site/register'
forgot_password_url = 'https://stellarburgers.nomoreparties.site/forgot-password'


class TestLogIn:
    # Тест на вход по кнопке «Войти в аккаунт» на главной
    def test_login_from_button_login(self, init_driver):
        init_driver.get(start_page_url)    # открытие стартовой страницы
        WebDriverWait(init_driver, 30).until(
            EC.invisibility_of_element_located((By.XPATH, "//img[@alt='loading animation']")))  # ожидание пропадания спиннера загрузки
        WebDriverWait(init_driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Войти в аккаунт')]"))).click()    # ожидание кнопки входа в аккаунт и нажатие на неё

        WebDriverWait(init_driver, 30).until(EC.url_to_be(login_url))    # ожидание смены адреса страницы со статовой на страницу авторизации

        init_driver.find_element(By.XPATH, "//label[contains(text(),'Email')]/../input").send_keys(test_email)    # ввод эмейла
        init_driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(test_password)    # ввод пароля

        init_driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()    # нажатие на кнопку входа
        WebDriverWait(init_driver, 30).until(
            EC.invisibility_of_element_located((By.XPATH, "//img[@alt='loading animation']")))  # ожидание пропадания спиннера загрузки

        assert WebDriverWait(init_driver, 30).until(EC.url_changes(start_page_url))    # проверка смены адреса страницы со страницы авторизации на стартовую
        assert WebDriverWait(init_driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))    # проверка наличия кнопки оформления заказа (появляется вместо кнопки входа в аккаунт приуспешной авторизации)

    # Тест на вход через кнопку «Личный кабинет»
    def test_login_from_button_account(self, init_driver):
        init_driver.get(start_page_url)    # открытие стартовой страницы
        WebDriverWait(init_driver, 30).until(
            EC.invisibility_of_element_located((By.XPATH, "//img[@alt='loading animation']")))  # ожидание пропадания спиннера загрузки
        WebDriverWait(init_driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='/account']"))).click()    # ожидание кнопки входа в личных кабинет и нажатие на неё

        WebDriverWait(init_driver, 30).until(EC.url_to_be(login_url))    # ожидание смены адреса со стартовой страницы на авторизацию
        WebDriverWait(init_driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Войти')]")))    # ожидание кнопки входа для подтверждения, что страница загрузилась

        init_driver.find_element(By.XPATH, "//label[contains(text(),'Email')]/../input").send_keys(test_email)    # ввод эемейла
        init_driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(test_password)    # ввод пароля

        init_driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()    # нажатие на кнопку входа
        WebDriverWait(init_driver, 30).until(
            EC.invisibility_of_element_located((By.XPATH, "//img[@alt='loading animation']")))  # ожидание пропадания спиннера загрузки

        assert WebDriverWait(init_driver, 30).until(EC.url_changes(start_page_url))    # проверка смены адреса со страницы авторизаци на стартовую
        assert WebDriverWait(init_driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))    # проверка наличия кнопки оформления заказа (появляется вместо кнопки входа в аккаунт приуспешной авторизации)

    # Тест на вход через кнопку в форме регистрации
    def test_loginh_from_register_page(self, init_driver):
        init_driver.get(forgot_password_url)    # открытие страницы восстановления пароля
        WebDriverWait(init_driver, 30).until(
            EC.invisibility_of_element_located((By.XPATH, "//img[@alt='loading animation']")))  # ожидание пропадания спиннера загрузки
        WebDriverWait(init_driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Войти')]"))).click()    # ожидание кнопки входа и нажатие на неё

        WebDriverWait(init_driver, 30).until(
            EC.url_to_be(login_url))  # ожидание смены адреса страницы с регистрации на страницу авторизации

        init_driver.find_element(By.XPATH, "//label[contains(text(),'Email')]/../input").send_keys(
            test_email)  # ввод эмейла
        init_driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(test_password)  # ввод пароля

        init_driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()  # нажатие на кнопку входа
        WebDriverWait(init_driver, 30).until(
            EC.invisibility_of_element_located((By.XPATH, "//img[@alt='loading animation']")))  # ожидание пропадания спиннера загрузки

        assert WebDriverWait(init_driver, 30).until(
            EC.url_changes(start_page_url))  # проверка смены адреса страницы со страницы авторизации на стартовую
        assert WebDriverWait(init_driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))  # проверка наличия кнопки оформления заказа (появляется вместо кнопки входа в аккаунт приуспешной авторизации)

    # Тест на вход через кнопку в форме восстановления пароля
    def test_login_from_forgot_password_page(self, init_driver):
        init_driver.get(register_url)    # открытие страницы регистрации
        WebDriverWait(init_driver, 30).until(
            EC.invisibility_of_element_located((By.XPATH, "//img[@alt='loading animation']")))  # ожидание пропадания спиннера загрузки
        WebDriverWait(init_driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Войти')]"))).click()    # ожидание кнопки входа и нажатие на неё

        WebDriverWait(init_driver, 30).until(
            EC.url_to_be(login_url))  # ожидание смены адреса страницы с регистрации на страницу авторизации

        init_driver.find_element(By.XPATH, "//label[contains(text(),'Email')]/../input").send_keys(
            test_email)  # ввод эмейла
        init_driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(test_password)  # ввод пароля

        init_driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()  # нажатие на кнопку входа
        WebDriverWait(init_driver, 30).until(
            EC.invisibility_of_element_located((By.XPATH, "//img[@alt='loading animation']")))  # ожидание пропадания спиннера загрузки

        assert WebDriverWait(init_driver, 30).until(
            EC.url_changes(start_page_url))  # проверка смены адреса страницы со страницы авторизации на стартовую
        assert WebDriverWait(init_driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))  # проверка наличия кнопки оформления заказа (появляется вместо кнопки входа в аккаунт приуспешной авторизации)