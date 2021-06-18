# 我的页面相关操作
import time
from page.base_page_two import BasePageTwo
from page.my_account_page import MyAccountPage


class MyPage(BasePageTwo):
    _rl_my_account = 'resourceId("com.intretech.readerx:id/layout_reader_learn_report")'
    _vv_course = 'resourceId("com.intretech.readerx:id/layout_person_set_schedule")'

    # 进入我的账号页面
    def enter_my_account_page(self):
        time.sleep(1)
        self.element_android_uiautomator(self._rl_my_account).click()
        return MyAccountPage(self.driver)
