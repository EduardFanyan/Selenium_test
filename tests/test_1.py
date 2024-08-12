from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.cart_pages import CartPage
from pages.client_information_pages import ClientInformationPage
from pages.finish_page import FinishPage
from pages.login_pages import LoginPage
from pages.main_pages import MainPage
from pages.payment_page import PaymentPage


def test_11():
    service = Service(executable_path=r'C:\Users\Edward\Desktop\driver\chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=service, options=options)

    print('Старт теста')

    login = LoginPage(driver)
    login.authorization()
    mp = MainPage(driver)
    mp.select_product()
    cp = CartPage(driver)
    cp.product_confirmation()
    cip = ClientInformationPage(driver)
    cip.input_information()
    p = PaymentPage(driver)
    p.payment()
    f = FinishPage(driver)
    f.get_screenshot()