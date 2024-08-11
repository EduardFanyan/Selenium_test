from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Login_page(Base):

    url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы

    user_name = "//*[@id='user-name']"
    password = "//*[@id='password']"
    login_button = "//*[@id='login-button']"

    # Методы

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_button_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    # Действия

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print('Вводим имя')

    def input_password(self, login_password):
        self.get_password().send_keys(login_password)
        print('Вводим пароль')

    def click_button_login(self):
        self.get_button_login().click()
        print('Жмием залогиниться')


    #Метод авторизации

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.input_password('secret_sauce')
        self.input_user_name('standard_user')
        self.click_button_login()
