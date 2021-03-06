import logging
import time

from appium import webdriver
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from utils.log import Logger

# 实例化对象
logger = Logger("search", "E:\\study\\Fork\\estudy\\estudy\\data\\search.log", filelevel=logging.INFO)


class Search(BasePage):
    driver: webdriver = None

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
