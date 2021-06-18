import logging
import time
import serial as serial
from utils.log import Logger


# 实例化日志对象
file_path = r"E:\study\Fork\estudy\estudy\data\devices_upgrade.log"
logger = Logger("devices_upgrade", file_path, filelevel=logging.INFO)
file_path_backups = r"E:\study\Fork\estudy\estudy\data\devices_upgrade_backups.log"
logger_backups = Logger("devices_upgrade", file_path_backups, filelevel=logging.INFO)


class DevicesUpgrade:

    count_success = 0  # 升级成功的次数
    count_fail = 0  # 升级失败的次数

    def __init__(self, serial_port: '', baud_rate: ''):
        self.serial_port = serial_port
        self.baud_rate = baud_rate

    # 台灯强制升级
    def sf1_constraint_upgrade(self):
        # 设置打开的串口和波特率
        ser = serial.Serial(self.serial_port, self.baud_rate, timeout=0.5)
        print("打开的串口是：${0}" .format(ser.name))
        """ 台灯强制升级的指令"""
        # 版本号降到119
        ser.write(("echo 119 > /app/info/version.inf" + '\n').encode('utf-8'))
        time.sleep(0.5)
        # 查看版本号
        ser.write(("cat /app/info/version.inf" + '\n').encode('utf-8'))
        time.sleep(0.5)
        # 重启检测版本号升级
        ser.write(("reboot" + '\n').encode('utf-8'))
        is_found = False  # 默认没找到升级成功或升级失败的字符串
        while is_found is not True:
            # 输出全部log
            full_data = ser.readall()
            # 将输出的log根据换行符切割
            split_data = full_data.splitlines()
            # 将切割好的log循环遍历输出到文件中
            for data in split_data:
                # logger.info(data)
                logger_backups.info(data)
            # 版本号修改成功
            if self.check_version():
                # 升级成功
                if self.check_success():
                    DevicesUpgrade.count_success += 1
                    print("升级成功次数为：%s" % DevicesUpgrade.count_success)
                    is_found = True
                # 升级失败
                elif self.check_fail():
                    DevicesUpgrade.count_fail += 1
                    print("升级失败次数为：%s" % DevicesUpgrade.count_fail)
                    is_found = True
            # 版本号修改失败
            else:
                print("版本号修改失败")
                is_found = True

    # 台灯静默升级
    def sf1_silent_upgrade(self):
        # 设置打开的串口和波特率
        ser_silent = serial.Serial(self.serial_port, self.baud_rate, timeout=0.5)
        print("打开的串口是：${0}".format(ser_silent.name))
        # 判断台灯是否关机

    # 判断版本号是否修改成功
    def check_version(self):
        version = "'119'"
        """读取日志文件，并查找版本号"""
        with open(file_path) as temp:
            datafile = temp.readlines()
        for line in datafile:
            if version in line:
                return True  # edit version success
        return False  # edit version fail

    # 判断设备升级成功
    def check_success(self):
        upgrade_success = "[CMD] Set file name:/app/prompt/update_succ.mp3."
        """读取日志文件，并查找升级成功的日志"""
        with open(file_path) as temp:
            datafile = temp.readlines()
        for line in datafile:
            if upgrade_success in line:
                print("升级成功")
                return True  # The string is found
        return False  # The string does not exist in the file

    # 判断设备升级失败
    def check_fail(self):
        upgrade_fail = "[CMD] Set file name:/app/prompt/update_fail.mp3"
        """读取日志文件，并查找升级失败的日志"""
        with open(file_path) as temp:
            datafile = temp.readlines()
        for line in datafile:
            if upgrade_fail in line:
                print("升级失败")
                return True     # The string is found
        return False  # The string does not exist in the file

    # 清除devices_upgrade.log文件内容
    def clear_log_data(self):
        with open(file_path, 'w+', encoding='utf-8') as log_file:
            log_file.truncate(0)
        print("log清除成功")


if __name__ == '__main__':
    devices_upgrade = DevicesUpgrade("COM14", str(115200))
    for i in range(3):
        devices_upgrade.clear_log_data()
        devices_upgrade.sf1_constraint_upgrade()

    # 打印log的时间戳
    # every_date = time.strftime('%Y-%m-%d')
    # every_time = time.strftime('%H:%M:%S')
    # log_data = every_date + ' ' + every_time + ' ' + str(data)
    # print(log_data)

    # 将log写入到excel文件
    # def write_excel_xlsx(self):
    #     every_date, every_time, data = self.sf1_upgrade()
    #     wb = openpyxl.Workbook()
    #     ws = wb.active
    #     title_data = ['date', 'time', 'log']
    #     # 写入第一行数据，行号和列号都从1开始计数
    #     for i in range(len(title_data)):
    #         ws.cell(1, i + 1, title_data[i])
    #     # 写入第一列数据，因为第一行已经有数据了，i+2
    #     for j in range(len(every_date)):
    #         ws.cell(j + 2, 1, every_date[j])
    #         # 写入第二列数据
    #         for k in range(len(every_time)):
    #             ws.cell(k + 2, 2, every_time[k])
    #             # 写入第二列数据
    #             for p in range(len(data)):
    #                 ws.cell(p + 2, 2, data[p])
    #     wb.save(filename="E:\\others\\log\\test.xlsx")

    # def check_success_upgrade(self):
    #     success_log = re.findall(r'[CMD] Set file name:/app/prompt/update_succ.mp3.', str(data))
    #     if data == success_log:
    #         is_open = False
    #         print(success_log)
    #     return every_time, str(data)
