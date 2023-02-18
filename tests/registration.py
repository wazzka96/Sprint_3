from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

faker = Faker('ru_RU')
register_url = 'https://stellarburgers.nomoreparties.site/register'

class TestRegistration:
    # Тест на успешную регистрацию
    def test_registration_success(self, init_driver):
        mail = faker.email()
        password = faker.password(length=6, special_chars=True, digits=True, upper_case=True, lower_case=True)
        name = faker.name()

        init_driver.get(register_url)   # Переход на страницу регистрации
        WebDriverWait(init_driver, 30).until(
            EC.invisibility_of_element_located((By.XPATH, "//img[@alt='loading animation']")))  # ожидание пропадания спиннера загрузки
        init_driver.find_element(By.XPATH, "//label[contains(text(),'Имя')]/../input").send_keys(name)   # ввод рандомного имени
        init_driver.find_element(By.XPATH, "//label[contains(text(),'Email')]/../input").send_keys(mail)   # ввод рандомного эмейла
        init_driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(password)   # ввод рандомного пароля
        init_driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click()   # нажатие на кнопку регистрации
        WebDriverWait(init_driver, 30).until(
            EC.invisibility_of_element_located((By.XPATH, "//img[@alt='loading animation']")))  # ожидание пропадания спиннера загрузки

        assert WebDriverWait(init_driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))   # проверка смены адреса страницы на авторизацию
        assert WebDriverWait(init_driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Войти')]")))   # проверка наличия кнопки на странице авторизации (как дополнительный факт подтверждения успешного перехода)

        # Далее дополнительная проверка на авторизацию. Но хз  нужна ли она тут. Был-бы какой-то алерт об успешной
        # регистрации, ориентировалась бы на него
        init_driver.find_element(By.XPATH, "//label[contains(text(),'Email')]/../input").send_keys(mail)   # ввод эмейла, который использовался при регистрации
        init_driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(password)   # ввод пароля, который использовался при регистрации

        init_driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()   # нажатие на кнопку входа
        WebDriverWait(init_driver, 30).until(
            EC.invisibility_of_element_located((By.XPATH, "//img[@alt='loading animation']")))  # ожидание пропадания спиннера загрузки

        assert WebDriverWait(init_driver, 10).until(EC.url_changes("https://stellarburgers.nomoreparties.site"))   # проверка смены адреса страницы на главную
        assert WebDriverWait(init_driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))   # проверка наличия кнопки оформления заказа (как дополнительный факт подтверждения успешного перехода)

    # Тест на ошибку для некорректного пароля
    def test_registration_invalid_password(self, init_driver):
        mail = faker.email()
        password = faker.password(length=5, special_chars=True, digits=True, upper_case=True, lower_case=True)   # генерация рандомного невалидного пароля
        name = faker.name()   # генерация рандомного имени

        init_driver.get(register_url)   # Переход на страницу регистрации
        WebDriverWait(init_driver, 30).until(
            EC.invisibility_of_element_located((By.XPATH, "//img[@alt='loading animation']")))  # ожидание пропадания спиннера загрузки
        init_driver.find_element(By.XPATH, "//label[contains(text(),'Имя')]/../input").send_keys(name)   # ввод рандомного имени
        init_driver.find_element(By.XPATH, "//label[contains(text(),'Email')]/../input").send_keys(mail)   # ввод рандомного эмейла
        init_driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(password)   # ввод рандомного пароля
        init_driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click()   # нажатие на кнопку регистрации

        assert WebDriverWait(init_driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Некорректный пароль')]")))   # проверка наличия сообщения об ошибке (некорректный пароль)
