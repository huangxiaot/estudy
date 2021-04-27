import time
from page.base_page_two import BasePageTwo


class EditorPortraitParam(BasePageTwo):
    # 拍照和相册按钮
    rl_my_account_photo_album = 'className("android.widget.RelativeLayout")'
    # 系统拍照页面的拍照按钮
    iv_editor_baby_avatar_take_photo = 'resourceId("com.android.camera:id/shutter_button")'
    # 系统拍照后确认按钮
    btn_editor_baby_avatar_confirm_photo = 'resourceId("com.android.camera:id/done_button")'
    # 系统拍照后重拍按钮
    _iv_editor_baby_avatar_rephotograph = 'resourceId("com.android.camera:id/retake_button")'
    # 系统拍照后取消按钮
    _btn_editor_baby_avatar_cancel_photo = 'resourceId("com.android.camera:id/cancel_button")'
    # 系统拍照-确认-裁剪页面"✔"
    _tv_editor_baby_avatar_tailor_confirm = 'resourceId("com.intretech.readerx:id/menu_crop")'
    # 裁剪页面左上角“x"
    _btn_editor_baby_avatar_tailor_cancel = "android.widget.ImageButton"
    # 系统相册中照片列表
    _iv_editor_baby_avatar_system_photo_album = "android.widget.ImageView"

    """进入拍照页面"""
    """
        1.判断页面是否存在拍照按钮
        2.存在点击，不存在输出”找不到我的头像入口“
    """
    def enter_take_photo(self):
        time.sleep(1)
        try:
            my_account = self.elements_android_uiautomator(self.rl_my_account_photo_album)
        except:
            print("找不到拍照按钮")
        else:
            my_account[0].click()

    """进入相册页面"""
    """
        1.判断页面是否存在相册按钮
        2.存在点击，不存在输出”找不到我的头像入口“
    """
    def enter_photo_album(self):
        time.sleep(1)
        try:
            my_account = self.elements_android_uiautomator(self.rl_my_account_photo_album)
        except:
            print("找不到相册按钮")
        else:
            my_account[1].click()
