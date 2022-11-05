import unittest
from tomorrow import threads

"""
多线程执行层，用于多线程执行用例
"""


discover = unittest.defaultTestLoader.discover(start_dir='./', pattern='test_api.py')
caseList = []
for test_file in discover:    # 遍历获取所有测试文件
    print('test_file:', test_file)
    for test_model in test_file:    # 遍历测试文件，获取所有测试类
        print('test_model:', test_model)
        for test_case in test_model:    # 遍历测试类，获取所有测试用例
            print('test_case:', test_case)
            caseList.append(test_case)

@threads(3)
def run(case):
    suitone = unittest.TestSuite()
    suitone.addTest(case)
    unittest.TextTestRunner().run(suitone)

for case in caseList:
    run(case)