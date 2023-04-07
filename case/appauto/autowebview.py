import os
import platform
from loguru import logger
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from configs import CHROMEDRIVERVERSION


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
        path = ChromeDriverManager(path='driver/', version=CHROMEDRIVERVERSION).install()
        self.driver = webdriver.Chrome(executable_path=path, options=options)
        self.driver.implicitly_wait(3)

    def getPidName(self):
        pidcommand = f'adb -s {self.serial} shell dumpsys activity top| {"findstr" if platform.system() == "Windows" else "grep"} ACTIVITY'
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

    def senftext(self, text=None):
        """
        切换到对应url窗口，未指定
        """
        windows = self.driver.window_handles  # 获取所有窗口
        [logger.info(f'当前存在的窗口有：{win}') for win in windows]

        if not text:
            self.driver.switch_to.window(windows[-1])  # 切换最新窗口
            logger.debug(f'window: {windows[-1]}, windowUrl: {self.driver.current_url}')  # 打印窗口和对应url
            logger.debug(f'切换成功')
            return self

        for window in windows:
            self.driver.switch_to.window(window)  # 切换窗口
            logger.debug(f'window: {window}, windowUrl: {self.driver.current_url}')  # 打印窗口和对应url
            if text in self.driver.current_url or text in self.driver.execute_script('return document.documentElement.outerHTML'):
                logger.debug(f'切换成功')
                return self
        else:
            logger.error(f'切换失败，未切换到含有{text}的页面')

    def find_element(self, type_value):
        return self.driver.find_element(type_value['type'], type_value['value'])

    def find_elements(self, type_value):
        return self.driver.find_elements(type_value['type'], type_value['value'])
