import os
import time
from loguru import logger
import threading
import uiautomator2 as u2
from configs import *



class PhoneObject:

    def __init__(self):
        # 定义全局变量，储存已分配的手机序列号和分配时间
        # UsePhoneList = {'serial': serial, 'useTime': time}
        self.UsePhoneList = []
        self.LOCK = threading.Lock()


    def getPhoneSerial(self):
        # 获取一个可用设备

        usableSerial = {'serial': None, 'time': None}
        for i in range(100):

            self.delBreakPhone()     # 清理 不可用设备

            with self.LOCK:
                serialList = self.adbDevicesPhone()
                useSerialList = [UsePhone['serial'] for UsePhone in self.UsePhoneList]  # 获取已分配的设备序列号列表

                for serial in serialList:
                    if not serial in useSerialList:     # 判断设备是否已被分配
                        usableSerial['serial'] = serial
                        usableSerial['time'] = time.time()
                        break

                if usableSerial['serial']:
                    self.UsePhoneList.append(usableSerial)
                    logger.debug(f'已分配该设备: {usableSerial}')
                    break

            time.sleep(5)
            logger.info(f'无可用手机等待中,已等待{i * 5}秒')

        return u2.connect(usableSerial['serial'])


    def delUsePhone(self, serial):
        # 在已分配设备列表中删除指定设备

        with self.LOCK:

            for UsePhone in self.UsePhoneList:

                if UsePhone['serial'] == serial:
                    self.UsePhoneList.remove(UsePhone)
                    break


    def adbDevicesPhone(self):
        # 通过adb devices获取所有连接的设备
        lsof = os.popen(f'adb devices')
        lsofText = lsof.read()
        logger.info(lsofText)
        serialList = []
        for item in lsofText.split('\n')[1:]:
            if not 'device' in item:
                continue
            serial = item.split('\t')[0]
            serialList.append(serial)
        return serialList


    def delBreakPhone(self, timeout=TIMEVALID):
        # 删除 超过 timeout 秒的设备 和 已断开连接的设备

        with self.LOCK:

            delBreakPhoneList = []  # 保存需删除的设备
            serialList = self.adbDevicesPhone()

            for UsePhone in self.UsePhoneList:

                if time.time() - UsePhone['time'] > timeout:    # 判断连接是否超时
                    delBreakPhoneList.append(UsePhone)

                elif not UsePhone['serial'] in serialList:  # 判断设备是否断开连接
                    delBreakPhoneList.append(UsePhone)

            for delBreakPhone in  delBreakPhoneList:
                self.UsePhoneList.remove(delBreakPhone)


PO = PhoneObject()

if __name__ == '__main__':
    for i in range(3):
        ph = PO.getPhoneSerial()
        print(ph.serial)