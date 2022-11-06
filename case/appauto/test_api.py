import unittest
import uiautomator2 as u2
from loguru import logger
from phoneauto import AutoStep
from phoneautowebview import AutoWebView
from phoneObject import getPhoneSerial, delUsePhone
"""
用例层：存放用例
"""


class TestApp(unittest.TestCase):


    def setUp(self) -> None:
        self.phone = u2.connect(getPhoneSerial())
        logger.info(f'测试之前的准备：链接手机:{self.phone.serial}')
        logger.info('测试用例之前的准备：打开App')

    def tearDown(self) -> None:
        logger.info('测试用例之后的收尾：关闭App')
        delUsePhone(self.phone.serial)
        logger.info(f'测试之后的收尾：断开手机:{self.phone.serial}')

    # @unittest.skip('直接跳过')
    def test_demo01(self):
        logger.info("第1个用例")
        self.androidPackage = 'com.tencent.mm'
        AutoStep(self.phone).appClear(self.androidPackage)
        AutoStep(self.phone).appStart(self.androidPackage)
        AutoStep(self.phone).appWait(self.androidPackage)
        AutoStep(self.phone).signIn("wxid_8pa07s4ajq3l12", "abcd135790")
        AutoStep(self.phone).sendMessage2('https://www.baidu.com/')
        AutoWebView(self.phone).senftext()


    # @unittest.skipIf(1, '判断为真时跳过')
    def test_demo02(self):
        logger.info("第2个用例")
        self.androidPackage = 'com.android.chrome'
        AutoStep(self.phone).appClear(self.androidPackage)
        AutoStep(self.phone).appStart(self.androidPackage)
        AutoStep(self.phone).appWait(self.androidPackage)
        AutoStep(self.phone).chromeopenuel('https://www.baidu.com/')
        AutoWebView(self.phone).senftext('baidu')
        AutoWebView(self.phone).baiduinput('张无忌')
        AutoWebView(self.phone).openbaidubaike('张无忌')

    # @unittest.skipUnless(0, '判断为假时跳过')
    def test_demo03(self):
        """第三个用例"""
        logger.info("第3个用例")


    def test_demo04(self):
        """第4个用例"""
        logger.info("第4个用例")



    def test_demo05(self):
        """第5个用例"""
        logger.info("第5个用例")



    def test_demo06(self):
        """第6个用例"""
        logger.info("第6个用例")



    def test_demo07(self):
        """第7个用例"""
        logger.info("第7个用例")



    def test_demo08(self):
        """第8个用例"""
        logger.info("第8个用例")



    def test_demo09(self):
        """第9个用例"""
        logger.info("第9个用例")



    def test_demo10(self):
        """第10个用例"""
        logger.info("第10个用例")
