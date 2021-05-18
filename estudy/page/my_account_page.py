# 我的账号页面相关操作
import time
from page.base_page_two import BasePageTwo
from param.editor_portrait_param import EditorPortraitParam


class MyAccountPage(BasePageTwo):

    def __init__(self, driver):
        super().__init__(driver)
        self.portrait_param = EditorPortraitParam(driver)

    """头像相关"""
    # 头像显示
    _rl_my_account_portrait_display = 'className("android.widget.RelativeLayout")'

    """昵称相关"""
    # 昵称显示
    _rl_my_account_name_display = 'className("android.widget.RelativeLayout")'
    # 修改昵称页面昵称输入框
    _et_editor_my_account_name = 'resourceId("com.intretech.readerx:id/edit_modify")'
    # 修改昵称页面确认按钮
    _iv_editor_my_account_confirm = 'resourceId("com.intretech.readerx:id/btn_toolbar_more")'
    # 修改昵称页面删除输入的昵称
    _iv_clear_my_account = 'resourceId("com.intretech.readerx:id/img_modify_clear")'

    # 返回键
    _iv_my_account_back = 'resourceId("com.intretech.readerx:id/btn_toolbar_back")'

    """
    1.判断页面是否存在头像入口
    2.存在点击，不存在输出”找不到我的头像入口“
    """
    def enter_my_account_portrait(self):
        time.sleep(1)
        try:
            my_account_portrait = self.elements_android_uiautomator(self._rl_my_account_portrait_display)
        except:
            print("找不到我的头像显示")
        else:
            my_account_portrait[0].click()

    """拍照修改头像"""
    def editor_my_account_portrait_photo(self):
        # 进入我的头像--拍照修改头像
        self.enter_my_account_portrait()
        self.portrait_param.enter_take_photo()

    """相册修改头像"""
    def editor_my_account_portrait_album(self):
        # 进入我的头像--相册修改头像
        self.enter_my_account_portrait()
        self.portrait_param.enter_photo_album()

    """
    1.判断页面是否存在昵称入口
    2.存在点击，不存在输出”找不到我的昵称显示“
    """
    def enter_my_account_name(self):
        time.sleep(1)
        try:
            my_account = self.elements_android_uiautomator(self._rl_my_account_name_display)
        except:
            print("找不到我的昵称显示")
        else:
            my_account[1].click()

    """我的账户号昵称输入框设置"""
    def editor_my_account_name(self, my_account_name):
        time.sleep(1)
        self.element_android_uiautomator(self._et_editor_my_account_name).clear()
        self.element_android_uiautomator(self._et_editor_my_account_name).send_keys(my_account_name)

    """我的账号昵称修改成功"""
    def editor_my_account_name_success(self, my_account_name):
        # 进入我的账号页面，修改昵称
        self.enter_my_account_name()
        self.editor_my_account_name(my_account_name)
        self.element_android_uiautomator(self._iv_editor_my_account_confirm).click()
        time.sleep(2)

    """使用弹框异常处理"""
