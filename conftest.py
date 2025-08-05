import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Comma-separated browsers (chrome,firefox,edge)"
    )

def pytest_generate_tests(metafunc):
    if "browser_name" in metafunc.fixturenames:
        browser_option = metafunc.config.getoption("browser")
        browsers = browser_option.split(",")
        metafunc.parametrize("browser_name", browsers)

@pytest.fixture(scope="function")
def driver_setup(request, browser_name):
    driver = None

    if browser_name == "chrome":
        options = ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.set_preference("dom.webnotifications.enabled", False)  # disable notifications
        options.set_preference("permissions.default.desktop-notification", 2)  # deny permission by default
        driver = webdriver.Firefox(options=options)

    elif browser_name == "edge":
        options = EdgeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Edge(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.maximize_window()
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 10)

    request.cls.driver = driver
    request.cls.wait = wait

    yield

    driver.quit()
