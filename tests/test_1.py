from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_pages import Login_page


def test_11():
    service = Service(executable_path=r'C:\Users\Edward\Desktop\driver\chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=service, options=options)

    print('Старт теста')

    login = Login_page(driver)
    login.authorization()
