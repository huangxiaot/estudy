# 绑定手机号页面
import time
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from utils.server import InvokeServer


class BindPhonePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.invoke_server = InvokeServer(driver)

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

    """输入手机号码"""
    def input_phone_number(self, phone):
        self.find_element_id(self._et_phone_number).clear()
        self.find_element_id(self._et_phone_number).send_keys(phone)

    """输入验证码"""
    def input_verify_code(self, verify_code):
        self.find_element_id(self._et_verify_code).clear()
        self.find_element_id(self._et_verify_code).send_keys(verify_code)

    """1.手机号输入"""
    def success(self, phone):
        self.input_phone_number(phone)
        self.find_element_id(self._tv_get_code).click()
        # self.input_verify_code(verify_code)
        time.sleep(20)
        self.find_element_id(self._iv_next).click()
