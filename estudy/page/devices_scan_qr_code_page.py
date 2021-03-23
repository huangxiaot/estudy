# 设备管理--网络配置--设备扫描配网二维码页面
from selenium.webdriver.common.by import By
from page.base_page import BasePage


class DevicesScanQRCode(BasePage):
    # 设备重命名输入框
    _et_device_name = (By.ID, "com.intretech.readerx:id/edit_dialog_machine_name_input")

    """设备重命名输入框设置"""
    def input_device_name(self):
        self.find_element_id(self._et_device_name).clear()
        self.find_element_id(self._et_device_name).send_keys("蜗牛")
