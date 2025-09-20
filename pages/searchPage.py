from selenium.webdriver.common.by import By
from utils.selenium_helpers import CommonAction


class amazonPage(CommonAction):
    #Locators of required elements on amazon page
    searchtxt_field = (By.XPATH, "//*[@id='twotabsearchtextbox']")
    search_btn = (By.XPATH, "//*[@id='nav-search-submit-text']")
    products = (By.XPATH, "//*[@data-component-type = 's-search-result' and @class = 'sg-col-4-of-4 sg-col-20-of-24 s-result-item s-asin sg-col-16-of-20 sg-col sg-col-12-of-12 s-widget-spacing-small sg-col-8-of-8 sg-col-12-of-16']")
    title_tag = (By.XPATH, ".//h2/span")
    #price_tag = None
    #rating_tag = None
    #reviews_tag = None
    nxtpg = (By.XPATH, "//a[contains(@aria-label, 'Go to next page')]")

    def productSearch(self, keyword):
        self.find_element(self.searchtxt_field).send_keys(keyword)
        self.find_element(self.search_btn).click()
    

    def getDetails(self, pages):
        products_lst = []
        for p in range(pages):
            products = self.find_elements(self.products)
            #print(len(items))
            for product in products:
                title = self.get_text((self.title_tag, product)).split('|')[0]
                #price = self.get_text((self.price_tag, product))
                #rating = self.get_text((self.rating_tag, product))
                #reviews = self.get_text((self.reviews_tag, product))

                products_lst.append(
                    {"title": title,
                     "price": 0,
                     "rating": 0,
                     "reviews": 0
                    }
                )
            if p < pages-1:
                self.find_element(self.nxtpg).click()
        return products_lst