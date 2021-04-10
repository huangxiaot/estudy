# 该类主要用于截图和保存图片
import glob
import os
import time
from selenium.webdriver.common.by import By
from page.base_page import BasePage


class FileManager(BasePage):
    count = 1

    # 宝贝信息页面宝贝头像显示
    _iv_baby_info_portrait_display = (By.ID, "com.intretech.readerx:id/img_baby_detail_avatar")
    # 我的页面宝贝头像显示
    _iv_my_page_baby_portrait_display = (By.ID, "com.intretech.readerx:id/img_person_portrait")

    """整个页面截图"""
    def get_entire_screen(self):
        # 截图将图片保存至固定的位置
        img_folder = 'E:\\study\\Fork\\estudy\\estudy\\image\\'
        # 截图的文件名组成
        times = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # 图片存储位置+文件名
        screen_save_path = img_folder + times + '.jpg'
        # 截取当前页面的整张图片，并保存在已定义的存储位置和规定的文件名
        self.driver.get_screenshot_as_file(screen_save_path)
        # # 实例化ImageRecognition，传入需要识别的图片位置
        # ir = ImageRecognition(screen_save_path)
        # ir.ocr()

    """截取页面中特定区域的图片"""
    def get_part_screen(self):
        # 截图将图片保存至固定的位置
        img_folder = 'E:\\study\\Fork\\estudy\\estudy\\image\\'
        # 截图的文件名组成
        times = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # 图片存储位置+文件名
        screen_save_path = img_folder + times + '.jpg'
        # 截取当前页面的整张图片，并保存在已定义的存储位置和规定的文件名
        self.find_element_id(self._iv_baby_info_portrait_display).screenshot(screen_save_path)
        # 实例化ImageRecognition，传入需要识别的图片位置
        # ir = ImageRecognition(screen_save_path)
        # ir.ocr()
        # return screen_save_path

    """截取宝贝信息页面宝贝头像"""
    def get_baby_info_baby_portrait(self):
        # 截图将图片保存至固定的位置
        img_folder = 'E:\\study\\Fork\\estudy\\estudy\\image\\'
        # 截图的文件名组成
        name = 'test_baby_info_baby_portrait' + str(self.count)
        self.count = self.count + 1
        baby_portrait_screen_save_path = img_folder + name + '.jpg'
        self.find_element_id(self._iv_baby_info_portrait_display).screenshot(baby_portrait_screen_save_path)

    """截取我的页面宝贝头像"""
    def get_my_page_baby_portrait(self):
        # 截图将图片保存至固定的位置
        img_folder = 'E:\\study\\Fork\\estudy\\estudy\\image\\'
        # 截图的文件名组成
        name = 'test_my_page_baby_portrait' + str(self.count)
        self.count = self.count + 1
        baby_portrait_screen_save_path = img_folder + name + '.jpg'
        self.find_element_id(self._iv_my_page_baby_portrait_display).screenshot(baby_portrait_screen_save_path)

    """删除文件中的图片"""
    def delete_all_image(self):
        path = 'E:\\study\\Fork\\estudy\\estudy\\image\\'
        for infile in glob.glob(os.path.join(path, '*.jpg')):
            os.remove(infile)

    # # 获取文件目录（demo）
    # def get_file_path(self):
    #     # 上上级目录
    #     contents = os.path.abspath(os.path.join(os.getcwd(), "../.."))
    #     print(contents)
    #     # 上级目录
    #     content = os.path.abspath(os.path.join(os.getcwd(), ".."))
    #     print(content)
    #     # 当前目录
    #     c = os.getcwd()
    #     print(c)

    # 创建文件夹（存在错误）
    # img_folder = os.path.abspath(os.path.join(os.getcwd(), ".."))[:-4] + '\\image\\'
    # print(img_folder)
