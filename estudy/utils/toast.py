# 定义公共类，封装获取toast提示
from selenium.webdriver.support.wait import WebDriverWait
from page.base_page import BasePage


class Toast(BasePage):
    # 获取toast信息
    def get_toast(self, message):
        driver = self.driver
        try:
            toast_message = '//*[@text=\'{}\']'.format(message)
            toast_element = WebDriverWait(driver, 5, 0.5).until(lambda driver: self.driver.find_element_by_xpath(toast_message))
            print(toast_element.text)
            return toast_element.text
        except:
            print("没有找到这个toast！")
