import pytest
from pytest_bdd import *
from pages.searchPage import amazonPage
from selenium.webdriver.common.by import By
from utils.excelReadWrite import ExcelReadWrite
from utils.configReader import ConfigReader

scenarios("../features/productsList.feature")

config = ConfigReader()
amazon_url = config.get("amazon", "url")
search_keyword = config.get("amazon", "search_keyword")
pages = config.getint("amazon", "pages")
output_file = config.get("amazon", "output_file")


@given("the user is on the amazon home page")
def navHPage(driver, logger):
    driver.get(amazon_url)
    logger.info(f"Navigated to Amazon URL: {amazon_url}")
    try:
        driver.find_element(By.XPATH, "//button[contains(text(), 'Continue shopping')]").click()
        logger.info("Dismissed 'Continue shopping' prompt")
    except:
        logger.info("No prompt displayed")


@when("user search with the keyword")
def search(driver, logger):
    hPage = amazonPage(driver)
    hPage.productSearch(search_keyword)
    logger.info(f"Searched Amazon with keyword: {search_keyword}")


@then("extract details of the products from the first 2 pages")
def getDetails(driver, logger):
    gdt = amazonPage(driver)
    global prdList
    prdList = gdt.getDetails(pages)
    logger.info(f"Extracted {len(prdList)} products from {pages} pages")


@then("save the details into an Excel file")
def saveIntoFile(driver, logger):
    ExcelReadWrite.write(output_file, prdList)
    logger.info(f"Saved product details into {output_file}")


@then("check if details of atleast 10 products are fetched")
def productCnt(logger):
    assert len(prdList) >= 10
    logger.info(f"Product count validation passed: {len(prdList)} products")
