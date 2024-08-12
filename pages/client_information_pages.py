from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class ClientInformationPage(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы

    first_name = "//input[@id='first-name']"
    last_name = "//input[@id='last-name']"
    postal_code = "//input[@id='postal-code']"
    continue_button = "//input[@id='continue']"

    # Методы

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_postal_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.postal_code)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    # Действия

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print('Вводим имя')

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print('Вводим фамилию')

    def input_postal_code(self, postal_code):
        self.get_postal_code().send_keys(postal_code)
        print('Вводим Почтовый индекс')

    def click_continue_button(self):
        self.get_continue_button().click()
        print('Жмем подтверждение')

    # Метод авторизации

    def input_information(self):
        self.get_current_url()
        self.input_first_name('Eduard')
        self.input_last_name('Fanyan')
        self.input_postal_code('12345')
        self.click_continue_button()
