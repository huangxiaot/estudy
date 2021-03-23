from page.start import AppStart


class TestEditorBabyInfo:
    def setup_class(self):
        self.editor_baby_info = AppStart.start().enter_my_family_page().enter_editor_baby_info()

    """拍照方式修改宝贝头像"""
    def test_editor_portrait_photograph(self):
        self.editor_baby_info.editor_baby_portrait_photograph()

    """相册方式修改宝贝头像"""
    def test_editor_baby_portrait_photo_album(self):
        self.editor_baby_info.editor_baby_portrait_photo_album()

    """修改宝贝昵称"""
    def test_editor_baby_name(self):
        pass

    """修改宝贝头像"""
    def test_editor_baby_sex(self):
        self.editor_baby_info.editor_baby_sex()
