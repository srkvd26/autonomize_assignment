import pytest
from pytest_bdd import *
from pages.searchPage import amazonPage
from selenium.webdriver.common.by import By
from utils.excelReadWrite import ExcelReadWrite

scenarios("../features/productsList.feature")

@given("the user is on the amazon home page")
def navHPage(driver):
    driver.get("https://www.amazon.in/")
    try:
        driver.find_element(By.XPATH, "//button[contains(text(), 'Continue shopping')]").click()
    except:
        pass

@when("user search with 'mobile' keyword")
def search(driver):
    hPage = amazonPage(driver)
    hPage.productSearch('mobile')

@then("extract details of the products from the first 2 pages")
def getDetails(driver):
    gdt = amazonPage(driver)
    global prdList
    prdList = gdt.getDetails(2)
    

@then("save the details into an Excel file")
def saveIntoFile(driver):
    ExcelReadWrite.write("./data/prdDetails.xlsx", prdList)

@then("check if details of atleast 10 products are fetched")
def productCnt():
    assert len(prdList) >= 10