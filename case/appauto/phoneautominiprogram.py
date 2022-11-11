import time
from selenium.webdriver.common.by import By
from uiautomator2 import Direction
from webview import WebView


"""
webview自动化 执行层
"""

class AutoMiniProgram(WebView):

    def __init__(self, phone, text=None):
        super(AutoMiniProgram, self).__init__(phone)
        super(AutoMiniProgram, self).senftext(text)


    def miniprogram(self, text):
        self.driver.find_element(By.XPATH, f'//div[contains(text(),"搜索")]').click()
        textclear = self.driver.find_elements(By.XPATH, f'//wx-view[@class="search--iconfont search--icon-x"]')     # 判断 清空按钮是否存在
        if len(textclear) >= 1:
            textclear[0].click()

        self.phone.send_keys(text)
        self.senftext('魔卡图鉴')
        self.driver.find_element(By.XPATH, f'//wx-view[@data-index="0"]').click()   # S服

        time.sleep(1)
        # 判断 s服是否选中，选中则取消
        if self.driver.find_element(By.XPATH, f'//wx-view[@data-index="0"]').get_attribute('class') == 'search--item search--checked':
            self.driver.find_element(By.XPATH, f'//wx-view[@data-index="0"]').click()


        # 退出 输入框
        self.driver.find_element(By.XPATH, f'//wx-view[contains(text(),"取消")]').click()

        # 选择第一个搜索结果
        self.driver.find_element(By.XPATH, f'//wx-view[@class="child--__item"]').click()


if __name__ == '__main__':

    from phoneObject import PO
    phone =PO.getPhoneSerial()
    AutoMiniProgram(phone,'魔卡图鉴').miniprogram('酒吞童子')

