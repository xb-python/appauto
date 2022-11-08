import time
from selenium.webdriver.common.by import By
from webview import WebView


"""
webview自动化 执行层
"""

class AutoWebView(WebView):

    def __init__(self, phone, text=None):
        super(AutoWebView, self).__init__(phone)
        super(AutoWebView, self).senftext(text)

    def baiduinput(self, keyWord):
        self.driver.find_element(By.XPATH, '//input[@placeholder="输入搜索词"]').send_keys(keyWord)
        time.sleep(1)
        self.phone.press("enter")

    def openbaidubaike(self, keyWord):
        self.driver.find_element(By.XPATH, f'//div[@class="c-title"]/em[contains(text(),"{keyWord}")]').click()


if __name__ == '__main__':

    from phoneObject import PO
    phone =PO.getPhoneSerial()
    AutoWebView(phone, 'baidu')
    AutoWebView(phone).baiduinput('张无忌')
    AutoWebView(phone).openbaidubaike('张无忌')