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


    def miniprogram(self, text, by, value=None):
        # tars = self.driver.find_elements(by, value)
        # print('tars:', len(tars))
        # tar = tars[-1]
        # tar.click()

        # 小程序 输入 存在问题，还在测试中
        self.senftext()

        tar = self.driver.find_element(By.XPATH, '//wx-input[@placeholder="输入关键词搜索"]')
        js = f'arguments[0].value="{text}";arguments[0].cursor="{len(text)}";'
        self.driver.execute_script(js, tar)
        print('value:', tar.get_attribute('value'))
        print('cursor:', tar.get_attribute('cursor'))
        print('tar:',tar[0].get_attribute('role'))
        tar[0].send_keys(text)






if __name__ == '__main__':

    from phoneObject import PO
    phone =PO.getPhoneSerial()
    # AutoMiniProgram(phone,'魔卡图鉴').miniprogram('123456789', By.XPATH, f'//wx-input[@placeholder="搜索"]')
    # AutoMiniProgram(phone,'贴吧').miniprogram('酒吞童子', By.XPATH, f'//wx-text/span[contains(text(),"游戏")]')
    AutoMiniProgram(phone,'贴吧').miniprogram('酒吞童子', By.XPATH, f'//wx-text/span[contains(text(),"输入关键词")]')

