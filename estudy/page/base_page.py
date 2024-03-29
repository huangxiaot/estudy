# 基础类，封装元素定位操作
from appium import webdriver


class BasePage:
    def __init__(self, driver: webdriver):
        self.driver = driver

    """通过id定位"""
    def find_element_id(self, locator):
        try:
            return self.driver.find_element(*locator)
        except:
            return self.driver.find_elements(*locator)

    """通过xpath定位"""
    def find_element_xpath(self, locator):
        try:
            return self.driver.find_element_by_xpath(locator)
        except:
            return self.driver.find_elements(locator)

    """根据classname定位"""
    def find_element_classname(self, *locator):
        return self.driver.find_elements_by_class_name(*locator)
