import time
from page.base_page import BasePage
from page.search_page import Search


class ReadingPartnerPage(BasePage):
    _tv_search = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView"

    def enter_search(self):
        time.sleep(1)
        self.find_element_xpath(self._tv_search).click()
        return Search(self.driver)
