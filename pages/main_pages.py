from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы

    select_product_1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    cart = "//div[@id='shopping_cart_container']"
    menu = "//button[@id='react-burger-menu-btn']"
    link_about = "//a[@id='about_sidebar_link']"

    # Методы

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu)))

    def get_link_about(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_about)))

    # Действия

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print('Добавляю продукт 1 в корзину')

    def click_cart(self):
        self.get_cart().click()
        print('Жму на корзину')

    def click_menu(self):
        self.get_menu().click()
        print('Жму на меню')

    def click_link_about(self):
        self.get_link_about().click()
        print('Жму на about')

    # Методы

    def select_product(self):
        self.get_current_url()
        self.click_select_product_1()
        self.click_cart()

    def select_menu_about(self):
        self.get_current_url()
        self.click_menu()
        self.click_link_about()
        self.assert_url('https://saucelabs.com/')