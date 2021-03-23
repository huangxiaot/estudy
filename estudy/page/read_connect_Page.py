# 设备管理--网络配置--准备连接页面
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.fill_wifi_infomation_page import FillWifiInformationPage


class ReadyConnectPage(BasePage):
    # 确认，开始连接按钮
    _tv_connect = (By.ID, "com.intretech.readerx:id/tv_device_net_prepare_sure")

    """进入填写WiFi信息页面"""
    def enter_fill_wifi_information(self):
        self.find_element_id(self._tv_connect).click()
        return FillWifiInformationPage(self.driver)
