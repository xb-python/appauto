import unittest
import uiautomator2 as u2
from loguru import logger
from phoneautoapp import AutoApp
from phoneautoweb import AutoWeb
from phoneautominiprogram import AutoMiniProgram
from phoneobject import PO
"""
用例层：存放用例
"""


class TestApp(unittest.TestCase):


    def setUp(self) -> None:
        self.phone = PO.getPhoneSerial()
        self.serial = self.phone.serial
        logger.info(f'测试之前的准备：链接手机:{self.serial}')
        logger.info('测试用例之前的准备：打开App')

    def tearDown(self) -> None:
        logger.info('测试用例之后的收尾：关闭App')
        PO.delUsePhone(self.serial)
        logger.info(f'测试之后的收尾：断开手机:{self.serial}')

    # @unittest.skip('直接跳过')
    def test_demo01(self):
        logger.info("第1个用例")
        self.androidPackage = 'com.tencent.mm'
        self.androidActivity = '.plugin.account.ui.ContactsSyncUI'
        AutoApp(self.phone).appClear(self.androidPackage)
        AutoApp(self.phone).appStart(f'{self.androidPackage}/{self.androidActivity}')
        AutoApp(self.phone).appWait(self.androidPackage)
        AutoApp(self.phone).signIn("wxid_8pa07s4ajq3l12", "abcd135790")
        AutoApp(self.phone).sendMessage2('https://www.baidu.com/')
        AutoWeb(self.phone).senftext()


    # @unittest.skipIf(1, '判断为真时跳过')
    def test_demo02(self):
        logger.info("第2个用例")
        self.androidPackage = 'com.android.chrome'
        AutoApp(self.phone).appClear(self.androidPackage)
        AutoApp(self.phone).appStart(self.androidPackage)
        AutoApp(self.phone).appWait(self.androidPackage)
        AutoApp(self.phone).chromeopenuel('https://www.baidu.com/')
        AutoWeb(self.phone).senftext('baidu')
        AutoWeb(self.phone).baiduinput('张无忌')
        AutoWeb(self.phone).openbaidubaike('张无忌')

    # @unittest.skipUnless(0, '判断为假时跳过')
    def test_demo03(self):
        """第三个用例"""
        logger.info("第3个用例")
        AutoApp(self.phone).openMiniProgram('魔卡百科')
        AutoMiniProgram(self.phone, '魔卡图鉴').miniprogram('酒吞童子')

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


if __name__ == '__main__':
    
    suite = unittest.TestSuite()
    suite.addTest(TestApp('test_demo10'))
    unittest.TextTestRunner().run(suite)