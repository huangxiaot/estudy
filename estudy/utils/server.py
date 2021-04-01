# 调用服务器的接口
import requests
import json


class InvokeServer:
    def __init__(self, phone):
        self.phone = phone

    # 清除用户的账号信息--测试服
    def clear_user_info(self, phone):
        # 清除账号信息的URL
        clear_user_url = "http://estudy.umsin.com:8080/estudy/book/deleteUser?"
        # 传入的参数
        request_data = ({"telephone": phone, "markCode": "32ee7458693347588ff88cd380e564cb"})
        # 使用get请求
        ret = requests.get(clear_user_url, request_data)
        # 判断服务器的返回结果，200：服务器已成功处理了请求。 通常，这表示服务器提供了请求的网页。
        if ret.status_code == 200:
            text = json.loads(ret.text)
            print(text)


# 测试函数，实际运行过程中可以注释
# if __name__ == '__main__':
#     invoke_server = InvokeServer()
#     invoke_server.clear_user_info("86+15059941156")
