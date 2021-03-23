# 编辑宝贝信息页面
import time
from selenium.webdriver.common.by import By
from page.base_page import BasePage


class EditorBabyInfoPage(BasePage):
    # 宝贝头像
    _iv_baby_avatar = (By.ID, "com.intretech.readerx:id/img_baby_detail_avatar")
    # 拍照&相册按钮
    _rl_portrait = "android.widget.RelativeLayout"
    # 系统拍照页面的拍照按钮
    _iv_take_photo = (By.ID, "com.android.camera:id/shutter_button")
    # 系统拍照后确认按钮
    _btn_confirm_photo = (By.ID, "com.android.camera:id/done_button")
    # 系统拍照后重拍按钮
    _iv_rephotograph = (By.ID, "com.android.camera:id/retake_button")
    # 系统拍照后取消按钮
    _btn_cancel_photo = (By.ID, "com.android.camera:id/cancel_button")
    # 系统拍照-确认-裁剪页面"✔"
    _tv_tailor_confirm = (By.ID, "com.intretech.readerx:id/menu_crop")
    # 系统相册中照片列表
    _iv_system_photo_album = "android.widget.ImageView"
    # 性别男头像
    _iv_sex_boy = (By.ID, "com.intretech.readerx:id/img_baby_detail_boy")
    # 性别女头像
    _iv_sex_girl = (By.ID, "com.intretech.readerx:id/img_baby_detail_girl")

    """拍照方式修改宝贝头像，并修改成功"""
    def editor_baby_portrait_photograph(self):
        # 点击宝贝头像
        self.find_element_id(self._iv_baby_avatar).click()
        """ 
        1.判断有没有拍照&相册按钮
        2.存在点击相册按钮，不存在输出”没有找到拍照按钮“
        """
        try:
            portrait = self.find_element_classname(self._rl_portrait)
        except:
            print("没有找到拍照按钮")
        else:
            portrait[0].click()
        # 拍照页面点击拍照-确定-裁剪“✔”
        self.find_element_id(self._iv_take_photo).click()
        self.find_element_id(self._btn_confirm_photo).click()
        self.find_element_id(self._tv_tailor_confirm).click()
        time.sleep(1)

    """相册方式修改宝贝头像，并修改成功"""
    def editor_baby_portrait_photo_album(self):
        # 点击宝贝头像
        self.find_element_id(self._iv_baby_avatar).click()
        """ 
        1.判断有没有拍照&相册按钮
        2.存在点击相册按钮，不存在输出”没有找到拍照按钮“
        """
        try:
            portrait = self.find_element_classname(self._rl_portrait)
        except:
            print("没有找到拍照按钮")
        else:
            portrait[1].click()
        """ 
        1.判断系统相册中有没有照片
        2.有照片则点击第二张，没有照片则输出”没有找到照片“
        """
        try:
            photos = self.find_element_classname(self._iv_system_photo_album)
        except:
            print("没有找到照片")
        else:
            photos[1].click()
        # 系统相册选择照片后裁剪页面点击”✔“
        self.find_element_id(self._tv_tailor_confirm).click()
        time.sleep(1)

    """修改宝贝昵称"""
    def editor_baby_name(self):
        pass

    """修改宝贝性别"""
    def editor_baby_sex(self):
        # 循环点击男、女生头像
        for i in range(1, 10):
            self.find_element_id(self._iv_sex_boy).click()
            self.find_element_id(self._iv_sex_girl).click()
            i = i + 1
