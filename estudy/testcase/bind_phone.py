# 绑定手机号页面测试用例
from page.start import AppStart


class TestBindPhone:
    def setup_class(self):
        self.bind_phone_page = AppStart.start().enter_bind_phone_page()

    def test_success(self):
        phone = "15059941156"
        self.bind_phone_page.success(phone)
        self.bind_phone_page.invoke_server.clear_user_info("86+" + phone)
