from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

test_email = "qqqq@ana.st"
test_password = "qqqqQQQQ"
start_page_url = 'https://stellarburgers.nomoreparties.site'
login_url = 'https://stellarburgers.nomoreparties.site/login'
register_url = 'https://stellarburgers.nomoreparties.site/register'
forgot_password_url = 'https://stellarburgers.nomoreparties.site/forgot-password'


class TestLogOut:
    # Тест на выход по кнопке «Выйти» в личном кабинете
    def test_logout(self, init_driver):
        # Авторизация

        init_driver.get(start_page_url)  # открытие стартовой страницы
        WebDriverWait(init_driver, 30).until(
            EC.invisibility_of_element_located((By.XPATH, "//img[@alt='loading animation']")))  # ожидание пропадания спиннера загрузки
        WebDriverWait(init_driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Войти в аккаунт')]"))).click()  # ожидание кнопки входа в аккаунт и нажатие на неё
        WebDriverWait(init_driver, 30).until(
            EC.url_to_be(login_url))  # ожидание смены адреса страницы со статовой на страницу авторизации
        init_driver.find_element(By.XPATH, "//label[contains(text(),'Email')]/../input").send_keys(
            test_email)  # ввод эмейла
        init_driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(test_password)  # ввод пароля
        init_driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()  # нажатие на кнопку входа
        WebDriverWait(init_driver, 30).until(
            EC.invisibility_of_element_located((By.XPATH, "//img[@alt='loading animation']")))  # ожидание пропадания спиннера загрузки
        WebDriverWait(init_driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))  # ожидание загрузки элемента на статовой странице

        # Открытие личного кабинета
        init_driver.find_element(By.XPATH, "//a[@href='/account']").click()  # нажатие на кнопку входа в личный кабинет
        WebDriverWait(init_driver, 30).until(EC.visibility_of_element_located((
            By.XPATH, "//p[contains(text(),'В этом разделе вы можете изменить свои персональные данные')]")))  # ожидание текстового элемента в личном кабинете

        # Логаут
        init_driver.find_element(By.XPATH, "//button[contains(text(),'Выход')]").click()  # нажатие на кнопку выхода

        assert WebDriverWait(init_driver, 30).until(EC.url_to_be(login_url))  # проверка смены адреса страницы с личного кабинета на авторизацию
        assert init_driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]")
