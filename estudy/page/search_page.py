import logging
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from utils.get_excel_data import GetExcelData
from utils.log import Logger

# 实例化对象
logger = Logger("search", "E:\\study\\Fork\\estudy\\estudy\\data\\search.log", filelevel=logging.INFO)


class Search(BasePage):
    # 需要读取的文件的路径
    path = "E:\\study\\Fork\\other_file\\test_search.xlsx"
    driver: webdriver = None

    def __init__(self, driver):
        super().__init__(driver)
        self.excel_data = GetExcelData(self.driver)

    # 搜索框
    _et_search_context = (By.ID, "com.intretech.readerx:id/edit_search")
    # 搜索结果中绘本分类的绘本二字
    _tv_book = "//android.widget.TextView[@text='绘本']"
    # 绘本书籍的查看更多
    _tv_more_books = (By.ID, "com.intretech.readerx:id/tv_search_books_more")
    # 绘本书籍列表
    _tv_book_list = "android.view.ViewGroup"
    _tv_book_title = (By.ID, "com.intretech.readerx:id/tv_search_title")
    # 专辑的查看更多
    _tv_more_blbum = (By.ID, "com.intretech.readerx:id/tv_search_album_more")
    # 曲目的查看更多
    _tv_more_song = (By.ID, "com.intretech.readerx:id/tv_search_song_more")

    # 输入搜索内容
    def input_search_context(self, search_context):
        self.find_element_id(self._et_search_context).clear()
        self.find_element_id(self._et_search_context).send_keys(search_context)
        # 点击键盘的回车按钮
        self.driver.press_keycode(66)
        # 隐藏键盘
        self.driver.hide_keyboard()
        time.sleep(1)
        try:
            self.find_element_xpath(self._tv_book)
        except:
            logger.info(search_context)
        else:
            return True

    # 输入搜索内容，使用pandas读取excel文件内容
    def input_excel_search_context(self):
        # 获取excel文件的内容
        search_contexts = self.excel_data.pd_read_excel(self.path)
        # 获取到的内容是一个数组，遍历数组
        for context in search_contexts:
            self.find_element_id(self._et_search_context).clear()
            self.find_element_id(self._et_search_context).send_keys(context)
            # 点击键盘的回车按钮
            self.driver.press_keycode(66)
            # 隐藏键盘
            self.driver.hide_keyboard()
            # time.sleep(0.5)
            try:
                self.find_element_xpath(self._tv_book)
            except:
                logger.info(context)
                # print(context)
            # 使用return True会跳出for循环
            # else:
            #     return True
