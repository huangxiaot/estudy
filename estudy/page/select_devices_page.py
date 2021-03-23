# 选择设备类型页面
from selenium.webdriver.common.by import By
from page.add_reading_lamp import AddReadingLampPage
from page.base_page import BasePage


class SelectDevicesPage(BasePage):
    # 伴读台灯配网入口卡片
    _iv_reading_lamp = (By.ID, "com.intretech.readerx:id/img_product_reader")

    """进入添加伴读台灯页面"""
    def enter_add_reading_lamp(self):
        self.find_element_id(self._iv_reading_lamp).click()
        return AddReadingLampPage(self.driver)
