import unittest
from loguru import logger
from phoneauto import PhoneAuto
from phoneObject import delUsePhone

"""
用例层：存放用例
"""


class TestApp(unittest.TestCase):


    def setUp(self) -> None:
        self.PhoneAutoObject = PhoneAuto()
        self.serial = self.PhoneAutoObject.serial
        logger.info(f'测试之前的准备：链接手机:{self.serial}')
        self.PhoneAutoObject.appClear()
        self.PhoneAutoObject.appStart()
        self.PhoneAutoObject.appWait()
        logger.info('测试用例之前的准备：打开App')

    def tearDown(self) -> None:
        logger.info('测试用例之后的收尾：关闭App')
        # self.PhoneAutoObject.appStop()
        delUsePhone(self.serial)
        logger.info(f'测试之后的收尾：断开手机:{self.serial}')

    # @unittest.skip('直接跳过')
    def test_demo01(self):
        logger.info("第1个用例")
        self.PhoneAutoObject.caseid = 'demo01'
        self.PhoneAutoObject.signIn("wxid_8pa07s4ajq3l12", "abcd135790")
        self.PhoneAutoObject.sendMessage2('https://www.baidu.com/')

    # @unittest.skipIf(1, '判断为真时跳过')
    def test_demo02(self):
        logger.info("第2个用例")
        self.PhoneAutoObject.caseid = 'demo02'
        self.PhoneAutoObject.signIn("wxid_uhp0b5846yd112", "abcd135790")
        self.PhoneAutoObject.sendMessage2('https://www.baidu.com/')
        self.PhoneAutoObject.searchMiniProgram()


    # @unittest.skipUnless(0, '判断为假时跳过')
    def test_demo03(self):
        """第三个用例"""
        logger.info("第3个用例")
        self.PhoneAutoObject.caseid = 'demo03'
        self.PhoneAutoObject.signIn("wxid_yzhuktp4u9ms12", "abcd135790")
        self.PhoneAutoObject.sendMessage2('https://www.sohu.com/')


    def test_demo04(self):
        """第4个用例"""
        logger.info("第4个用例")
        self.PhoneAutoObject.caseid = 'demo04'
        self.PhoneAutoObject.signIn("wxid_fjejxkbn3u1212", "abcd135790")
        self.PhoneAutoObject.sendMessage2('https://www.qq.com/')


    def test_demo05(self):
        """第5个用例"""
        logger.info("第5个用例")
        self.PhoneAutoObject.caseid = 'demo05'
        self.PhoneAutoObject.signIn("wxid_tk6q6ng00ovf12", "abcd135790")
        self.PhoneAutoObject.sendMessage2('https://www.163.com/')


    def test_demo06(self):
        """第6个用例"""
        logger.info("第6个用例")
        self.PhoneAutoObject.caseid = 'demo06'
        self.PhoneAutoObject.signIn("wxid_p3048qz1g6wl12", "abcd135790")
        self.PhoneAutoObject.sendMessage2('https://www.jd.com/')


    def test_demo07(self):
        """第7个用例"""
        logger.info("第7个用例")
        self.PhoneAutoObject.caseid = 'demo07'
        self.PhoneAutoObject.signIn("wxid_meamyvg29y8r12", "abcd135790")
        self.PhoneAutoObject.sendMessage2('https://p4psearch.1688.com/')


    def test_demo08(self):
        """第8个用例"""
        logger.info("第8个用例")
        self.PhoneAutoObject.caseid = 'demo08'
        self.PhoneAutoObject.signIn("wxid_xu86yuevaaea12", "abcd135790")
        self.PhoneAutoObject.sendMessage2('https://www.ctrip.com/')


    def test_demo09(self):
        """第9个用例"""
        logger.info("第9个用例")
        self.PhoneAutoObject.caseid = 'demo09'
        self.PhoneAutoObject.signIn("wxid_2eu537xof6jx12", "abcd135790")
        self.PhoneAutoObject.sendMessage2('https://www.iqiyi.com/')


    def test_demo10(self):
        """第10个用例"""
        logger.info("第10个用例")
        self.PhoneAutoObject.caseid = 'demo10'
        self.PhoneAutoObject.signIn("wxid_kjztu4s6a6hi12", "abcd135790")
        self.PhoneAutoObject.searchMiniProgram()

