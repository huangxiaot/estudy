# 设备管理--网络配置--添加伴读台灯（扫描设备二维码）页面
import time
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.read_connect_Page import ReadyConnectPage


class AddReadingLampPage(BasePage):
    # 相册按钮
    _tv_photo_album = (By.ID, "com.intretech.readerx:id/btn_toolbar_more")
    # 相册图片
    _fl_photos = "android.widget.FrameLayout"
    # 剪裁页面的“✔”按钮
    _btn_tick = (By.ID, "com.intretech.readerx:id/menu_crop")

    """获取相册中的图片进行扫描"""
    def select_photo_album(self):
        # 进入手机系统相册页面
        self.find_element_id(self._tv_photo_album).click()
        time.sleep(0.5)
        try:
            # 查找相册的第一张图片
            photos = self.find_element_classname(self._fl_photos)
        except:
            print("没有找到图片")
        else:
            # 查找到图片后点击第一张图片
            photos[0].click()
        # 裁剪页面点击“✔”
        self.find_element_id(self._btn_tick).click()
        return ReadyConnectPage(self.driver)

