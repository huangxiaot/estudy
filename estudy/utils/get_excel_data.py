# 封装获取外部excel文件内容
import pandas as pd


class GetExcelData:
    def __init__(self, path: ''):
        self.path = path

    def pd_read_excel(self, path):
        # 读取excel文件中的子表book的第二列的内容，列下表从0开始(不包括列名)
        st_data = pd.read_excel(path, sheet_name="book", usecols=[1])
        # 读取book表的第一列数据(list形式)
        data = st_data.values
        # print(data)
        return data


# 测试函数，执行过程中可以注释
# if __name__ == '__main__':
#     path = "E:\\study\\Fork\\other_file\\test_searchs.xlsx"
#     a = GetExcelData(path)
#     a.pd_read_excel(path)
