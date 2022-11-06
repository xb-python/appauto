import os
import time
import uiautomator2
from selenium import webdriver
from selenium.webdriver.common.by import By
from uiautomator2 import Direction


"""
APP自动化 执行层
"""

class AutoStep():

    def __init__(self, phone):
        self.phone = phone


    def appStart(self, androidPackage):
        os.popen(f' adb shell am start -W {androidPackage}')

    def appClear(self, androidPackage):
        self.phone.app_clear(androidPackage)

    def appWait(self, androidPackage):
        self.phone.app_wait(androidPackage)

    def appStop(self, androidPackage):
        self.phone.app_stop(androidPackage)

    def signIn(self, user, password):
        """微信登录"""
        self.phone(text='登录').click()
        self.phone(text='用微信号/QQ号/邮箱登录').click()
        self.phone(text='请填写微信号/QQ号/邮箱').click()
        self.phone(text='请填写微信号/QQ号/邮箱').send_keys(user)
        if self.phone.xpath('//*[@resource-id="com.tencent.mm:id/g6b"]/android.widget.EditText[1]').wait(timeout=3):
            self.phone.xpath('//*[@resource-id="com.tencent.mm:id/g6b"]/android.widget.EditText[1]').click()
        else:
            self.phone(text='请填写密码').click()
        self.phone.send_keys(password)
        self.phone(text='同意并登录').click()
        for i in range(10):
            time.sleep(3)
            if self.phone(text='暂不设置').wait(timeout=1):
                self.phone(text='暂不设置').click()
            elif self.phone(text='通讯录').wait(timeout=1):
                break
            time.sleep(2)
        self.phone(text='我').click()
        time.sleep(1)

    def sendMessage2(self, url):
        self.phone(text='通讯录').click()
        for i in range(1):
            if self.phone(text='文件传输助手').wait(timeout=0.5):
                self.phone(text='文件传输助手').click()
                time.sleep(2)
                self.phone(text='发消息').click()
                break
            self.phone.swipe_ext(Direction.UP, 0.8)
        else:
            self.phone.xpath('//*[@resource-id="com.tencent.mm:id/f15"]').click()
            self.phone.send_keys('文件传输助手')
            self.phone(resourceId='com.tencent.mm:id/kpm', text='文件传输助手').click()
            time.sleep(2)


        self.phone.xpath('//android.widget.EditText').click()
        self.phone.send_keys('http://debugxweb.qq.com/?inspector=true')
        self.phone(text='发送').click()
        time.sleep(1)
        self.phone.send_keys(url)
        self.phone(text='发送').click()
        time.sleep(1)

        self.phone(text='http://debugxweb.qq.com/?inspector=true').click()
        time.sleep(15)
        self.phone.press("back")
        time.sleep(2)
        for i in range(5):
            time.sleep(5)
            if self.phone(text=url).wait(timeout=1, exists=False):
                break
            self.phone(text=url).click()
        time.sleep(10)

    def chromeopenuel(self,url):
        self.phone.app_wait('com.android.chrome')
        self.phone.xpath('//*[@resource-id="com.android.chrome:id/url_bar"]').click()
        self.phone.clear_text()
        self.phone.send_keys(url)
        self.phone.press('enter')
        time.sleep(2)




    def searchMiniProgram(self):
        self.phone(resourceId='com.tencent.mm:id/f2s', text='微信').click()
        # self.phone(resourceId='com.tencent.mm:id/j5t').click()
        self.phone.swipe_ext(Direction.DOWN, 1)
        time.sleep(2)
        self.phone(text='搜索小程序').click(timeout=5)
        time.sleep(5)
        self.phone.send_keys('魔卡百科')
        time.sleep(2)
        self.phone.press("search")  # 点击搜索按键



if __name__ == '__main__':
    PA = PhoneAuto()
    # PA.searchMiniProgram()



