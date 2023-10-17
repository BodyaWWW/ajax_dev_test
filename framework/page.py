
class Page:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()
