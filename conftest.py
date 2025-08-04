import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait


# Add command-line options
def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help='Browser to use: chrome, firefox, edge')
    parser.addoption('--os_type', action='store', default='windows', help='Operating system: windows or mac')


# Browser getter
@pytest.fixture(scope='module')
def browser(request):
    return request.config.getoption('--browser').lower()


@pytest.fixture(scope='module')
def os_type(request):
    return request.config.getoption('--os_type').lower()


# Set up before all tests in the module
@pytest.fixture(scope='class')
def onetimesetup(request, browser, os_type):
    print(
        f"\n==================== Starting tests on {browser.capitalize()} ({os_type.capitalize()}) ====================")

    driver = None

    if browser == 'chrome':
        options = ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(options=options)

    elif browser == 'firefox':
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)

    elif browser == 'edge':
        options = EdgeOptions()
        driver = webdriver.Edge(options=options)

    else:
        raise ValueError(f"Browser '{browser}' is not supported. Use chrome, firefox, or edge.")

    driver.maximize_window()
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 10)

    # Attach to the request context so it's accessible in test classes
    request.cls.driver = driver
    request.cls.wait = wait

    yield
    print("\n==================== THE END of all the tests ====================")
    driver.quit()


# Runs before each test
@pytest.fixture()
def setup():
    print('\n---------- Automation test for Morningexpert.com ----------')
    yield
    print('---------- THE END of the test ----------')
