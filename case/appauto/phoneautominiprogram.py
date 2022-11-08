import time
from selenium.webdriver.common.by import By
from webview import WebView


"""
webview自动化 执行层
"""

class AutoMiniProgram(WebView):

    def __init__(self, phone, text=None):
        super(AutoMiniProgram, self).__init__(phone)
        super(AutoMiniProgram, self).senftext(text)


    def miniprogram(self, text):
        self.driver.find_element(By.XPATH, f'//wx-input[@placeholder="搜索"]').click()
        self.senftext()
        self.phone.send_keys(text)
        self.phone.press("search")  # 点击搜索按键
        self.phone.press('enter')







if __name__ == '__main__':

    from phoneObject import PO
    phone =PO.getPhoneSerial()
    AutoMiniProgram(phone,'魔卡图鉴').miniprogram('酒吞童子')

