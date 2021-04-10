# 绑定手机号页面
import re
import time

from appium import webdriver
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from utils.server import InvokeServer
from utils.toast import Toast


class BindPhonePage(BasePage):

    driver: webdriver = None

    def __init__(self, driver):
        super().__init__(driver)
        self.invoke_server = InvokeServer(driver)
        self.toast = Toast(driver)

    """绑定手机号页面元素"""
    # 手机号输入框
    _et_phone_number = (By.ID, "com.intretech.readerx:id/edit_bind_phone_number")
    # 验证码输入框
    _et_verify_code = (By.ID, "com.intretech.readerx:id/edit_bind_phone_check_code")
    # 获取验证码按钮
    _tv_get_code = (By.ID, "com.intretech.readerx:id/tv_bind_phone_get_code")
    # 下一步按钮
    _iv_next = (By.ID, "com.intretech.readerx:id/btn_bind_phone_next")
    # 通知栏的短信内容
    _message_text = (By.ID, "android:id/big_text")
    # 添加家庭圈页面右上角跳过按钮
    _tv_add_family_skip = (By.ID, "com.intretech.readerx:id/btn_toolbar_more")

    """首页(快乐伴读)元素"""
    # 左上角我的页面入口
    _iv_my = (By.ID, "com.intretech.readerx:id/img_toolbar_main_avatar")

    """我的页面--我的账号元素"""
    # 我的账号入口
    _rl_my_count = (By.ID, "com.intretech.readerx:id/layout_reader_learn_report")
    # 我的账号中手机号显示
    _tv_my_account_phone_display = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[3]/android.widget.TextView[2]"
    # 退出登录按钮
    _rl_logout = (By.ID, "com.intretech.readerx:id/layout_person_logout")
    # 退出登录弹框-确认
    _tv_logout_confirm = (By.ID, "com.intretech.readerx:id/view_dialog_confirm")

    """输入手机号码"""
    def input_phone_number(self, phone):
        self.find_element_id(self._et_phone_number).clear()
        self.find_element_id(self._et_phone_number).send_keys(phone)

    """输入验证码"""
    def input_verify_code(self, verify_code):
        self.find_element_id(self._et_verify_code).clear()
        self.find_element_id(self._et_verify_code).send_keys(verify_code)

    """调用测试服清除账号接口，清除账号信息"""
    """由于一个手机号每天只能发送10条验证码，现使用特殊版本，不需要验证码就能登录"""
    def register_and_logout(self, phone):
        # 输入手机号
        self.input_phone_number(phone)
        # 获取验证码
        self.find_element_id(self._tv_get_code).click()
        time.sleep(20)
        # 点击下一步
        self.find_element_id(self._iv_next).click()
        # 点击跳过按钮
        self.find_element_id(self._tv_add_family_skip).click()
        # 点击左上角我的头像，进入我的页面
        self.find_element_id(self._iv_my).click()
        # 点击我的账号--退出登录--确认
        self.find_element_id(self._rl_my_count).click()
        self.find_element_id(self._rl_logout).click()
        self.find_element_id(self._tv_logout_confirm).click()
        time.sleep(2)

    """2.连续点击两次输入验证码"""
    def repeat_get_verify_code(self, phone):
        self.input_phone_number(phone)
        btn_get_code = self.find_element_id(self._tv_get_code)
        for i in range(2):
            btn_get_code.click()

    """3.自动获取短信验证码"""
    def auto_fill_verify_code(self):
        pass

    """通过手机通知栏自动获取短信验证码"""
    def auto_get_verify_code(self):
        time.sleep(2)
        # 打开通知栏
        self.driver.open_notifications()
        # 获取短信内容
        message = self.find_element_id(self._message_text)
        tx_message_code = message.text
        print(tx_message_code)
        # 通过正则匹配短信内容中的验证码，使用r前缀可以自动转义，不需要手动转换字符串
        verify_code = re.findall(r'[\d]{4}', tx_message_code)
        print(verify_code)
        # 关闭通知栏
        self.driver.press_keycode(4)
        return verify_code

    """我的--我的账号页面手机号码显示"""
    def my_account_page_phone_display(self):
        my_account_phone_display = self.find_element_xpath(self._tv_my_account_phone_display).text
        return my_account_phone_display

    """绑定手机号页面输入的手机号码显示"""
    def bind_page_phone_display(self):
        bind_phone_display = self.find_element_id(self._et_phone_number).text
        return bind_phone_display
