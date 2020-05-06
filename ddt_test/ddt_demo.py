# 实现4组测试用例执行
# 1、导入包，ddt,unittest
import ddt
import unittest


# 2、创建类，ddt.ddt
@ddt.ddt
class MyTestDdt(unittest.TestCase):
    # 3、测试用例方法，@data参数化
    # 数值
    @ddt.data(2, 4, 6, 8)
    @unittest.skip("先不运行")
    def test_1(self, value):
        print(f"参数内容是:{value}")

    # 字符串
    @ddt.data('code=200', "success", 'no')
    @unittest.skip("先不运行")
    def test_str(self, value):
        print(value)
        self.assertIn(value, "this is a success code=200")  # 断言

    # 列表
    @ddt.data([3, 2], [4, 3], [3, 5])
    @ddt.unpack  # 对列表元素进行拆解
    @unittest.skip("休息一下")
    def test_list(self, first, second):
        self.assertTrue(first > second)

    # 元组
    @ddt.data((3, 2), (4, 3), (3, 5))
    @ddt.unpack
    def test_tuple(self, first, second):
        self.assertTrue(first > second)

    # 字典
    @ddt.data({"first": 1, "second": 3, "third": 2}, {"first": 4, "second": 6, "third": 5})
    @ddt.unpack
    def test_dict(self, first, second, third):
        self.assertFalse(first < third < second)


# 4、运行
if __name__ == "__main__":
    unittest.main(verbosity=2)
