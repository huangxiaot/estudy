# 搜索操作
import pytest
import yaml
from page.start import AppStart


class TestSearch:
    search_context_data = yaml.safe_load(open("E:\\study\\Fork\\estudy\\estudy\\data\\search.yaml", "r", encoding= "utf-8"))
    print(search_context_data)

    def setup_class(self):
        self.search = AppStart.start().enter_search()

    # 搜索
    @pytest.mark.parametrize("search_context", search_context_data)
    def test_search(self, search_context):
        self.search.input_search_context(search_context)

    def teardown_class(self):
        AppStart.quit()
