import unittest
from utils.HTMLTestRunner3 import HTMLTestRunner

# 1、discover方法查找用例
suite = unittest.defaultTestLoader.discover("unittest_test", "Test*.py")
# 2、TextTestRunner运行用例，run方法  verbosity=2, stream=f
# runner = unittest.TextTestRunner()
# runner.run(suite)

# 1.打开文件对象
# with open("test_report.txt", "a") as f:
#     # 2.把对象以参数形式 runner
#     runner = unittest.TextTestRunner(verbosity=2, stream=f)
#     runner.run(suite)

# HTM格式报告
# 1、HTMLTestRunner  支持python2版本
# 若要支持python3，则要修改文件内容
# 2、打开文件对象，HTMLTestRunner方法替换TextTestRunner     (二进制:wb+ )
with open("test_report.html", "wb+") as report:
    runner = HTMLTestRunner(stream=report, verbosity=2, title="测试报告", description="这是一个练习的测试")
    runner.run(suite)
