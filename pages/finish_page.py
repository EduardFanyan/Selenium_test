from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class FinishPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы

    # Методы

    # Действия

    # Метод финиш

    def finish(self):
        self.get_current_url()
        self.get_screenshot()
