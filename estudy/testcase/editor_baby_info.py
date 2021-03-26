from page.start import AppStart


class TestEditorBabyInfo:
    def setup_class(self):
        self.editor_baby_info = AppStart.start().enter_my_family_page().enter_editor_baby_info()

    """拍照方式修改宝贝头像成功"""
    def test_editor_portrait_photograph_success(self):
        self.editor_baby_info.editor_baby_portrait_photograph_success()

    """相册方式修改宝贝头像成功"""
    def test_editor_baby_portrait_photo_album_success(self):
        self.editor_baby_info.editor_baby_portrait_photo_album_success()

    """修改宝贝昵称成功"""
    def test_editor_baby_name_success(self):
        editor_baby_name = "蜗牛宝宝"
        self.editor_baby_info.editor_baby_name_success(editor_baby_name)

    """修改宝贝性别成功"""
    def test_editor_baby_sex_success(self):
        self.editor_baby_info.editor_baby_sex_success()

    """修改宝贝生日成功"""
    def test_editor_baby_birth_success(self):
        self.editor_baby_info.editor_baby_birth_success()

    """修改与宝贝的关系成功"""
    def test_editor_baby_relation_success(self):
        self.editor_baby_info.editor_baby_relation_success()

    def teardown_class(self):
        AppStart.quit()
