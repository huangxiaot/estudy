# 编辑宝贝信息页面
import time
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from utils.slide import Slide
from utils.toast import Toast


class EditorBabyInfoPage(BasePage):
    driver: webdriver = None

    def __init__(self, driver):
        super().__init__(driver)
        self.slide = Slide(driver)
        self.toast = Toast(driver)

    """我的页面显示的宝贝信息，包括头像、昵称、性别、年龄"""
    # 宝贝昵称、性别、年龄显示
    _tv_show_baby_info = (By.ID, "com.intretech.readerx:id/tv_person_name")
    # 宝贝信息页面入口
    _iv_baby_info = (By.ID, "com.intretech.readerx:id/img_person_portrait")
    # 当前用户与宝贝的关系
    _tv_baby_relation = (By.ID, "com.intretech.readerx:id/tv_family_user_title")

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
    # 裁剪页面左上角“x"
    _btn_editor_baby_avatar_tailor_cancel = "android.widget.ImageButton"
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
    # 修改后未保存返回弹框取消按钮
    _tv_editor_baby_name_back_bounced_cancel = (By.ID, "com.intretech.readerx:id/view_dialog_cancel")
    # 修改后未保存返回弹框确认按钮
    _tv_editor_baby_name_back_bounced_confirm = (By.ID, "com.intretech.readerx:id/view_dialog_confirm")

    """以下元素为修改性别对应的元素"""
    # 性别男头像
    _iv_editor_baby_sex_boy = (By.ID, "com.intretech.readerx:id/img_baby_detail_boy")
    # 性别女头像
    _iv_editor_baby_sex_girl = (By.ID, "com.intretech.readerx:id/img_baby_detail_girl")

    """以下元素为修改宝贝生日对应的元素"""
    # 宝贝生日点击区域
    _rl_baby_birth_display = (By.ID, "com.intretech.readerx:id/layout_baby_detail_birthday")
    # 宝贝生日显示内容
    _tv_baby_birth_detail_display = (By.ID, "com.intretech.readerx:id/tv_baby_detail_birthday")
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

    """1.取消修改宝贝头像"""
    def editor_baby_portrait_cancel(self):
        # 点击宝贝头像，弹出弹框后点击取消
        self.find_element_id(self._iv_baby_avatar_display).click()
        self.find_element_id(self._tv_editor_baby_portrait_cancel).click()
        time.sleep(1)

    """拍照方式修改宝贝头像，进入拍照页面"""
    def editor_baby_portrait_photograph(self):
        # 点击宝贝头像
        self.find_element_id(self._iv_baby_avatar_display).click()
        time.sleep(0.5)
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

    """取消裁剪"""
    def editor_baby_portrait_cancel_tailor(self):
        try:
            _btn_cancel_tailor = self.find_element_classname(self._btn_editor_baby_avatar_tailor_cancel)
        except NoSuchElementException:
            print("没有找到取消裁剪按钮")
        else:
            _btn_cancel_tailor[0].click()

    """2.拍照方式修改宝贝头像，拍照并修改成功"""
    def editor_baby_portrait_photograph_success(self):
        self.editor_baby_portrait_photograph()
        # 系统拍照页面点击拍照-确定-裁剪“✔”
        self.find_element_id(self._iv_editor_baby_avatar_take_photo).click()
        self.find_element_id(self._btn_editor_baby_avatar_confirm_photo).click()
        self.find_element_id(self._tv_editor_baby_avatar_tailor_confirm).click()
        time.sleep(1)

    """3.拍照方式修改宝贝头像，未拍照，在系统拍照页面取消拍照"""
    def editor_baby_portrait_photograph_cancel(self):
        self.editor_baby_portrait_photograph()
        # 系统拍照页面点击左下角取消
        self.find_element_id(self._btn_editor_baby_avatar_cancel_photo).click()
        time.sleep(0.5)
        self.find_element_id(self._tv_editor_baby_portrait_cancel).click()
        time.sleep(0.5)

    """4.拍照方式修改宝贝头像，已拍照，在拍的照片页面取消拍照"""
    def editor_baby_portrait_photograph_cancel_photo(self):
        self.editor_baby_portrait_photograph()
        # 系统拍照页面点击拍照
        self.find_element_id(self._iv_editor_baby_avatar_take_photo).click()
        # 拍照后取消拍照
        self.find_element_id(self._btn_editor_baby_avatar_cancel_photo).click()
        time.sleep(1)
        self.find_element_id(self._tv_editor_baby_portrait_cancel).click()
        time.sleep(0.5)

    """5.拍照方式修改宝贝头像，已拍照，在裁剪页面点击“x”"""
    def editor_baby_portrait_photograph_cancel_tailor(self):
        self.editor_baby_portrait_photograph()
        # 系统拍照页面点击拍照-确定-裁剪“x”
        self.find_element_id(self._iv_editor_baby_avatar_take_photo).click()
        self.find_element_id(self._btn_editor_baby_avatar_confirm_photo).click()
        time.sleep(0.5)
        # 系统拍照页面已拍照裁剪页面点击“x”
        self.editor_baby_portrait_cancel_tailor()
        time.sleep(1)

    """相册方式修改宝贝头像"""
    def editor_baby_portrait_photo_album(self):
        # 点击宝贝头像
        self.find_element_id(self._iv_baby_avatar_display).click()
        time.sleep(0.5)
        """ 
        1.判断有没有拍照&相册按钮
        2.存在点击相册按钮，不存在输出”没有找到拍照按钮“
        """
        try:
            portrait = self.find_element_classname(self._rl_editor_baby_portrait)
        except NoSuchElementException:
            print("没有找到相册按钮")
        else:
            portrait[1].click()

    """6.相册方式修改宝贝头像，修改成功"""
    def editor_baby_portrait_photo_album_success(self):
        self.editor_baby_portrait_photo_album()
        time.sleep(0.5)
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
        time.sleep(0.5)
        # 系统相册选择照片后裁剪页面点击”✔“
        self.find_element_id(self._tv_editor_baby_avatar_tailor_confirm).click()
        time.sleep(1)

    """7.相册方式修改宝贝头像，相册页面取消"""
    def editor_baby_portrait_photo_album_cancel(self):
        self.editor_baby_portrait_photo_album()
        time.sleep(0.5)
        # 系统相册页面直接点击返回键
        self.editor_baby_portrait_cancel_tailor()
        time.sleep(0.5)
        self.find_element_id(self._tv_editor_baby_portrait_cancel).click()
        time.sleep(0.5)

    """8.相册方式修改宝贝头像，裁剪页面取消"""
    def editor_baby_portrait_photo_album_cancel_tailor(self):
        self.editor_baby_portrait_photo_album()
        time.sleep(0.5)
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
        time.sleep(0.5)
        self.editor_baby_portrait_cancel_tailor()
        # 返回我的页面
        self.find_element_id(self._iv_baby_information_display_back).click()
        time.sleep(0.5)

    """修改宝贝昵称页面-输入宝贝昵称"""
    def input_baby_name(self, editor_baby_name):
        # 进入宝贝信息页面
        self.find_element_id(self._iv_baby_info).click()
        # 进入修改宝贝昵称页面
        self.find_element_id(self._tv_baby_name_display).click()
        # 清空昵称-修改昵称
        self.find_element_id(self._et_editor_baby_name).clear()
        self.find_element_id(self._et_editor_baby_name).send_keys(editor_baby_name)

    """修改宝贝昵称"""
    def modify_baby_name(self, editor_baby_name):
        # 清空昵称-修改昵称
        self.find_element_id(self._et_editor_baby_name).clear()
        self.find_element_id(self._et_editor_baby_name).send_keys(editor_baby_name)
        self.find_element_id(self._iv_editor_baby_name_confirm).click()

    """1.修改宝贝昵称，并修改成功"""
    def editor_baby_name_success(self, editor_baby_name):
        # 修改宝贝昵称页面-修改宝贝昵称-点击“✔”
        self.input_baby_name(editor_baby_name)
        self.find_element_id(self._iv_editor_baby_name_confirm).click()
        time.sleep(1)

    """2.未修改宝贝昵称，点击返回"""
    def editor_baby_name_back(self):
        # 进入宝贝信息页面
        self.find_element_id(self._iv_baby_info).click()
        # 进入修改宝贝昵称页面
        self.find_element_id(self._tv_baby_name_display).click()
        # 未修改宝贝昵称，点击返回
        self.find_element_id(self._iv_editor_baby_name_back).click()

    """3.未修改宝贝昵称，点击确定"""
    def editor_baby_name_confirm(self):
        # 进入宝贝信息页面
        self.find_element_id(self._iv_baby_info).click()
        # 进入修改宝贝昵称页面
        self.find_element_id(self._tv_baby_name_display).click()
        # 未修改宝贝昵称，点击确定
        self.find_element_id(self._iv_editor_baby_name_confirm).click()

    """4.已修改宝贝昵称，点击返回-取消"""
    def editor_baby_name_back_cancel(self, editor_baby_name):
        self.input_baby_name(editor_baby_name)
        # 已修改宝贝昵称，点击返回 - 取消
        self.find_element_id(self._iv_editor_baby_name_back).click()
        self.find_element_id(self._tv_editor_baby_name_back_bounced_cancel).click()
        # 输入昵称
        self.find_element_id(self._et_editor_baby_name).clear()
        self.find_element_id(self._et_editor_baby_name).send_keys(editor_baby_name)
        self.find_element_id(self._iv_editor_baby_name_confirm).click()

    """5.已修改宝贝昵称，点击返回-确定"""
    def editor_baby_name_back_confirm(self, editor_baby_name):
        # 已修改宝贝昵称，点击返回-确定
        self.input_baby_name(editor_baby_name)
        self.find_element_id(self._iv_editor_baby_name_back).click()
        self.find_element_id(self._tv_editor_baby_name_back_bounced_confirm).click()

    """6.修改宝贝昵称为空"""
    def editor_baby_name_null(self):
        # 进入宝贝信息页面
        self.find_element_id(self._iv_baby_info).click()
        # 进入修改宝贝昵称页面
        self.find_element_id(self._tv_baby_name_display).click()
        # 点击昵称输入框右侧的“x”按钮
        self.find_element_id(self._iv_clear_editor_baby_name).click()
        time.sleep(0.5)
        self.find_element_id(self._iv_editor_baby_name_confirm).click()

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
        # 获取宝贝昵称
        my_page_baby_name_display = my_page_baby_infos[0]
        return my_page_baby_name_display

    """1.修改宝贝性别女，并修改成功"""
    def editor_baby_sex_girl_success(self):
        # 进入宝贝信息页面
        self.find_element_id(self._iv_baby_info).click()
        # 循环点击男、女生头像
        for i in range(1, 10):
            self.find_element_id(self._iv_editor_baby_sex_boy).click()
            self.find_element_id(self._iv_editor_baby_sex_girl).click()
            i = i + 1
        # 返回我的页面
        self.find_element_id(self._iv_baby_information_display_back).click()

    """2.修改宝贝性别男，并修改成功"""
    def editor_baby_sex_boy_success(self):
        # 进入宝贝信息页面
        self.find_element_id(self._iv_baby_info).click()
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
        # 将存放宝贝性别和年龄的列表按照空格切割一次，切割后的列表中存放两个字符串，一个为性别，一个为年龄
        my_page_baby_sex_and_age = my_page_baby_infos[1].split(" ", 1)
        # 读取列表中宝贝性别
        my_page_baby_sex_display = my_page_baby_sex_and_age[0]
        return my_page_baby_sex_display

    """修改宝贝生日年份"""
    def editor_baby_birth_year_success(self):
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

    """修改宝贝生日月份"""
    def editor_baby_birth_month_success(self):
        # 点击宝贝生日，进入编辑宝贝生日页面
        self.find_element_id(self._rl_baby_birth_display).click()
        # 修改月份，点击上一个月
        self.find_element_id(self._ib_editor_baby_name_month_previous).click()
        time.sleep(0.5)

    """修改宝贝生日日期"""
    def editor_baby_birth_day_success(self):
        # 点击宝贝生日，进入编辑宝贝生日页面
        self.find_element_id(self._rl_baby_birth_display).click()
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
        time.sleep(1)

    """1.不修改宝贝生日，点击取消按钮"""
    def editor_baby_birth_cancel(self):
        # 进入宝贝信息页面
        self.find_element_id(self._iv_baby_info).click()
        # 点击宝贝生日，进入编辑宝贝生日页面
        self.find_element_id(self._rl_baby_birth_display).click()
        # 不修改宝贝生日，点击取消按钮
        self.find_element_id(self._btn_editor_baby_birth_cancel).click()
        time.sleep(0.5)

    """2.不修改宝贝生日，点击确定按钮"""
    def editor_baby_birth_confirm(self):
        # 进入宝贝信息页面
        self.find_element_id(self._iv_baby_info).click()
        # 点击宝贝生日，进入编辑宝贝生日页面
        self.find_element_id(self._rl_baby_birth_display).click()
        # 不修改宝贝生日，点击确定按钮
        self.find_element_id(self._btn_editor_baby_birth_confirm).click()

    """3.点击宝贝生日年份，不修改，点击取消"""
    def editor_baby_birth_year_cancel(self):
        # 进入宝贝信息页面
        self.find_element_id(self._iv_baby_info).click()
        # 点击宝贝生日，进入编辑宝贝生日页面
        self.find_element_id(self._rl_baby_birth_display).click()
        # 点击修改年份
        self.find_element_id(self._tv_editor_baby_birth_year).click()
        # 不修改年份，点击取消按钮
        self.find_element_id(self._btn_editor_baby_birth_cancel).click()

    """4.点击宝贝生日年份，不修改，点击确定"""
    def editor_baby_birth_year_confirm(self):
        # 进入宝贝信息页面
        self.find_element_id(self._iv_baby_info).click()
        # 点击宝贝生日，进入编辑宝贝生日页面
        self.find_element_id(self._rl_baby_birth_display).click()
        # 点击修改年份
        self.find_element_id(self._tv_editor_baby_birth_year).click()
        # 不修改年份，点击确定按钮
        self.find_element_id(self._btn_editor_baby_birth_confirm).click()

    """5.修改宝贝生日月份，修改后点击取消"""
    def editor_baby_birth_month_cancel(self):
        # 进入宝贝信息页面
        self.find_element_id(self._iv_baby_info).click()
        # 修改宝贝生日月份
        self.editor_baby_birth_month_success()
        self.find_element_id(self._btn_editor_baby_birth_cancel).click()

    """6.修改宝贝生日月份，修改后点击确定"""
    def editor_baby_birth_month_confirm(self):
        # 进入宝贝信息页面
        self.find_element_id(self._iv_baby_info).click()
        # 修改宝贝生日月份
        self.editor_baby_birth_month_success()
        self.find_element_id(self._btn_editor_baby_birth_confirm).click()

    """7.修改宝贝生日日期，修改后点击取消"""
    def editor_baby_birth_day_cancel(self):
        # 进入宝贝信息页面
        self.find_element_id(self._iv_baby_info).click()
        # 修改宝贝生日月份
        self.editor_baby_birth_day_success()
        self.find_element_id(self._btn_editor_baby_birth_cancel)

    """8.修改宝贝生日日期，修改后点击确认按钮"""
    def editor_baby_birth_day_confirm(self):
        self.editor_baby_birth_day_success()
        self.find_element_id(self._btn_editor_baby_birth_confirm).click()

    """宝贝信息页面显示的宝贝生日"""
    def baby_information_baby_birth_display(self):
        baby_info_baby_birth_display = self.find_element_id(self._tv_baby_birth_detail_display).text
        return baby_info_baby_birth_display

    """将我的页面中宝贝年龄分割为独立字符串"""
    def split_my_page_baby_age_display(self):
        # 返回我的页面
        self.find_element_id(self._iv_baby_information_display_back).click()
        # 获取页面显示的宝贝昵称、性别、年龄
        my_page_baby_infos_display = self.find_element_id(self._tv_show_baby_info).text
        # 先将字符串按照”/“分割一个列表，列表中存放两个字符串，一个为昵称，另一个为性别和年龄
        my_page_baby_infos = my_page_baby_infos_display.split("/")
        # 将存放宝贝性别和年龄的列表按照空格切割一次，切割后的列表中存放两个字符串，一个为性别，一个为年龄
        my_page_baby_sex_and_age = my_page_baby_infos[1].split(" ", 1)
        # 读取列表中宝贝性别
        my_page_baby_age_display = my_page_baby_sex_and_age[1]
        return my_page_baby_age_display

    """1.取消修改与宝贝的关系"""
    def editor_baby_relation_cancel(self):
        # 点击与宝贝关系，底部弹框显示宝贝关系
        self.find_element_id(self._rl_baby_relation_display).click()
        # 点击取消按钮
        self.find_element_id(self._tv_editor_baby_relation_cancel).click()

    """2.不修改与宝贝的关系，点击确定"""
    def editor_baby_relation_confirm(self):
        # 点击与宝贝关系，底部弹框显示宝贝关系
        self.find_element_id(self._rl_baby_relation_display).click()
        # 点击取消按钮
        self.find_element_id(self._tv_editor_baby_relation_confirm).click()

    """3.修改与宝贝的关系，不保存"""
    def editor_baby_relation_cancel_editor(self):
        # 点击与宝贝关系，底部弹框显示宝贝关系--滑动选择与宝贝关系--取消
        self.find_element_id(self._rl_baby_relation_display).click()
        self.slide.swipe_up(500)
        self.find_element_id(self._tv_editor_baby_relation_cancel).click()
        time.sleep(1)

    """4.滑动任意位置修改与宝贝的关系，并修改成功"""
    def editor_baby_relation_success(self):
        # 点击与宝贝关系，底部弹框显示宝贝关系--滑动选择与宝贝关系--确认
        self.find_element_id(self._rl_baby_relation_display).click()
        self.slide.swipe_up(500)
        self.find_element_id(self._tv_editor_baby_relation_confirm).click()
        time.sleep(1)

    """5.下滑一个，修改与宝贝的关系：爸爸-亲友-阿姨-叔叔-外婆-外公-姥姥-姥爷-奶奶-爷爷-妈妈"""
    def editor_baby_relation_down(self):
        # 点击与宝贝关系，底部弹框显示宝贝关系
        self.find_element_id(self._rl_baby_relation_display).click()
        # 下滑修改下一个与宝贝关系
        self.slide.swipe_down_baby_relation(1000)
        self.find_element_id(self._tv_editor_baby_relation_confirm).click()

    """6.上滑一个，修改与宝贝的关系：爸爸-妈妈-爷爷-奶奶-姥爷-姥姥-外公-外婆-叔叔-阿姨-亲友"""
    def editor_baby_relation_up(self):
        # 点击与宝贝关系，底部弹框显示宝贝关系
        self.find_element_id(self._rl_baby_relation_display).click()
        # 上滑修改上一个与宝贝关系
        self.slide.swipe_up_baby_relation(1000)
        self.find_element_id(self._tv_editor_baby_relation_confirm).click()

    """我的页面当前家庭圈管理员的与宝贝关系"""
    def my_page_baby_relation_display(self):
        my_page_baby_relation = self.find_element_id(self._tv_baby_relation).text
        return my_page_baby_relation
