from selenium import webdriver
import pytest
import logging
import os


@pytest.fixture(scope="session")
def driver():
    global driver
    optns = webdriver.ChromeOptions()
    optns.add_argument("--incognito")
    driver = webdriver.Chrome(options=optns)
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()