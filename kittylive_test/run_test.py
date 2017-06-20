__author__ = 'lisong'
# coding:utf-8
import unittest


def all_case():
    # 待执行用例的目录
    case_dir = "/home/lisong/work/kittylive_test/kittylive_test/cases"


    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,
                                                   pattern="test*.py")
    # discover方法筛选出来的用例，循环添加到测试套件中
    for test_case in discover:
        #for test_case in test_suite:
            #print(test_case)
            #print("222222222222222")
            # 添加用例到testcase
        testcase.addTests(test_case)
    print testcase
    return testcase


if __name__ == "__main__":
    # 返回实例
    runner = unittest.TextTestRunner()
    # run所有用例
    runner.run(all_case())