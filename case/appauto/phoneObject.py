import os
import time
from loguru import logger
import threading


"""
设备分配层
"""


LOCK = threading.Lock()

UsePhoneList = []
# 定义全局变量，储存已分配的手机序列号和分配时间
# UsePhoneList = {'serial': serial, 'useTime': time}


def adbDevicesPhone():
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


def getPhoneSerial():
    # 获取一个可用设备

    usableSerial = {'serial': None, 'time': None}
    for i in range(100):

        delBreakPhone()     # 清理 不可用设备

        with LOCK:
            global UsePhoneList
            serialList = adbDevicesPhone()
            useSerialList = [UsePhone['serial'] for UsePhone in UsePhoneList]  # 获取已分配的设备序列号列表

            for serial in serialList:
                if not serial in useSerialList:     # 判断设备是否已被分配
                    usableSerial['serial'] = serial
                    usableSerial['time'] = time.time()
                    break

            if usableSerial['serial']:
                UsePhoneList.append(usableSerial)
                logger.debug(f'已分配该设备: {usableSerial}')
                print(f'已分配该设备: {usableSerial}')
                break

        time.sleep(5)
        logger.info(f'无可用手机等待中,已等待{i * 5}秒')
        print(f'无可用手机等待中,已等待{i * 5}秒')

    return usableSerial['serial']


def delUsePhone(serial):
    # 在已分配设备列表中删除指定设备

    with LOCK:

        global UsePhoneList
        for UsePhone in UsePhoneList:

            if UsePhone['serial'] == serial:
                UsePhoneList.remove(UsePhone)
                break


def delBreakPhone(timeout=600):
    # 删除 超过 timeout 秒的设备 和 已断开连接的设备

    with LOCK:

        global UsePhoneList
        delBreakPhoneList = []  # 保存需删除的设备
        serialList = adbDevicesPhone()

        for UsePhone in UsePhoneList:

            if time.time() - UsePhone['time'] > 600:    # 判断连接是否超时
                delBreakPhoneList.append(UsePhone)

            elif not UsePhone['serial'] in serialList:  # 判断设备是否断开连接
                delBreakPhoneList.append(UsePhone)

        for delBreakPhone in  delBreakPhoneList:
            UsePhoneList.remove(delBreakPhone)
