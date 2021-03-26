# 我的页面--已创建或加入家庭圈
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.editor_baby_info_page import EditorBabyInfoPage


class MyFamilyPage(BasePage):
    # 宝贝信息页面入口
    _iv_editor_baby_info_portrait = (By.ID, "com.intretech.readerx:id/img_person_portrait")

    """以下内容为我的页面显示的宝贝信息，包括头像、昵称、性别、年龄"""
    # 宝贝昵称、性别、年龄显示
    _tv_show_baby_info = (By.ID, "com.intretech.readerx:id/tv_person_name")

    """进入编辑宝贝信息页面"""
    def enter_editor_baby_info(self):
        self.find_element_id(self._iv_editor_baby_info_portrait).click()
        return EditorBabyInfoPage(self.driver)

    """宝贝昵称、性别、年龄显示，将宝贝昵称分割为独立字符串"""
    def split_baby_name_display(self):
        # 获取页面显示的宝贝昵称、性别、年龄
        show_baby_info = self.find_element_id(self._tv_show_baby_info).text
        # 先将字符串按照”/“分割一个列表，列表中存放两个字符串，一个为昵称，另一个为性别和年龄
        baby_infos = show_baby_info.split("/")
        print(baby_infos)
        # 获取宝贝昵称
        baby_name = baby_infos[0]
        print(baby_name)
        return baby_name

    """宝贝昵称、性别、年龄显示，将宝贝性别分割为独立字符串"""
    def split_baby_sex_display(self):
        # 获取页面显示的宝贝昵称、性别、年龄
        show_baby_info = self.find_element_id(self._tv_show_baby_info).text
        # 先将字符串按照”/“分割一个列表，列表中存放两个字符串，一个为昵称，另一个为性别和年龄
        baby_infos = show_baby_info.split("/")
        print(baby_infos)
        # 将存放宝贝性别和年龄的列表按照空格切割一次，切割后的列表中存放两个字符串，一个为性别，一个为年龄
        baby_sex_and_age = baby_infos[1].split(" ", 1)
        print(baby_sex_and_age)
        # 读取列表中宝贝性别
        baby_sex = baby_sex_and_age[0]
        print(baby_sex)
        return baby_sex

    """宝贝昵称、性别、年龄显示，将宝贝年龄分割为独立字符串"""
    def split_baby_age_display(self):
        # 获取页面显示的宝贝昵称、性别、年龄
        show_baby_info = self.find_element_id(self._tv_show_baby_info).text
        # 先将字符串按照”/“分割一个列表，列表中存放两个字符串，一个为昵称，另一个为性别和年龄
        baby_infos = show_baby_info.split("/")
        print(baby_infos)
        # 将存放宝贝性别和年龄的列表按照空格切割一次，切割后的列表中存放两个字符串，一个为性别，一个为年龄
        baby_sex_and_age = baby_infos[1].split(" ", 1)
        print(baby_sex_and_age)
        # 读取列表中宝贝年龄
        baby_age = baby_sex_and_age[1]
        print(baby_age)
        return baby_age
