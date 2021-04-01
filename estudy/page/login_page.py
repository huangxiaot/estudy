# 登录页面显示
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.bind_phone_page import BindPhonePage


class LoginPage(BasePage):
    # 微信登录按钮
    _iv_wechat_login = (By.ID, "com.intretech.readerx:id/img_welcome_login")

    """新用户进入绑定手机号页面"""
    def enter_bind_phone_page(self):
        self.find_element_id(self._iv_wechat_login).click()
        return BindPhonePage(self.driver)
