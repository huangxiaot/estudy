# 定义公共类，封装页面上下左右滑动操作
from appium import webdriver
from page.base_page import BasePage


class Slide(BasePage):
    driver: webdriver = None

    """
        以下为swipe()，可以根据自己需要设置滑动的距离：swipe（self，start_x, start_y,end_x,end_y,duration)
        start_x－开始滑动的x坐标；
        start_y －开始滑动的y坐标 ；
        end_x －结束点x坐标；
        end_y －结束点y坐标； 
        duration 滑动时间（默认5毫秒）
    """
    # 获取当前手机屏幕的大小
    def get_screen_size(self):
        return self.driver.get_window_size(self)

    # 上滑
    def swipe_up(self, t):
        screen_size = self.get_screen_size()
        # 起始x坐标
        x1 = screen_size['width'] * 0.5
        # 起始 y 坐标
        y1 = screen_size['height'] * 0.8
        # 终点 y 坐标
        y2 = screen_size['height'] * 0.2
        self.driver.swipe(x1, y1, x1, y2, t)

    # 下滑
    def swipe_down(self, t):
        screen_size = self.get_screen_size()
        x1 = screen_size['width'] * 0.5
        y1 = screen_size['height'] * 0.2
        y2 = screen_size['height'] * 0.8
        self.driver.swipe(x1, y1, x1, y2, t)

    # 左滑
    def swipe_left(self, t):
        screen_size = self.get_screen_size()
        x1 = screen_size['width'] * 0.8
        y1 = screen_size['height'] * 0.5
        x2 = screen_size['width'] * 0.2
        self.driver.swipe(x1, y1, x2, y1, t)

    # 右滑
    def swipe_right(self, t):
        print("111")
        screen_size = self.get_screen_size()
        x1 = screen_size['width'] * 0.2
        y1 = screen_size['height'] * 0.5
        x2 = screen_size['width'] * 0.8
        self.driver.swipe(x1, y1, x2, y1, t)

    """
        以下为scroll()，可以根据页面中两个元素位置距离进行滑动：scroll(self, origin_el, destination_el, duration=None)：
        - originalEl - 开始要滚动的元素
        - destinationEl - 要滚动到的元素
        - 即从元素origin_el滚动至元素destination_el
        - duration 即滚动的持续时间
        driver.scroll(el1,el2)
    """

    def scroll(self, el1, el2, t):
        self.find_element_xpath(el1)
        self.find_element_xpath(el2)
        self.driver.scroll(el1, el2, t)
