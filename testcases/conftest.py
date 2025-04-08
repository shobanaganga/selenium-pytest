from selenium import webdriver
import pytest

@pytest.fixture(autouse=True)
def setup(request,browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    if browser == "firefox":
        driver = webdriver.Firefox()
    if browser == "edge":
        driver = webdriver.Edge()
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")
    #parser.addoption("--url")

@pytest.fixture(scope="class",autouse=True)
def browser(request):
    return request.config.getoption("--browser")

#@pytest.fixture(scope="class",autouse=True)
#def url(request):
 #   return request.config.getoption("--url")
