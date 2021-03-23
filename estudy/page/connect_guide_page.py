# 设备管理--网络配置--连接引导页面
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.devices_scan_qr_code_page import DevicesScanQRCode


class ConnectGuidePage(BasePage):
    # 开始扫码按钮
    _tv_start_scan = (By.ID, "com.intretech.readerx:id/tv_wifi_info_send_guide_sure")

    """开始扫码，进入配网二维码页面"""
    def enter_devices_scan_qr_code(self):
        self.find_element_id(self._tv_start_scan).click()
        return DevicesScanQRCode(self.driver)
