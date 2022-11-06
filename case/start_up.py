import os
import unittest
from tomorrow3 import threads


def collectCase():
    path = os.getcwd() + '/case/appauto'
    print(f'path: {path}')
    discover = unittest.defaultTestLoader.discover(start_dir=f'{path}', pattern='test_*.py')
    caseList = []
    for test_file in discover:  # 遍历获取所有测试文件
        print('test_file:', test_file)
        for test_model in test_file:  # 遍历测试文件，获取所有测试类
            print('test_model:', test_model)
            for test_case in test_model:  # 遍历测试类，获取所有测试用例
                print('test_case:', test_case)
                caseList.append(test_case)

    return caseList


@threads(1)
def run(case):
    suitone = unittest.TestSuite()
    suitone.addTest(case)
    unittest.TextTestRunner().run(suitone)

if __name__ == '__main__':
    [run(case) for case in collectCase()]