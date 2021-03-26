# 编辑宝贝信息页面
import time
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.my_family_page import MyFamilyPage
from utils.slide import Slide


class EditorBabyInfoPage(BasePage):
    driver: webdriver = None

    def __init__(self, driver):
        super().__init__(driver)
        self.slide = Slide(driver)
        self.my_family_page = MyFamilyPage(driver)

    """以下元素为修改头像对应的元素"""
    # 宝贝头像
    _iv_baby_avatar_display = (By.ID, "com.intretech.readerx:id/img_baby_detail_avatar")
    # 拍照&相册按钮
    _rl_editor_baby_portrait = "android.widget.RelativeLayout"
    # 系统拍照页面的拍照按钮
    _iv_editor_baby_avatar_take_photo = (By.ID, "com.android.camera:id/shutter_button")
    # 系统拍照后确认按钮
    _btn_editor_baby_avatar_confirm_photo = (By.ID, "com.android.camera:id/done_button")
    # 系统拍照后重拍按钮
    _iv_editor_baby_avatar_rephotograph = (By.ID, "com.android.camera:id/retake_button")
    # 系统拍照后取消按钮
    _btn_editor_baby_avatar_cancel_photo = (By.ID, "com.android.camera:id/cancel_button")
    # 系统拍照-确认-裁剪页面"✔"
    _tv_editor_baby_avatar_tailor_confirm = (By.ID, "com.intretech.readerx:id/menu_crop")
    # 系统相册中照片列表
    _iv_editor_baby_avatar_system_photo_album = "android.widget.ImageView"

    """以下元素为修改宝贝昵称对应的元素"""
    # 宝贝信息页面显示的宝贝昵称
    _tv_baby_name_display = (By.ID, "com.intretech.readerx:id/tv_baby_detail_nickname")
    # 修改宝贝昵称页面的宝贝昵称输入框
    _et_editor_baby_name = (By.ID, "com.intretech.readerx:id/edit_modify")
    # 修改宝贝昵称页面的宝贝昵称输入框右侧的“x”
    _iv_clear_editor_baby_name = (By.ID, "com.intretech.readerx:id/img_modify_clear")
    # 修改宝贝昵称页面右上角的“✔”
    _iv_editor_baby_name_confirm = (By.ID, "com.intretech.readerx:id/btn_toolbar_more")
    # 修改宝贝昵称页面左上角的返回键
    _iv_editor_baby_name_back = (By.ID, "com.intretech.readerx:id/btn_toolbar_back")

    """以下元素为修改性别对应的元素"""
    # 性别男头像
    _iv_editor_baby_sex_boy = (By.ID, "com.intretech.readerx:id/img_baby_detail_boy")
    # 性别女头像
    _iv_editor_baby_sex_girl = (By.ID, "com.intretech.readerx:id/img_baby_detail_girl")

    """以下元素为修改宝贝生日对应的元素"""
    # 宝贝生日显示
    _rl_baby_birth_display = (By.ID, "com.intretech.readerx:id/layout_baby_detail_birthday")
    # 修改宝贝生日页面左上角修改年份按钮
    _tv_editor_baby_birth_year = (By.ID, "android:id/date_picker_header_year")
    # 修改宝贝生日页面年份定位
    _tv_editor_baby_birth_years = "android.widget.TextView"
    # 修改宝贝生日页面修改月份-上个月
    _ib_editor_baby_name_month_previous = (By.ID, "android:id/prev")
    # 修改宝贝生日页面修改月份-下个月
    _ib_editor_baby_name_month_next = (By.ID, "android:id/next")
    # 修改宝贝生日页面修改日期
    _vv_editor_baby_birth_day = "android.view.View"
    # 修改宝贝生日页面取消按钮
    _btn_editor_baby_birth_cancel = (By.ID, "android:id/button2")
    # 修改宝贝生日页面确定按钮
    _btn_editor_baby_birth_confirm = (By.ID, "android:id/button1")

    """以下元素为修改与宝贝的关系相对应的元素"""
    # 与宝贝的关系显示
    _rl_baby_relation_display = (By.ID, "com.intretech.readerx:id/layout_baby_detail_relation")
    # 修改与宝贝关系的确认按钮
    _tv_editor_baby_relation_confirm = (By.ID, "com.intretech.readerx:id/tv_bottom_relation_sure")
    # 修改与宝贝关系的取消按钮
    _tv_editor_baby_relation_cancel = (By.ID, "com.intretech.readerx:id/tv_bottom_relation_cancel")
    # 修改与宝贝关系
    _fl_editor_baby_relation = (By.ID, "com.intretech.readerx:id/design_bottom_sheet")

    """拍照方式修改宝贝头像，并修改成功"""
    def editor_baby_portrait_photograph_success(self):
        # 点击宝贝头像
        self.find_element_id(self._iv_baby_avatar_display).click()
        """ 
        1.判断有没有拍照&相册按钮
        2.存在点击相册按钮，不存在输出”没有找到拍照按钮“
        """
        try:
            portrait = self.find_element_classname(self._rl_editor_baby_portrait)
        except NoSuchElementException:
            print("没有找到拍照按钮")
        else:
            portrait[0].click()
        # 拍照页面点击拍照-确定-裁剪“✔”
        self.find_element_id(self._iv_editor_baby_avatar_take_photo).click()
        self.find_element_id(self._btn_editor_baby_avatar_confirm_photo).click()
        self.find_element_id(self._tv_editor_baby_avatar_tailor_confirm).click()
        time.sleep(1)

    """相册方式修改宝贝头像，并修改成功"""
    def editor_baby_portrait_photo_album_success(self):
        # 点击宝贝头像
        self.find_element_id(self._iv_baby_avatar_display).click()
        """ 
        1.判断有没有拍照&相册按钮
        2.存在点击相册按钮，不存在输出”没有找到拍照按钮“
        """
        try:
            portrait = self.find_element_classname(self._rl_editor_baby_portrait)
        except NoSuchElementException:
            print("没有找到拍照按钮")
        else:
            portrait[1].click()
        """ 
        1.判断系统相册中有没有照片
        2.有照片则点击第二张，没有照片则输出”没有找到照片“
        """
        try:
            photos = self.find_element_classname(self._iv_editor_baby_avatar_system_photo_album)
        except NoSuchElementException:
            print("没有找到照片")
        else:
            photos[1].click()
        # 系统相册选择照片后裁剪页面点击”✔“
        self.find_element_id(self._tv_editor_baby_avatar_tailor_confirm).click()
        time.sleep(1)

    """修改宝贝昵称，并修改成功"""
    def editor_baby_name_success(self, editor_baby_name):
        # 点击宝贝昵称，进入修改宝贝昵称页面-修改宝贝昵称-点击“✔”
        self.find_element_id(self._tv_baby_name_display).click()
        self.find_element_id(self._tv_baby_name_display).clear()
        self.find_element_id(self._et_editor_baby_name).send_keys(editor_baby_name)
        self.find_element_id(self._iv_editor_baby_name_confirm).click()
        time.sleep(1)
        return editor_baby_name

    """判断修改后的宝贝昵称是否正确"""
    def judge_baby_name_validity(self, editor_baby_name):
        my_family_page_baby_name_display = self.my_family_page.split_baby_name_display()
        baby_info_page_baby_name_display = self.find_element_id(self._tv_baby_name_display).text
        editor_baby_name = self.editor_baby_name_success(editor_baby_name)
        if (my_family_page_baby_name_display == baby_info_page_baby_name_display) & (editor_baby_name == baby_info_page_baby_name_display):
            print("宝贝昵称修改成功")
        else:
            print("宝贝昵称修改失败")

    """修改宝贝性别，并修改成功"""
    def editor_baby_sex_success(self):
        # 循环点击男、女生头像
        for i in range(1, 10):
            self.find_element_id(self._iv_editor_baby_sex_boy).click()
            self.find_element_id(self._iv_editor_baby_sex_girl).click()
            i = i + 1

    """修改宝贝生日，并修改成功"""
    def editor_baby_birth_success(self):
        # 点击宝贝生日，进入编辑宝贝生日页面
        self.find_element_id(self._rl_baby_birth_display).click()
        # 点击修改年份
        self.find_element_id(self._tv_editor_baby_birth_year).click()
        is_find = False
        is_sequential_search = True
        while is_find is not True:
            try:
                self.driver.find_element_by_xpath("//android.widget.TextView[@text='1995']").click()
                is_find = True
            except NoSuchElementException:
                if is_sequential_search:
                    self.slide.swipe_up(2500)
                    # 所有年份，获取屏幕列表中最底部的一个年份的text值
                    years = self.find_element_classname(self._tv_editor_baby_birth_years)
                    years_text = years[9].text
                    print(years_text)
                    if years_text == "2021":
                        is_sequential_search = False
                else:
                    self.slide.swipe_down_search(2500)
        # 修改月份，点击上一个月
        self.find_element_id(self._ib_editor_baby_name_month_previous).click()
        time.sleep(0.5)
        """
        1.判断是否存在18号
        2.存在点击，不存在则输出“没有找到该日期“
        """
        try:
            days = self.find_element_classname(self._vv_editor_baby_birth_day)
        except NoSuchElementException:
            print("没有找到该日期")
        else:
            days[17].click()
        # 日期修改完成后点击确认
        self.find_element_id(self._btn_editor_baby_birth_confirm).click()
        time.sleep(1)

    """修改与宝贝的关系，并修改成功"""
    def editor_baby_relation_success(self):
        # 点击与宝贝关系，底部弹框显示宝贝关系--滑动选择与宝贝关系--确认
        self.find_element_id(self._rl_baby_relation_display).click()
        self.slide.swipe_up(500)
        self.find_element_id(self._tv_editor_baby_relation_confirm).click()
        time.sleep(1)
