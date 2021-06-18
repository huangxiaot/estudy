# 修改宝贝信息
import pytest
import yaml
from page.start import AppStart


class TestEditorBabyInfo:
    # 这边打开yaml文件需要使用绝对路径
    editor_baby_name_data = yaml.safe_load(open("E:\\study\\Fork\\estudy\\estudy\\data\\baby_name.yaml", "r", encoding= "utf-8"))
    print(editor_baby_name_data)

    def setup_class(self):
        self.editor_baby_info = AppStart.start().enter_editor_baby_info_page()

    # """1.取消修改宝贝头像"""
    # @pytest.mark.run(order=1)
    # def test_editor_baby_portrait_cancel(self):
    #     self.editor_baby_info.editor_baby_portrait_cancel()
    #     print("1.取消修改宝贝头像成功")

    """2.拍照方式修改宝贝头像成功"""
    @pytest.mark.run(order=2)
    def test_editor_portrait_photograph_success(self):
        self.editor_baby_info.editor_baby_portrait_photograph_success()
        print("2.拍照方式宝贝头像修改成功")

    # """3.拍照方式修改宝贝头像，未拍照，在系统拍照页面取消拍照"""
    # @pytest.mark.run(order=3)
    # def test_editor_baby_portrait_photograph_cancel(self):
    #     self.editor_baby_info.editor_baby_portrait_photograph_cancel()
    #     print("3.拍照方式取消拍照成功")

    # """4.拍照方式修改宝贝头像，已拍照，在拍的照片页面取消拍照"""
    # @pytest.mark.run(order=4)
    # def test_editor_baby_portrait_photograph_cancel_photo(self):
    #     self.editor_baby_info.editor_baby_portrait_photograph_cancel_photo()
    #     print("4.拍照方式已拍照，取消拍照成功")

    # """5.拍照方式修改宝贝头像，已拍照，在裁剪页面点击“x”"""
    # @pytest.mark.run(order=5)
    # def test_editor_baby_portrait_photograph_cancel_tailor(self):
    #     self.editor_baby_info.editor_baby_portrait_photograph_cancel_tailor()
    #     print("5.拍照方式取消裁剪成功")

    """6.相册方式修改宝贝头像，修改成功"""
    @pytest.mark.run(order=6)
    def test_editor_baby_portrait_photo_album_success(self):
        self.editor_baby_info.editor_baby_portrait_photo_album_success()
        print("6.相册方式修改宝贝头像成功")

    # """7.相册方式修改宝贝头像，相册页面取消"""
    # @pytest.mark.run(order=7)
    # def test_editor_baby_portrait_photo_album_cancel(self):
    #     self.editor_baby_info.editor_baby_portrait_photo_album_cancel()
    #     print("7.相册方式，在系统相册页面取消修改宝贝头像成功")

    # """8.相册方式修改宝贝头像，裁剪页面取消"""
    # @pytest.mark.run(order=8)
    # def test_editor_baby_portrait_photo_album_cancel_tailor(self):
    #     self.editor_baby_info.editor_baby_portrait_photo_album_cancel_tailor()
    #     print("8.相册方式，选择相册后在裁剪页面取消修改宝贝头像成功")

    # """宝贝信息页面判断修改前后的宝贝头像相似度"""
    # def test_check_baby_info_baby_portrait(self):
    #     self.editor_baby_info.check_baby_info_baby_portrait()
    #
    # """我的页面判断修改前后的宝贝头像相似率"""
    # def test_check_my_page_baby_portrait(self):
    #     self.editor_baby_info.check_my_page_baby_portrait()

    """1.修改宝贝昵称，并修改成功"""
    @pytest.mark.run(order=9)
    @pytest.mark.parametrize("editor_baby_name", editor_baby_name_data)
    def test_editor_baby_name_success(self, editor_baby_name):
        self.editor_baby_info.editor_baby_name_success(editor_baby_name)
        # 判断修改的宝贝昵称与宝贝信息页面显示的宝贝昵称是否一致
        assert self.editor_baby_info.baby_information_baby_name_display() == editor_baby_name
        print("1.修改的宝贝昵称与宝贝信息页面显示的宝贝昵称一致")
        # 判断修改的宝贝昵称与我的页面显示的宝贝昵称是否一致
        assert self.editor_baby_info.split_baby_name_display() == editor_baby_name
        print("1.修改的宝贝昵称与我的信息页面显示的宝贝昵称一致")

    """2.未修改宝贝昵称，点击返回"""
    @pytest.mark.run(order=10)
    def test_editor_baby_name_back(self):
        self.editor_baby_info.editor_baby_name_back()
        assert self.editor_baby_info.baby_information_baby_name_display() == "蜗牛宝宝"
        print("2.修改的宝贝昵称与宝贝信息页面显示的宝贝昵称一致")
        assert self.editor_baby_info.split_baby_name_display() == "蜗牛宝宝"
        print("2.修改的宝贝昵称与我的信息页面显示的宝贝昵称一致")

    """3.未修改宝贝昵称，点击确定"""
    @pytest.mark.run(order=11)
    def test_editor_baby_name_confirm(self):
        self.editor_baby_info.editor_baby_name_confirm()
        assert self.editor_baby_info.baby_information_baby_name_display() == "蜗牛宝宝"
        print("3.修改的宝贝昵称与宝贝信息页面显示的宝贝昵称一致")
        assert self.editor_baby_info.split_baby_name_display() == "蜗牛宝宝"
        print("3.修改的宝贝昵称与我的信息页面显示的宝贝昵称一致")

    """4.已修改宝贝昵称，点击返回-取消"""
    @pytest.mark.run(order=12)
    def test_editor_baby_name_back_cancel(self):
        editor_baby_name = "蜗牛宝宝啊"
        self.editor_baby_info.editor_baby_name_back_cancel(editor_baby_name)
        assert self.editor_baby_info.baby_information_baby_name_display() == "蜗牛宝宝啊"
        print("4.修改的宝贝昵称与宝贝信息页面显示的宝贝昵称一致")
        assert self.editor_baby_info.split_baby_name_display() == "蜗牛宝宝啊"
        print("4.修改的宝贝昵称与我的信息页面显示的宝贝昵称一致")

    """5.已修改宝贝昵称，点击返回-确定"""
    @pytest.mark.run(order=13)
    def test_editor_baby_name_back_confirm(self):
        editor_baby_name = "蜗牛宝宝哦"
        self.editor_baby_info.editor_baby_name_back_confirm(editor_baby_name)
        assert self.editor_baby_info.baby_information_baby_name_display() == "蜗牛宝宝啊"
        print("5.修改的宝贝昵称与宝贝信息页面显示的宝贝昵称一致")
        assert self.editor_baby_info.split_baby_name_display() == "蜗牛宝宝啊"
        print("5.修改的宝贝昵称与我的信息页面显示的宝贝昵称一致")

    """6.修改宝贝昵称为空"""
    @pytest.mark.run(order=14)
    def test_editor_baby_name_null(self):
        editor_baby_name = "蜗牛宝宝"
        self.editor_baby_info.editor_baby_name_null()
        self.editor_baby_info.toast.get_toast("请输入宝宝的昵称哦")
        self.editor_baby_info.modify_baby_name(editor_baby_name)
        assert self.editor_baby_info.baby_information_baby_name_display() == "蜗牛宝宝"
        print("6.修改的宝贝昵称与宝贝信息页面显示的宝贝昵称一致")
        assert self.editor_baby_info.split_baby_name_display() == "蜗牛宝宝"
        print("6.修改的宝贝昵称与我的信息页面显示的宝贝昵称一致")

    """7.修改宝贝昵称，大于16个字，选取前面16个字"""
    @pytest.mark.run(order=15)
    def test_editor_baby_name_sixteen_word(self):
        editor_baby_name = "蜗牛宝宝abcdefghijklmn"
        self.editor_baby_info.editor_baby_name_success(editor_baby_name)
        assert self.editor_baby_info.baby_information_baby_name_display() == "蜗牛宝宝abcdefghijkl"
        print("修改的宝贝昵称与宝贝信息页面显示的宝贝昵称一致")
        assert self.editor_baby_info.split_baby_name_display() == "蜗牛宝宝abcdefghijkl"
        print("修改的宝贝昵称与我的信息页面显示的宝贝昵称一致")

    """1.修改宝贝性别女成功"""
    @pytest.mark.run(order=16)
    def test_editor_baby_sex_girl_success(self):
        self.editor_baby_info.editor_baby_sex_girl_success()
        # 判断修改的宝贝性别与我的页面显示的宝贝性别是否一致
        assert self.editor_baby_info.split_baby_sex_display() == "女宝"
        print("1.修改的宝贝性别女与我的信息页面显示的宝贝性别一致")

    """2.修改宝贝性别男成功"""
    @pytest.mark.run(order=17)
    def test_editor_baby_sex_boy_success(self):
        self.editor_baby_info.editor_baby_sex_boy_success()
        # 判断修改的宝贝性别与我的页面显示的宝贝性别是否一致
        assert self.editor_baby_info.split_baby_sex_display() == "男宝"
        print("2.修改的宝贝性别男与我的信息页面显示的宝贝性别一致")

    # """1.不修改宝贝生日，点击取消按钮"""
    # @pytest.mark.run(order=18)
    # def test_editor_baby_birth_cancel(self):
    #     self.editor_baby_info.editor_baby_birth_cancel()
    #     # 判断宝贝信息页面的宝贝生日显示
    #     assert self.editor_baby_info.baby_information_baby_birth_display() == "2000-05-18"
    #     print("1.修改的宝贝生日与宝贝信息页面显示的宝贝生日一致")
    #     # 判断我的页面显示的宝贝年龄显示
    #     assert self.editor_baby_info.split_my_page_baby_age_display() == "20岁 十个月"
    #     print("1.修改的宝贝生日与我的页面显示的宝贝年龄一致")

    # """2.不修改宝贝生日，点击确定按钮"""
    # @pytest.mark.run(order=19)
    # def test_editor_baby_birth_confirm(self):
    #     self.editor_baby_info.editor_baby_birth_confirm()
    #     # 判断宝贝信息页面的宝贝生日显示
    #     assert self.editor_baby_info.baby_information_baby_birth_display() == "2000-05-18"
    #     print("2.修改的宝贝生日与宝贝信息页面显示的宝贝生日一致")
    #     # 判断我的页面显示的宝贝年龄显示
    #     assert self.editor_baby_info.split_my_page_baby_age_display() == "20岁 十个月"
    #     print("2.修改的宝贝生日与我的页面显示的宝贝年龄一致")
    #
    # """3.点击宝贝生日年份，不修改，点击取消"""
    # @pytest.mark.run(order=20)
    # def test_editor_baby_birth_year_cancel(self):
    #     self.editor_baby_info.editor_baby_birth_year_cancel()
    #     # 判断宝贝信息页面的宝贝生日显示
    #     assert self.editor_baby_info.baby_information_baby_birth_display() == "2000-05-18"
    #     print("3.修改的宝贝生日与宝贝信息页面显示的宝贝生日一致")
    #     # 判断我的页面显示的宝贝年龄显示
    #     assert self.editor_baby_info.split_my_page_baby_age_display() == "20岁 十个月"
    #     print("3.修改的宝贝生日与我的页面显示的宝贝年龄一致")
    #
    # """4.点击宝贝生日年份，不修改，点击确定"""
    # @pytest.mark.run(order=21)
    # def test_editor_baby_birth_year_confirm(self):
    #     self.editor_baby_info.editor_baby_birth_year_confirm()
    #     # 判断宝贝信息页面的宝贝生日显示
    #     assert self.editor_baby_info.baby_information_baby_birth_display() == "2000-05-18"
    #     print("4.修改的宝贝生日与宝贝信息页面显示的宝贝生日一致")
    #     # 判断我的页面显示的宝贝年龄显示
    #     assert self.editor_baby_info.split_my_page_baby_age_display() == "20岁 十个月"
    #     print("4.修改的宝贝生日与我的页面显示的宝贝年龄一致")
    #
    # """5.修改宝贝生日月份，修改后点击取消"""
    # @pytest.mark.run(order=22)
    # def test_editor_baby_birth_month_cancel(self):
    #     self.editor_baby_info.editor_baby_birth_month_cancel()
    #     # 判断宝贝信息页面的宝贝生日显示
    #     assert self.editor_baby_info.baby_information_baby_birth_display() == "2000-05-18"
    #     print("5.修改的宝贝生日与宝贝信息页面显示的宝贝生日一致")
    #     # 判断我的页面显示的宝贝年龄显示
    #     assert self.editor_baby_info.split_my_page_baby_age_display() == "20岁 十个月"
    #     print("5.修改的宝贝生日与我的页面显示的宝贝年龄一致")

    # """6.修改宝贝生日月份，修改后点击确定"""
    # @pytest.mark.run(order=23)
    # def test_editor_baby_birth_month_confirm(self):
    #     self.editor_baby_info.editor_baby_birth_month_confirm()
    #     # 判断宝贝信息页面的宝贝生日显示
    #     assert self.editor_baby_info.baby_information_baby_birth_display() == "2000-05-18"
    #     print("6.修改的宝贝生日与宝贝信息页面显示的宝贝生日一致")
    #     # 判断我的页面显示的宝贝年龄显示
    #     assert self.editor_baby_info.split_my_page_baby_age_display() == "20岁 十个月"
    #     print("6.修改的宝贝生日与我的页面显示的宝贝年龄一致")

    # """7.修改宝贝生日日期，修改后点击取消"""
    # @pytest.mark.run(order=24)
    # def test_editor_baby_birth_day_cancel(self):
    #     self.editor_baby_info.editor_baby_birth_day_cancel()
    #     # 判断宝贝信息页面的宝贝生日显示
    #     assert self.editor_baby_info.baby_information_baby_birth_display() == "2000-05-18"
    #     print("7.修改的宝贝生日与宝贝信息页面显示的宝贝生日一致")
    #     # 判断我的页面显示的宝贝年龄显示
    #     assert self.editor_baby_info.split_my_page_baby_age_display() == "20岁 十个月"
    #     print("7.修改的宝贝生日与我的页面显示的宝贝年龄一致")

    # """8.修改宝贝生日日期，修改后点击确认按钮"""
    # @pytest.mark.run(order=25)
    # def test_editor_baby_birth_day_confirm(self):
    #     self.editor_baby_info.editor_baby_birth_day_confirm()
    #     # 判断宝贝信息页面的宝贝生日显示
    #     assert self.editor_baby_info.baby_information_baby_birth_display() == "2000-05-15"
    #     print("8.修改的宝贝生日与宝贝信息页面显示的宝贝生日一致")
    #     # 判断我的页面显示的宝贝年龄显示
    #     assert self.editor_baby_info.split_my_page_baby_age_display() == "20岁 十个月"
    #     print("8.修改的宝贝生日与我的页面显示的宝贝年龄一致")

    """9.修改宝贝生日所有信息"""
    @pytest.mark.run(order=26)
    def test_editor_baby_birth(self):
        self.editor_baby_info.editor_baby_birth()
        # 判断宝贝信息页面的宝贝生日显示
        assert self.editor_baby_info.baby_information_baby_birth_display() == "1994-05-15"
        print("8.修改的宝贝生日与宝贝信息页面显示的宝贝生日一致")
        # 判断我的页面显示的宝贝年龄显示
        assert self.editor_baby_info.split_my_page_baby_age_display() == "27岁 0个月"
        print("8.修改的宝贝生日与我的页面显示的宝贝年龄一致")

    # """1.取消修改与宝贝的关系"""
    # @pytest.mark.run(order=27)
    # def test_editor_baby_relation_cancel(self):
    #     self.editor_baby_info.editor_baby_relation_cancel()
    #     # 判断宝贝信息页面的与宝贝关系显示
    #     assert self.editor_baby_info.baby_information_baby_relation_display() == "爸爸"
    #     print("1.修改的与宝贝关系与宝贝信息页面显示的与宝贝关系一致")

    # """2.不修改与宝贝的关系，点击确定"""
    # @pytest.mark.run(order=27)
    # def test_editor_baby_relation_confirm(self):
    #     self.editor_baby_info.editor_baby_relation_confirm()
    #     # 判断宝贝信息页面的与宝贝关系显示
    #     assert self.editor_baby_info.baby_information_baby_relation_display() == "爸爸"
    #     print("2.修改的与宝贝关系与宝贝信息页面显示的与宝贝关系一致")
    #
    # """3.修改与宝贝的关系，不保存"""
    # @pytest.mark.run(order=28)
    # def test_editor_baby_relation_cancel_editor(self):
    #     self.editor_baby_info.editor_baby_relation_cancel_editor()
    #     # 判断宝贝信息页面的与宝贝关系显示
    #     assert self.editor_baby_info.baby_information_baby_relation_display() == "爸爸"
    #     print("3.修改的与宝贝关系与宝贝信息页面显示的与宝贝关系一致")
    #
    # """4.下滑一个，修改与宝贝的关系：爸爸-亲友-阿姨-叔叔-外婆-外公-姥姥-姥爷-奶奶-爷爷-妈妈"""
    # @pytest.mark.run(order=29)
    # def test_editor_baby_relation_down(self):
    #     self.editor_baby_info.editor_baby_relation_down()
    #     # 判断宝贝信息页面的与宝贝关系显示
    #     assert self.editor_baby_info.baby_information_baby_relation_display() == "亲友"
    #     print("4.修改的与宝贝关系与宝贝信息页面显示的与宝贝关系一致")
    #
    # """5.上滑一个，修改与宝贝的关系：爸爸-妈妈-爷爷-奶奶-姥爷-姥姥-外公-外婆-叔叔-阿姨-亲友"""
    # @pytest.mark.run(order=30)
    # def test_editor_baby_relation_up(self):
    #     self.editor_baby_info.editor_baby_relation_up()
    #     # 判断宝贝信息页面的与宝贝关系显示
    #     assert self.editor_baby_info.baby_information_baby_relation_display() == "爸爸"
    #     print("5.修改的与宝贝关系与宝贝信息页面显示的与宝贝关系一致")

    """6.滑动任意位置修改与宝贝的关系，并修改成功"""
    @pytest.mark.run(order=31)
    def test_editor_baby_relation_success(self):
        self.editor_baby_info.editor_baby_relation_success()

    def teardown_class(self):
        AppStart.quit()
