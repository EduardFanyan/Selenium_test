import pytest


@pytest.fixture()
def set_up():
    print('Старт тест')
    yield
    print('Конец теста')


@pytest.fixture(scope="module")
def set_group():
    print('Вход в систем')
    yield
    print('Выход из системы')
