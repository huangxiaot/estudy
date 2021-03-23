# 设备管理--网络配置--填写WiFi信息页面
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.connect_guide_page import ConnectGuidePage


class FillWifiInformationPage(BasePage):
    # WiFi账号输入框
    _et_wifi_account = (By.ID, "com.intretech.readerx:id/edit_wifi_name")
    # WiFi密码输入框
    _et_wifi_pwd = (By.ID, "com.intretech.readerx:id/edit_wifi_pwd")
    # 下一步按钮
    _tv_next = (By.ID, "com.intretech.readerx:id/btn_wifi_start")

    """WiFi账号密码输入框设置"""
    def input_account_pwd(self, account, pwd):
        # 清除WiFi账号输入框内容，并输入WiFi账号
        self.find_element_id(self._et_wifi_account).clear()
        self.find_element_id(self._et_wifi_account).send_keys(account)
        # 清除WiFi密码输入框内容，并输入WiFi密码
        self.find_element_id(self._et_wifi_pwd).clear()
        self.find_element_id(self._et_wifi_pwd).send_keys(pwd)

    """输入WiFi账号密码，点击下一步，进入连接引导页面"""
    def enter_connect_guide(self, account, pwd):
        self.input_account_pwd(account, pwd)
        self.find_element_id(self._tv_next).click()
        return ConnectGuidePage(self.driver)
