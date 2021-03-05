# 封装日志类
import logging


class Logger:
    def __init__(self, logname, filename, filelevel):
        # LoggerName：实例化对象的名字  FileName:外部文件名  FileLevel:设置文件日志输出的级别
        self.logger = logging.getLogger(logname)
        # 设置日志的级别
        self.logger.setLevel(logging.INFO)
        # 设置日志的输出格式
        fmt = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

        # 借助handle将日志输出到文件中
        fh = logging.FileHandler(filename, encoding='utf-8')
        fh.setLevel(filelevel)

        # 配置logger
        fh.setFormatter(fmt)

        # 给logger添加handle
        self.logger.addHandler(fh)

    # 日志的级别为debug
    def debug(self, message):
        self.logger.debug(message)

    # 日志的级别为info
    def info(self, message):
        self.logger.info(message)

    # 日志的级别为warn
    def warn(self, message):
        self.logger.warning(message)

    # 日志的级别为error
    def error(self, message):
        self.logger.error(message)

    # 日志的级别为critical
    def critical(self, message):
        self.logger.critical(message)


# if __name__ == "__main__":
#     logger = Logger("search", "E:\\study\\Fork\\estudy\\estudy\\data\\search.log", filelevel=logging.INFO)
#     logger.debug("debug message!")
#     logger.info("info message!")
#     logger.warn("warning message!")
#     logger.error("error message!")
#     logger.critical("critical message!")
