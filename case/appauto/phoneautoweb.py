import time
from selenium.webdriver.common.by import By
from autowebview import AutoWebView


"""
webview自动化 执行层
"""

class AutoWeb(AutoWebView):

    def __init__(self, phone, text=None):
        super(AutoWeb, self).__init__(phone)
        super(AutoWeb, self).senftext(text)
        self.input_box = {'type': By.XPATH, 'value': '//input[@placeholder="输入搜索词"]'}



    def baiduinput(self, keyWord):
        self.find_element(self.input_box).send_keys(keyWord)
        time.sleep(1)
        self.phone.press("enter")

    def openbaidubaike(self, keyWord):
        self.driver.find_element(By.XPATH, f'//div[@class="c-title"]/em[contains(text(),"{keyWord}")]').click()


if __name__ == '__main__':

    from phoneobject import PO
    phone =PO.getPhoneSerial()
    AutoWeb(phone, 'baidu')
    AutoWeb(phone).baiduinput('张无忌')
    AutoWeb(phone).openbaidubaike('张无忌')