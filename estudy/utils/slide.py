# 定义公共类，封装页面上下左右滑动操作
from appium import webdriver
from page.base_page import BasePage


class Slide(BasePage):
    driver: webdriver = None

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
