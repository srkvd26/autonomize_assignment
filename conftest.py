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

@pytest.fixture(scope="session")
def logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(f"./data/QA_Automation.log")
    formatter = logging.Formatter("%(asctime)s - %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger