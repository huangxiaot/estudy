# APP参数配置
from appium import webdriver
from page.login_page import LoginPage
from page.reading_partner_page import ReadingPartnerPage


class AppStart:
    # 声明driver对象事属于webdriver库里面的
    driver: webdriver = None

    @classmethod
    def start(cls):
        caps = {"platformName": "Android",
                "deviceName": "000002b74cd8494e",
                "platforVersion": "9",
                "appPackage": "com.intretech.readerx",
                "appActivity": "com.intretech.readerx.ui.WelcomeActivity",
                "autoGrantPermissions": "true",
                "automationName": "UiAutomator2",
                "noReset": True
                }

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(5)
        return ReadingPartnerPage(cls.driver)
        # return LoginPage(cls.driver)

    # 退出app
    @classmethod
    def quit(cls):
        cls.driver.quit()
