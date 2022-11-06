import os
import platform
from loguru import logger
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from configs import *


"""
webview自动化 执行层
"""

class AutoWebView:

    def __init__(self, phone):
        self.phone = phone
        self.serial = phone.serial
        app = phone.current_app()
        optionsData = {
            'androidPackage': app['package'],
            'androidDeviceSerial': self.serial,
            'androidUseRunningApp': True,
            'androidProcess': self.getPidName(),
        }
        logger.info(f'options:{optionsData}')
        options = webdriver.ChromeOptions()
        options.add_experimental_option('androidPackage', optionsData['androidPackage'])
        options.add_experimental_option('androidDeviceSerial', optionsData['androidDeviceSerial'])
        options.add_experimental_option('androidUseRunningApp', optionsData['androidUseRunningApp'])
        options.add_experimental_option('androidProcess', optionsData['androidProcess'])

        # version 手机驱动版本，需指定
        path = ChromeDriverManager(path='auto/', version=CHROMEDRIVERVERSION).install()
        self.driver = webdriver.Chrome(executable_path=path, options=options)



    def getPidName(self):

        pidcommand = f'adb -s {self.serial} shell dumpsys activity top| findstr ACTIVITY' \
            if platform.system() == "Windows" else \
            f'adb -s {self.serial} shell dumpsys activity top| grep ACTIVITY'
        logger.info(pidcommand)
        pidcommandtext = os.popen(pidcommand)
        pidText = pidcommandtext.read()
        logger.info(f'pidText: {pidText}')
        pid = (pidText.split('pid=')[-1]).split('\n')[0]
        logger.info(f'pid: {pid}')

        pidnamecommand = f'adb -s {self.serial} shell ps {pid}'
        logger.info(pidcommand)
        pidnamecommandtext = os.popen(pidnamecommand)
        pidNameText = pidnamecommandtext.read()
        logger.info(f'adbshellPidNameText: {pidNameText}')
        pidName = (pidNameText.split(' ')[-1]).split('\n')[0]
        logger.info(f'pidName: {pidName}')
        return pidName


    def senftext(self, url=None):
        """
        切换到对应url窗口，未指定
        """
        windows = self.driver.window_handles  # 获取所有窗口
        if url:
            for window in windows:
                self.driver.switch_to.window(window)  # 切换窗口
                logger.debug(f'window: {window}, windowUrl: {self.driver.current_url}')  # 打印窗口和对应url
                if url in self.driver.current_url:
                    return True     # 切换成功
            else:
                return False     # 切换失败
        else:
            pass

    def baiduinput(self, keyWord):
        self.driver.find_element(By.XPATH, '//input[@placeholder="输入搜索词"]').send_keys(keyWord)
        self.phone.press("enter")

    def openbaidubaike(self, keyWord):
        self.driver.find_element(By.XPATH, f'//div[@class="c-title"]/em[contains(text(),"{keyWord}")]').click()


if __name__ == '__main__':

    from phoneObject import PO
    phone =PO.getPhoneSerial()
    AutoWebView(phone).senftext('www.baidu.com')
    AutoWebView(phone).baiduinput('张无忌')
    AutoWebView(phone).openbaidubaike('张无忌')