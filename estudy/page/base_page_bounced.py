# 基础类，封装元素定位操作
from appium import webdriver


class BasePageBounced:
    # 计数：统计查找元素的次数
    i = 0
    # 黑名单列表中的元素位置
    black_list_locator = 0
    # 黑名单：异常弹框的元素
    black_list = [
        'className("android.view.View").text("点击签到")'
        'className("android.view.View").text("今日已签到，邀请好友奖励翻倍")'
    ]

    # 初始化
    def __init__(self, driver: webdriver):
        self.driver = driver

    """元素定位
        1.判断目标元素是否存在
        2.存在：则点击目标元素
        3.不存在：开始进行查找弹框处理
    """

    def find_element(self, locator):
        try:
            print("查找元素 %s" % locator)
            return self.android_uiautomator(locator)
        except:
            # 当查找完黑名单中的元素，但仍然没有定位到想要的元素，则跳出异常处理，此时需要将查找次数和元素位置归零
            if BasePageBounced.i > BasePageBounced.black_list_locator:
                print("跳出异常处理")
                BasePageBounced.i = 0
                BasePageBounced.handle_locator = 0
                return self.android_uiautomator(locator)
            print("进入弹框处理第 %s 次 " % BasePageBounced.i)
            # 当黑名单的元素没有查找完，则继续查找
            self.handle_exception()

    """异常弹框处理
        1.查找黑名单中的元素
        2.存在：点击
        3.不存在：则进入查找元素函数，查找是否存在目标元素
    """

    def handle_exception(self):
        print(":exception")
        self.driver.implicitly_wait(10)
        # 定位黑名单中元素的位置
        handle_elements = self.black_list[BasePageBounced.black_list_locator]  # 相当于black_list[0]
        BasePageBounced.i += 1
        BasePageBounced.black_list_locator += 1
        print(handle_elements)
        # 调用函数判断是否存在黑名单中的元素
        elements = self.is_element_present(handle_elements)
        # 找到异常弹框的元素，将计数和黑名单位置清0，则点击
        if elements:
            BasePageBounced.i = 0
            BasePageBounced.black_list_locator = 0
            self.find_element(handle_elements).click()
        # 未找到异常弹框的元素，则返回查找元素函数，查找是否存在目标元素
        else:
            print("没找到元素")
            return self.find_element(handle_elements)

    # 判断是否找到想要的元素
    def is_element_present(self, locator):
        try:
            self.android_uiautomator(locator)
        except Exception as e:
            # 打印异常信息
            print(e)
            # 发生了 NoSuchElementException异常，说明页面中未找到该元素，返回False
            return False
        else:
            # 没有发生异常，表示在页面中找到了该元素，返回True
            return True

    # 根据android uiautomator和xpath定位
    def android_uiautomator(self, locator):
        try:
            return self.driver.find_element_by_android_uiautomator(locator)
        except:
            return self.driver.find_element_by_xpath(*locator)
