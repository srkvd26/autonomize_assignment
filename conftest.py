from selenium import webdriver
import pytest
import logging
import pytest_html


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
    logger = logging.getLogger("QA_Automation")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler("./data/QA_Automation.log", encoding="utf-8")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

#Set custom title for the HTML report
def pytest_html_report_title(report):
    report.title = "QA Automation Test Report"