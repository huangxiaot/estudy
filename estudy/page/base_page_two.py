# 基础类，封装元素定位操作
from appium import webdriver


class BasePageTwo:
    def __init__(self, driver: webdriver):
        self.driver = driver

    # 根据android-uiautomator定位
    def element_android_uiautomator(self, locator):
        return self.driver.find_element_by_android_uiautomator(locator)

    # 根据android-uiautomators定位
    def elements_android_uiautomator(self, locator):
        return self.driver.find_elements_by_android_uiautomator(locator)

    def find_element_au(self, locator):
        try:
            return self.driver.find_element_by_android_uiautomator(locator)
        except:
            return self.driver.find_elements_by_android_uiautomator(locator)
