from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class CommonAction:
    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 30)

    def find_element(self, locator, parent = None):
        if parent:
            return parent.find_element(*locator)
        return self.driver.find_element(*locator)

    def find_elements(self, locator, parent = None):
        if parent:
            return parent.find_elements(*locator)
        return self.driver.find_elements(*locator)

    def wait_till_located(self, locator, all = None):
        if all:
            return self._wait.until(EC.presence_of_all_elements_located(locator))
        return self._wait.until(EC.presence_of_element_located(locator))

    def wait_till_clickable(self, locator):
        return self._wait.until(EC.element_to_be_clickable(locator))

    def wait_till_seen(self, locator):
        return self._wait.until(EC.visibility_of_element_located(locator))

    def click_enter_key(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.ENTER).perform()

    def scroll_till_visible(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def get_text(self, locator, parent = None):
        if parent:
            element = self.find_element(locator, parent)
        else:
            element = self.find_element(locator)
        return element.text
    
    def getAttribute(self, locator, atrbt, parent):
        if parent:
            element = self.find_element(locator, parent)
        else:
            element = self.find_element(locator)
        return element.get_attribute(atrbt)