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
        y1 = screen_size['height'] * 0.75
        # 终点 y 坐标
        y2 = screen_size['height'] * 0.25
        self.driver.swipe(x1, y1, x1, y2, t)

    # 下滑
    def swipe_down(self, t):
        screen_size = self.get_screen_size()
        x1 = screen_size['width'] * 0.5
        y1 = screen_size['height'] * 0.25
        y2 = screen_size['height'] * 0.75
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
        screen_size = self.get_screen_size()
        x1 = screen_size['width'] * 0.2
        y1 = screen_size['height'] * 0.5
        x2 = screen_size['width'] * 0.8
        self.driver.swipe(x1, y1, x2, y1, t)

    # 下滑
    def swipe_down_search(self, t):
        screen_size = self.get_screen_size()
        x1 = screen_size['width'] * 0.5
        y1 = screen_size['height'] * 0.5
        y2 = screen_size['height'] * 0.75
        self.driver.swipe(x1, y1, x1, y2, t)

    # 修改宝贝信息页面的下滑
    def swipe_down_baby_relation(self, t):
        screen_size = self.get_screen_size()
        x1 = screen_size['width'] * 0.5
        y1 = screen_size['height'] * 0.85
        y2 = screen_size['height'] * 0.95
        self.driver.swipe(x1, y1, x1, y2, t)

    # 修改宝贝信息页面的上滑
    def swipe_up_baby_relation(self, t):
        screen_size = self.get_screen_size()
        # 起始x坐标
        x1 = screen_size['width'] * 0.5
        # 起始 y 坐标
        y1 = screen_size['height'] * 0.95
        # 终点 y 坐标
        y2 = screen_size['height'] * 0.85
        self.driver.swipe(x1, y1, x1, y2, t)
