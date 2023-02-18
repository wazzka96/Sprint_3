from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

test_email = "qqqq@ana.st"
test_password = "qqqqQQQQ"

login_url = 'https://stellarburgers.nomoreparties.site/login'
profile_url = 'https://stellarburgers.nomoreparties.site/account/profile'
start_page_url = 'https://stellarburgers.nomoreparties.site'


class TestProfile:
    # Тест перехода по клику на «Личный кабинет»
    def test_open_profile_page(self, init_driver):
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

        # Переход в личный кабинет

        WebDriverWait(init_driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='/account']"))).click()  # ожидание кнопки входа в личных кабинет и нажатие на неё

        assert WebDriverWait(init_driver, 30).until(EC.url_to_be(profile_url))  # ожидание смены адреса со стартовой страницы на профайл
        assert init_driver.find_element(By.XPATH, "//p[contains(text(),'В этом разделе вы можете изменить свои персональные данные')]")