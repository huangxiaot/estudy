# 编辑宝贝信息页面
import time
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from utils.slide import Slide


class EditorBabyInfoPage(BasePage):
    driver: webdriver = None

    def __init__(self, driver):
        super().__init__(driver)
        self.slide = Slide(driver)

    """我的页面显示的宝贝信息，包括头像、昵称、性别、年龄"""
    # 宝贝昵称、性别、年龄显示
    _tv_show_baby_info = (By.ID, "com.intretech.readerx:id/tv_person_name")

    """宝贝信息页面的返回键"""
    _iv_baby_information_display_back = (By.ID, "com.intretech.readerx:id/btn_toolbar_back")

    """以下元素为修改头像对应的元素"""
    # 宝贝头像
    _iv_baby_avatar_display = (By.ID, "com.intretech.readerx:id/img_baby_detail_avatar")
    # 拍照&相册按钮
    _rl_editor_baby_portrait = "android.widget.RelativeLayout"
    # 拍照&相册弹框底部取消按钮
    _tv_editor_baby_portrait_cancel = (By.ID, "com.intretech.readerx:id/tv_bottom_menu_cancel")
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

    """取消修改宝贝头像"""
    def editor_baby_portrait_cancel(self):
        # 点击宝贝头像，弹出弹框后点击取消
        self.find_element_id(self._iv_baby_avatar_display).click()
        self.find_element_id(self._tv_editor_baby_portrait_cancel).click()
        time.sleep(1)
        print("取消修改宝贝头像")

    """拍照方式修改宝贝头像，进入拍照页面"""
    def editor_baby_portrait_photograph(self):
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

    """1.拍照方式修改宝贝头像，拍照并修改成功"""
    def editor_baby_portrait_photograph_success(self):
        self.editor_baby_portrait_photograph()
        # 系统拍照页面点击拍照-确定-裁剪“✔”
        self.find_element_id(self._iv_editor_baby_avatar_take_photo).click()
        self.find_element_id(self._btn_editor_baby_avatar_confirm_photo).click()
        self.find_element_id(self._tv_editor_baby_avatar_tailor_confirm).click()
        time.sleep(1)
        print("拍照方式宝贝头像修改成功")

    """2.拍照方式修改宝贝头像，未拍照，在系统拍照页面取消拍照"""
    def editor_baby_portrait_photograph_cancel(self):
        self.editor_baby_portrait_photograph()
        # 系统拍照页面点击左下角取消
        self.find_element_id(self._btn_editor_baby_avatar_cancel_photo).click()
        time.sleep(1)
        self.find_element_id(self._tv_editor_baby_portrait_cancel).click()
        print("拍照方式取消拍照成功")

    """3.拍照方式修改宝贝头像，已拍照，在拍的照片页面取消拍照"""
    def editor_baby_portrait_photograph_cancel_photo(self):
        self.editor_baby_portrait_photograph()
        # 系统拍照页面点击拍照
        self.find_element_id(self._iv_editor_baby_avatar_take_photo).click()
        # 拍照后取消拍照
        self.find_element_id(self._btn_editor_baby_avatar_cancel_photo).click()
        time.sleep(1)
        self.find_element_id(self._tv_editor_baby_portrait_cancel).click()
        print("拍照方式已拍照，取消拍照成功")

    """4.拍照方式修改宝贝头像，已拍照，在裁剪页面点击“x”"""
    def editor_baby_portrait_photograph_cancel_tailor(self):
        self.editor_baby_portrait_photograph()
        # 系统拍照页面点击拍照-确定-裁剪“x”
        self.find_element_id(self._iv_editor_baby_avatar_take_photo).click()
        self.find_element_id(self._btn_editor_baby_avatar_confirm_photo).click()
        # 系统拍照页面直接点击手机系统的返回键
        self.driver.press_keycode(4)
        time.sleep(1)
        print("拍照方式取消裁剪成功")

    """相册方式修改宝贝头像"""
    def editor_baby_portrait_photo_album(self):
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

    """1.相册方式修改宝贝头像，修改成功"""
    def editor_baby_portrait_photo_album_success(self):
        self.editor_baby_portrait_photo_album()
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
        print("相册方式修改宝贝头像成功")

    """2.相册方式修改宝贝头像，相册页面取消"""
    def editor_baby_portrait_photo_album_cancel(self):
        self.editor_baby_portrait_photo_album()
        # 系统相册页面直接点击手机系统的返回键
        self.driver.press_keycode(4)
        time.sleep(1)
        self.find_element_id(self._tv_editor_baby_portrait_cancel).click()
        print("相册方式，在系统相册页面取消修改宝贝头像成功")

    """3.相册方式修改宝贝头像，裁剪页面取消"""
    def editor_baby_portrait_photo_album_cancel_tailor(self):
        self.editor_baby_portrait_photo_album()
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
        # 系统相册选择照片后裁剪页面点击”x“
        self.driver.press_keycode(4)
        time.sleep(1)
        print("相册方式，选择相册后在裁剪页面取消修改宝贝头像成功")

    """修改宝贝昵称页面-输入宝贝昵称"""
    def input_baby_name(self, editor_baby_name):
        self.find_element_id(self._tv_baby_name_display).click()
        self.find_element_id(self._et_editor_baby_name).clear()
        self.find_element_id(self._et_editor_baby_name).send_keys(editor_baby_name)

    """1.修改宝贝昵称，并修改成功"""
    def editor_baby_name_success(self, editor_baby_name):
        # 修改宝贝昵称页面-修改宝贝昵称-点击“✔”
        self.input_baby_name(editor_baby_name)
        self.find_element_id(self._iv_editor_baby_name_confirm).click()
        time.sleep(1)

    """宝贝信息页面显示的宝贝昵称"""
    def baby_information_baby_name_display(self):
        # 获取宝贝信息页面的宝贝昵称
        baby_name_display = self.find_element_id(self._tv_baby_name_display).text
        return baby_name_display

    """将我的页面中宝贝昵称分割为独立字符串"""
    def split_baby_name_display(self):
        # 返回我的页面
        self.find_element_id(self._iv_baby_information_display_back).click()
        # 获取页面显示的宝贝昵称、性别、年龄
        my_page_baby_infos_display = self.find_element_id(self._tv_show_baby_info).text
        # 先将字符串按照”/“分割一个列表，列表中存放两个字符串，一个为昵称，另一个为性别和年龄
        my_page_baby_infos = my_page_baby_infos_display.split("/")
        print(my_page_baby_infos)
        # 获取宝贝昵称
        my_page_baby_name_display = my_page_baby_infos[0]
        print(my_page_baby_name_display)
        return my_page_baby_name_display

    """1.修改宝贝性别女，并修改成功"""
    def editor_baby_sex_girl_success(self):
        # 循环点击男、女生头像
        for i in range(1, 10):
            self.find_element_id(self._iv_editor_baby_sex_boy).click()
            self.find_element_id(self._iv_editor_baby_sex_girl).click()
            i = i + 1

    """2.修改宝贝性别男，并修改成功"""
    def editor_baby_sex_boy_success(self):
        # 循环点击男、女生头像
        for i in range(1, 10):
            self.find_element_id(self._iv_editor_baby_sex_girl).click()
            self.find_element_id(self._iv_editor_baby_sex_boy).click()
            i = i + 1

    """将我的页面中宝贝性别分割为独立字符串"""
    def split_baby_sex_display(self):
        # 返回我的页面
        self.find_element_id(self._iv_baby_information_display_back).click()
        # 获取页面显示的宝贝昵称、性别、年龄
        my_page_baby_infos_display = self.find_element_id(self._tv_show_baby_info).text
        # 先将字符串按照”/“分割一个列表，列表中存放两个字符串，一个为昵称，另一个为性别和年龄
        my_page_baby_infos = my_page_baby_infos_display.split("/")
        print(my_page_baby_infos)
        # 将存放宝贝性别和年龄的列表按照空格切割一次，切割后的列表中存放两个字符串，一个为性别，一个为年龄
        my_page_baby_sex_and_age = my_page_baby_infos[1].split(" ", 1)
        print(my_page_baby_sex_and_age)
        # 读取列表中宝贝性别
        my_page_baby_sex_display = my_page_baby_sex_and_age[0]
        print(my_page_baby_sex_display)
        return my_page_baby_sex_display

    """修改宝贝生日，并修改成功"""
    def editor_baby_birth_success(self):
        # 点击宝贝生日，进入编辑宝贝生日页面
        self.find_element_id(self._rl_baby_birth_display).click()
        # 点击修改年份
        self.find_element_id(self._tv_editor_baby_birth_year).click()
        is_find = False     # 默认没找到元素
        is_sequential_search = True      # 默认顺序查找，即上滑
        while is_find is not True:
            try:
                self.driver.find_element_by_xpath("//android.widget.TextView[@text='1995']").click()
                is_find = True      # 找到了，退出循环
            except NoSuchElementException:
                if is_sequential_search:      # 顺序查找
                    self.slide.swipe_up(2500)
                    # 所有年份，获取屏幕列表中最底部的一个年份的text值
                    years = self.find_element_classname(self._tv_editor_baby_birth_years)
                    years_text = years[9].text
                    print(years_text)
                    if years_text == "2021":      # 到列表的最后一个，但没找到
                        is_sequential_search = False      # 转换为逆序查找，即下滑
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

    """将我的页面中宝贝年龄分割为独立字符串"""
    def split_my_page_baby_age_display(self):
        # 返回我的页面
        self.find_element_id(self._iv_baby_information_display_back).click()
        # 获取页面显示的宝贝昵称、性别、年龄
        my_page_baby_infos_display = self.find_element_id(self._tv_show_baby_info).text
        # 先将字符串按照”/“分割一个列表，列表中存放两个字符串，一个为昵称，另一个为性别和年龄
        my_page_baby_infos = my_page_baby_infos_display.split("/")
        print(my_page_baby_infos)
        # 将存放宝贝性别和年龄的列表按照空格切割一次，切割后的列表中存放两个字符串，一个为性别，一个为年龄
        my_page_baby_sex_and_age = my_page_baby_infos[1].split(" ", 1)
        print(my_page_baby_sex_and_age)
        # 读取列表中宝贝性别
        my_page_baby_age_display = my_page_baby_sex_and_age[1]
        print(my_page_baby_age_display)
        return my_page_baby_age_display
