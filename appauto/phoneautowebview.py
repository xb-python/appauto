import os
import time
import uiautomator2
from loguru import logger
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from phoneObject import getPhoneSerial

"""
webview自动化 执行层
"""

class PhoneAutoWebView:

    def __init__(self, serial=getPhoneSerial()):
        self.serial = serial
        self.phone = uiautomator2.connect(serial)
        self.caseid = ''


    def webviewauto(self):
        # 返回当前webview页面的driver对象
        """
        以下 Chrome 选项适用于 Chrome 和 Web View 应用：
        androidPackage：Chrome 或 WebView 应用的程序包名称。
        androidDeviceSerial：（可选）用于启动应用程序的设备序列号（请参阅下面的“多个设备”部分）。
        androidUseRunningApp：（可选）附加到已在运行的应用程序，而不是使用清晰的数据目录启动应用程序。
        以下功能仅适用于 Web 视图应用。
        androidActivity：托管 Web View 的活动的名称。
        androidProcess：（可选）托管 WebView 的活动的进程名称（由 ps 给出）。如果未给出，则假定进程名称与androidPackage 相同。 
        """

        app = self.phone.current_app()
        optionsData = {
            'androidPackage': app['package'],
            'androidDeviceSerial': self.serial,
            'androidUseRunningApp': True,
            'androidProcess': self.getPidName(),
        }
        logger.info(f'options:{optionsData}')
        options = webdriver.ChromeOptions()
        options.add_experimental_option('androidPackage', optionsData['androidPackage'])  # 指定应用名
        options.add_experimental_option('androidDeviceSerial', optionsData['androidDeviceSerial'])  # 指定设备
        options.add_experimental_option('androidUseRunningApp', optionsData['androidUseRunningApp'])  # 使用已打开的引用
        options.add_experimental_option('androidProcess', optionsData['androidProcess'])    # 指定进程名

        # version 手机驱动版本，需指定
        path = ChromeDriverManager(path='./', version="100.0.4896.60").install()
        self.driver = webdriver.Chrome(executable_path=path, options=options)
        return self.driver

    def getPidName(self, serial=None):
        """
        获取当前页面的进程信息
        Mac：adb shell dumpsys activity top| grep ACTIVITY
        Windows：adb shell dumpsys activity top| findstr ACTIVITY
        通过进程号获取进程名：adb shell ps pid(例：adb shell ps 1716)
        return: 当前页面的进程名称
        """
        serial = serial if serial else self.serial
        if serial:
            logger.info(f'adb -s {serial} shell dumpsys activity top| grep ACTIVITY')
            adbshellPid = os.popen(f'adb -s {serial} shell dumpsys activity top| grep ACTIVITY')
        else:
            logger.info(f'adb shell dumpsys activity top| grep ACTIVITY')
            adbshellPid = os.popen(f'adb shell dumpsys activity top| grep ACTIVITY')

        adbshellPidText = adbshellPid.read()
        logger.info(f'PidText: {adbshellPidText}')
        pid = (adbshellPidText.split('pid=')[-1]).split('\n')[0]
        logger.info(f'pid: {pid}')

        if serial:
            logger.info(f'adb -s {serial} shell ps {pid}')
            adbshellPidName = os.popen(f'adb -s {serial} shell ps {pid}')
        else:
            logger.info(f'adb shell ps {pid}')
            adbshellPidName = os.popen(f'adb shell ps {pid}')

        adbshellPidNameText = adbshellPidName.read()
        logger.info(f'adbshellPidNameText: {adbshellPidNameText}')
        pidName = (adbshellPidNameText.split(' ')[-1]).split('\n')[0]
        logger.info(f'pidName: {pidName}')

        return pidName


    def senftext(self, driver=None):
        driver = driver if driver else self.driver
        """
        自定义步骤
        获取webview对象后，可以像操作chrome一样操作webview
        """
        windows = driver.window_handles  # 获取所有窗口
        for window in windows:
            driver.switch_to.window(window)  # 切换窗口
            print('window:', window, 'windowUrl:', driver.current_url)  # 打印窗口和对应url
            if 'baidu' in driver.current_url:
                break

        driver.find_element(By.XPATH, '//input[@placeholder="输入搜索词"]').send_keys('张无忌')

if __name__ == '__main__':

    paw = PhoneAutoWebView()
    paw.senftext(paw.webviewauto())
    paw.senftext()
