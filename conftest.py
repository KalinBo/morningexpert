import pytest


@pytest.fixture()
def setup():
    print('Automation test for Morningexpert.com')
    yield
    print('THE END of the test')


@pytest.fixture(scope='module')
def onetimesetup(browser, os_type):
    print('*************************** Starting tests ....... ***********************')
    yield
    print('********************* THE END of all the tests *********************')


def pytest_addoption(parser):
    parser.addoption('--browser')
    parser.addoption('--os_type', help='Windows or Mac')


@pytest.fixture(scope='module')
def browser(request):
    return request.config.getoption('--browser')


@pytest.fixture(scope='module')
def os_type(request):
    return request.config.getoption('--os_type')