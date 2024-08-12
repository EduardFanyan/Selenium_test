

class Base():

    def __init__(self, driver):
        self.driver = driver


    """Метод возвращающий URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Текущий URL: " + get_url)


    """Метод проверяющий слова"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result, 'Слово не найдено'
        print("Слово найдено")
