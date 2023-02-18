from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

register_url = 'https://stellarburgers.nomoreparties.site/register'
start_page_url = 'https://stellarburgers.nomoreparties.site'


class TestConstructor:
    # Тест на переход по клику на «Конструктор»
    def test_open_constructor_from_register_page(self, init_driver):
        init_driver.get(register_url)  # открытие стартовой страницы
        WebDriverWait(init_driver, 30).until(
            EC.invisibility_of_element_located((By.XPATH, "//img[@alt='loading animation']")))  # ожидание пропадания спиннера загрузки
        WebDriverWait(init_driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Конструктор')]"))).click()  # ожидание кнопки перехода в конструктор и нажатие на неё

        assert WebDriverWait(init_driver, 20).until(EC.url_changes("https://stellarburgers.nomoreparties.site"))  # проверка смены адреса страницы на главную
        assert WebDriverWait(init_driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(text(),'Булки')]")))  # проверка наличия вкладки "Булки"

    # Тест на переход по клику на логотип Stellar Burgers
    def test_open_startpage_from_register_page(self, init_driver):
        init_driver.get(register_url)  # открытие стартовой страницы
        WebDriverWait(init_driver, 30).until(
            EC.invisibility_of_element_located((By.XPATH, "//img[@alt='loading animation']")))  # ожидание пропадания спиннера загрузки
        WebDriverWait(init_driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@*, 'logo')]"))).click()  # ожидание кнопки логотипа и нажатие на неё

        assert WebDriverWait(init_driver, 20).until(EC.url_changes("https://stellarburgers.nomoreparties.site"))  # проверка смены адреса страницы на главную
        assert WebDriverWait(init_driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[contains(text(),'Булки')]")))  # проверка наличия вкладки "Булки"

    # Тест на переход к разделу Булки
    def test_switch_tab_buns(self, init_driver):
        init_driver.get(start_page_url)  # открытие стартовой страницы
        WebDriverWait(init_driver, 30).until(
            EC.invisibility_of_element_located((By.XPATH, "//img[@alt='loading animation']")))  # ожидание пропадания спиннера загрузки
        WebDriverWait(init_driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Соусы')]"))).click()  # ожидание кнопки перехода на раздел Соусы и нажатие на неё
        WebDriverWait(init_driver, 30).until(
            EC.invisibility_of_element_located((By.XPATH, "//div[contains(@*, 'tab_tab_type_current')]/span[contains(text(),'Булки')]")))  # ожидание снятия активного флага с разделок Булок

        init_driver.find_element(By.XPATH, "//span[contains(text(),'Булки')]").click()  # нажатие на кнопку перехода в раздел Булок

        assert WebDriverWait(init_driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@*, 'tab_tab_type_current')]/span[contains(text(),'Булки')]")))  # ожидание, что вкладка булок станет активной

    # Тест на переход к разделу Соусы
    def test_switch_tab_sauces(self, init_driver):
        init_driver.get(start_page_url)  # открытие стартовой страницы
        WebDriverWait(init_driver, 30).until(
            EC.invisibility_of_element_located((By.XPATH, "//img[@alt='loading animation']")))  # ожидание пропадания спиннера загрузки
        WebDriverWait(init_driver, 30).until(
            EC.invisibility_of_element_located((By.XPATH, "//div[contains(@*, 'tab_tab_type_current')]/span[contains(text(),'Соусы')]")))  # ожидание отсутствия активного флага с разделок Булок
        init_driver.find_element(By.XPATH, "//span[contains(text(),'Соусы')]").click()  # переход в раздел Соусов

        assert WebDriverWait(init_driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@*, 'tab_tab_type_current')]/span[contains(text(),'Соусы')]")))  # ожидание, что вкладка соусов станет активной

    # Тест на переход к разделу Начинки
    def test_switch_tab_toppings(self, init_driver):
        init_driver.get(start_page_url)  # открытие стартовой страницы
        WebDriverWait(init_driver, 30).until(
            EC.invisibility_of_element_located((By.XPATH, "//img[@alt='loading animation']")))  # ожидание пропадания спиннера загрузки
        WebDriverWait(init_driver, 30).until(
            EC.invisibility_of_element_located((By.XPATH, "//div[contains(@*, 'tab_tab_type_current')]/span[contains(text(),'Начинки')]")))  # ожидание отсутствия активного флага с разделок Булок
        init_driver.find_element(By.XPATH, "//span[contains(text(),'Начинки')]").click()  # переход в раздел Соусов

        assert WebDriverWait(init_driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@*, 'tab_tab_type_current')]/span[contains(text(),'Начинки')]")))  # ожидание, что вкладка соусов станет активной
