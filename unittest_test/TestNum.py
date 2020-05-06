# 1、导入unittest包
import unittest


# 2、创建类，继承unittest.TestCase
class Test(unittest.TestCase):
    # 3、创建测试用例方法，方法test开头

    @classmethod
    def setUpClass(cls):
        print("测试用例执行前只执行一次")

    def setUp(self):
        print("测试用例执行前操作=====")

    # @unittest.skip("累了，不想执行了")
    # @unittest.skipUnless(2>1,"成立不会跳过用例")
    @unittest.skipUnless(2 < 1, "不成立跳过测试用例")
    def test_num_02(self):
        print("num02")
        # self.assertEqual(1, 2)
        # self.assertNotEqual(1, 2)
        # self.assertTrue(1 > 2, "1>2是错误的")  # 失败
        # self.assertFalse(1 > 2)  # 成功
        # self.assertIn("h","hello")#成功
        self.assertNotIn("h", "hello")  # 失败

    # @unittest.skipIf(2>1,"因为2>1,不想执行了")
    @unittest.skipIf(2 < 1, "因为2<1,不想执行了")
    def test_num_01(self):
        print("num01")
        # self.assertEqual(1, 1)
        # self.assertNotEqual(1, 1, "内容相等了")
        # self.assertTrue(True)  # 成功
        # self.assertFalse(True)  # 失败
        # self.assertIn("a","hello","内容不存在")#失败

        self.assertNotIn("a", "hello", "内容不存在")

    def tearDown(self):
        print("测试用例执行后操作=====")

    @classmethod
    def tearDownClass(cls):
        print("测试用例执行后只执行一次")
