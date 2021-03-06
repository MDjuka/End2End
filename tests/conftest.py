import pytest
from selenium import webdriver
import logging as logger


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="class")
def setup(request, browser, url):
    driver = None
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    driver.get(url)
    logger.info("Logging to URL address")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
