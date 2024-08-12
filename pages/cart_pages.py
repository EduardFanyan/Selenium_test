from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы

    checkout_button = "//button[@id='checkout']"

    # Методы

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    # Действия

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print('Жмем Подтверждение')

    # Метод Подтверждение

    def product_confirmation(self):
        self.get_current_url()
        self.click_checkout_button()
