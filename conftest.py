from selenium import webdriver
import pytest
import logging
import os


@pytest.fixture()
def driver():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()