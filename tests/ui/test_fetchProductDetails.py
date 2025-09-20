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
def navHPage(driver):
    driver.get(amazon_url)
    try:
        driver.find_element(By.XPATH, "//button[contains(text(), 'Continue shopping')]").click()
    except:
        pass


@when("user search with the keyword")
def search(driver):
    hPage = amazonPage(driver)
    hPage.productSearch(search_keyword)


@then("extract details of the products from the first 2 pages")
def getDetails(driver):
    gdt = amazonPage(driver)
    global prdList
    prdList = gdt.getDetails(pages)


@then("save the details into an Excel file")
def saveIntoFile(driver):
    ExcelReadWrite.write(output_file, prdList)


@then("check if details of atleast 10 products are fetched")
def productCnt():
    assert len(prdList) >= 10
