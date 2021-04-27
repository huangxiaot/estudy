# 快乐伴读页面
import time
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.base_page_two import BasePageTwo
from page.editor_baby_info_page import EditorBabyInfoPage
from page.my_page import MyPage
from page.search_page import Search


class ReadingPartnerPage(BasePage):
    # 搜索框
    _tv_search = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView"
    # 左上角我的页面入口
    _iv_my = (By.ID, "com.intretech.readerx:id/img_toolbar_main_avatar")
    # 宝贝信息页面入口
    _iv_baby_info = (By.ID, "com.intretech.readerx:id/img_person_portrait")

    """进入搜索页面"""
    def enter_search(self):
        time.sleep(1)
        self.find_element_xpath(self._tv_search).click()
        return Search(self.driver)

    """进入我的--修改宝贝信息页面"""
    def enter_editor_baby_info_page(self):
        time.sleep(1)
        self.find_element_id(self._iv_my).click()
        self.find_element_id(self._iv_baby_info).click()
        return EditorBabyInfoPage(self.driver)


# 以下内容为根据android uiautomator定位的测试
class ReadingPartnerPageTwo(BasePageTwo):

    """以下元素为根据android uiautomator定位"""
    _my = 'resourceId("com.intretech.readerx:id/img_toolbar_main_avatar")'

    """进入我的页面"""
    def enter_my_page(self):
        time.sleep(1)
        self.element_android_uiautomator(self._my).click()
        return MyPage(self.driver)
