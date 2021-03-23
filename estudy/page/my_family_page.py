# 我的页面--已创建或加入家庭圈
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.editor_baby_info_page import EditorBabyInfoPage


class MyFamilyPage(BasePage):
    # 宝贝信息页面入口
    _iv_editor_baby_info_portrait = (By.ID, "com.intretech.readerx:id/img_person_portrait")

    def enter_editor_baby_info(self):
        self.find_element_id(self._iv_editor_baby_info_portrait).click()
        return EditorBabyInfoPage(self.driver)
