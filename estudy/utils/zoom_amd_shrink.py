# 多点触控封装，包括页面的放大缩小
from appium import webdriver
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction


class MultiTouch:
    driver: webdriver = None

    # 获取屏幕大小
    def get_screen_size(self):
        screen_size = self.driver.get_window_size(self)
        x = screen_size['width']
        y = screen_size['height']
        return x, y

    # 放大
    def zoom(self):
        driver = self.driver
        x, y = self.get_screen_size()
        # 初始化MultiAction对象
        add_action = MultiAction(driver)
        # 初始化TouchAction对象，执行手势操作：点击/按压/移动操作
        action1 = TouchAction(driver)
        action2 = TouchAction(driver)
        # 执行短按操作，并移动坐标点，最后通过release释放坐标点来结束动作
        action1.press(x=x * 0.4, y=y * 0.4).wait(1000).move_to(x=x * 0.2, y=y * 0.2).wait(1000).release()
        action2.press(x=x * 0.6, y=y * 0.6).wait(1000).move_to(x=x * 0.8, y=y * 0.8).wait(1000).release()
        # 添加TouchAction对象到MultiAction中
        add_action.add(action1, action2)
        # perform()通过向服务器发送命令来执行动作
        print("start zoom!")
        add_action.perform()

    # 缩小
    def shrink(self):
        driver = self.driver
        x, y = self.get_screen_size()
        # 初始化MultiAction对象
        add_action = MultiAction(driver)
        # 初始化TouchAction对象，执行手势操作：点击/按压/移动操作
        action1 = TouchAction(driver)
        action2 = TouchAction(driver)
        # 执行短按操作，并移动坐标点，最后通过release释放坐标点来结束动作
        action1.press(x=x * 0.2, y=y * 0.2).wait(1000).move_to(x=x * 0.4, y=y * 0.4).wait(1000).release()
        action2.press(x=x * 0.8, y=y * 0.8).wait(1000).move_to(x=x * 0.6, y=y * 0.6).wait(1000).release()
        # 添加TouchAction对象到MultiAction中
        add_action.add(action1, action2)
        # perform()通过向服务器发送命令来执行动作
        print("start shrink!")
        add_action.perform()
