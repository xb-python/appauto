import os
import time
import uiautomator2
from selenium import webdriver
from selenium.webdriver.common.by import By
from uiautomator2 import Direction
from phoneautowebview import PhoneAutoWebView


"""
APP自动化 执行层
"""

class PhoneAuto(PhoneAutoWebView):


    def appStart(self):
        self.phone.app_start('com.tencent.mm')

    def appClear(self):
        self.phone.app_clear('com.tencent.mm')

    def appWait(self):
        self.phone.app_wait('com.tencent.mm')

    def appStop(self):
        self.phone.app_stop('com.tencent.mm')

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
        self.phone.screenshot(f'./img/{self.caseid}_signIn.jpg')

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
        self.phone.screenshot(f'./img/{self.caseid}_sendMessage2.jpg')

    def start_chrome(self,url):
        os.popen(f' adb shell am start -W com.android.chrome')
        self.phone.app_wait('com.android.chrome')
        self.phone.xpath('//*[@resource-id="com.android.chrome:id/url_bar"]').click()
        self.phone.clear_text()
        self.phone.send_keys(url)
        self.phone.press('enter')
        time.sleep(2)


        """
        以下 Chrome 选项适用于 Chrome 和 Web View 应用：
        androidPackage：Chrome 或 WebView 应用的程序包名称。
        androidDeviceSerial：（可选）用于启动应用程序的设备序列号（请参阅下面的“多个设备”部分）。
        androidUseRunningApp：（可选）附加到已在运行的应用程序，而不是使用清晰的数据目录启动应用程序。
        以下功能仅适用于 Web 视图应用。
        androidActivity：托管 Web View 的活动的名称。
        androidProcess：（可选）托管 WebView 的活动的进程名称（由 ps 给出）。如果未给出，则假定进程名称与androidPackage 相同。 
        """
        path = os.getcwd() + '/chromedriver2'

        app = self.phone.app_current()
        package = app.get('package')
        options = webdriver.ChromeOptions()
        options.add_experimental_option('androidPackage', package)
        options.add_experimental_option('androidDeviceSerial', self.phone.serial)
        options.add_experimental_option('androidUseRunningApp', True)
        driver = webdriver.Chrome(executable_path=path, options=options)

        driver.find_elements(By.XPATH, '//*[@id="msKeyWord"]')[0].send_keys('诺基亚')
        driver.quit()

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



