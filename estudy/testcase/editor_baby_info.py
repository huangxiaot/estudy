import pytest
from page.start import AppStart


class TestEditorBabyInfo:
    def setup_class(self):
        self.editor_baby_info = AppStart.start().enter_my_family_page().enter_editor_baby_info()

    """取消修改宝贝头像"""
    @pytest.mark.run(order=1)
    def test_editor_baby_portrait_cancel(self):
        self.editor_baby_info.editor_baby_portrait_cancel()

    """1.拍照方式修改宝贝头像成功"""
    @pytest.mark.run(order=2)
    def test_editor_portrait_photograph_success(self):
        self.editor_baby_info.editor_baby_portrait_photograph_success()

    """2.拍照方式修改宝贝头像，未拍照，在系统拍照页面取消拍照"""
    @pytest.mark.run(order=3)
    def test_editor_baby_portrait_photograph_cancel(self):
        self.editor_baby_info.editor_baby_portrait_photograph_cancel()

    """3.拍照方式修改宝贝头像，已拍照，在拍的照片页面取消拍照"""
    @pytest.mark.run(order=4)
    def test_editor_baby_portrait_photograph_cancel_photo(self):
        self.editor_baby_info.editor_baby_portrait_photograph_cancel_photo()

    """4.拍照方式修改宝贝头像，已拍照，在裁剪页面点击“x”"""
    @pytest.mark.run(order=5)
    def test_editor_baby_portrait_photograph_cancel_tailor(self):
        self.editor_baby_info.editor_baby_portrait_photograph_cancel_tailor()

    """1.相册方式修改宝贝头像，修改成功"""
    @pytest.mark.run(order=6)
    def test_editor_baby_portrait_photo_album_success(self):
        self.editor_baby_info.editor_baby_portrait_photo_album_success()

    """2.相册方式修改宝贝头像，相册页面取消"""
    @pytest.mark.run(order=7)
    def test_editor_baby_portrait_photo_album_cancel(self):
        self.editor_baby_info.editor_baby_portrait_photo_album_cancel()

    """3.相册方式修改宝贝头像，裁剪页面取消"""
    @pytest.mark.run(order=8)
    def test_editor_baby_portrait_photo_album_cancel_tailor(self):
        self.editor_baby_info.editor_baby_portrait_photo_album_cancel_tailor()

    """1.修改宝贝昵称，并修改成功"""
    def test_editor_baby_name_success(self):
        editor_baby_name = "蜗牛宝宝"
        self.editor_baby_info.editor_baby_name_success(editor_baby_name)
        assert self.editor_baby_info.check_result_baby_name() == editor_baby_name
        print("修改的宝贝昵称与显示的宝贝昵称一致")

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
