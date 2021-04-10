# 绑定手机号页面测试用例
import time
import pytest
import yaml
from page.start import AppStart


class TestBindPhone:
    # 读取外部yaml文件内容，转换成utf-8格式
    register_phone_data = yaml.safe_load(open("E:\\study\\Fork\\estudy\\estudy\\data\\register_phone.yaml", "r", encoding="utf-8"))
    print(register_phone_data)

    def setup_class(self):
        self.bind_phone_page = AppStart.start().enter_bind_phone_page()

    """调用测试服清除账号接口，清除账号信息"""
    """由于一个手机号每天只能发送10条验证码，现使用特殊版本，不需要验证码就能登录"""
    @pytest.mark.parametrize("phone", register_phone_data)
    def test_success(self, phone):
        self.bind_phone_page.register_and_logout(phone)
        assert self.bind_phone_page.my_account_page_phone_display() == "+86-" + phone
        self.bind_phone_page.invoke_server.clear_user_info("86+" + phone)

    """1.手机号最长只能输入11位"""
    @pytest.mark.run(order=2)
    def test_phone_more_larger(self):
        phone = "123456789123456"
        self.bind_phone_page.input_phone_number(phone)
        assert self.bind_phone_page.bind_page_phone_display() == "12345678912"
        print("1.手机号码最长只能输入11位")

    """2.连续点击获取验证码按钮"""
    @pytest.mark.run(order=3)
    def test_repeat_get_verify_code(self):
        phone = "15056654452"
        self.bind_phone_page.repeat_get_verify_code(phone)
        time.sleep(1)
        self.bind_phone_page.toast.get_toast("每分钟发送次数超限")

    """3.自动获取短信验证码"""
    @pytest.mark.run(order=4)
    def test_auto_fill_verify_code(self):
        pass
