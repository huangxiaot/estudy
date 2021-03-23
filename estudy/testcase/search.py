# 搜索测试用例
import pytest
import yaml
from page.start import AppStart


class TestSearch:
    # 读取外部yaml文件内容，转换成utf-8格式
    search_context_data = yaml.safe_load(open("E:\\study\\Fork\\estudy\\estudy\\data\\search.yaml", "r", encoding= "utf-8"))
    print(search_context_data)

    def setup_class(self):
        self.search = AppStart.start().enter_search()

    """读取外部yaml文件，传入参数"""
    @pytest.mark.parametrize("search_context", search_context_data)
    def test_search(self, search_context):
        self.search.input_search_context(search_context)

    """读取外部excel文件内容，传入参数"""
    def test_excel_search(self):
        self.search.input_excel_search_context()

    def teardown_class(self):
        AppStart.quit()
