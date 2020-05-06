# 1、导入unittest包
import unittest


# 2、创建类，继承unittest.TestCase
class Test(unittest.TestCase):
    # 3、创建测试用例方法，方法test开头

    def test_add_02(self):
        print(3 - 2)

    def test_add_01(self):
        print(5 + 7)

    def add_03(self):
        print("add03")


# 4、运行
if __name__ == "__main__":
    suite = unittest.TestSuite()
    # 写成数组
    test_cases = [Test("test_add_02"), Test("test_add_01")]
    # suite.addTest(Test("test_add_02"))
    # suite.addTest(Test("test_add_01"))
    suite.addTests(test_cases)
    runner = unittest.TextTestRunner()
    runner.run(suite)
