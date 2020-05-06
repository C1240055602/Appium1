import pytest


# 1、创建简单的测试方法        unittest.testcase

# def func(x):
#    return x+1

# def test_a():
#    print("----test_a----")
#    assert func(3) == 5

# def test_b():
#    print("----test_b----")
#    assert func(3) == 4
# 2、执行
# 代码运行
# if __name__ == '__main__':
#    pytest.main(["-s","demo_pytest.py"])
# 命令下运行


# 1、修改用例，增加断言，assert
# 2、命令行运行,--reruns n 3/5/1

# 1、创建类
class TestLogin:
    # 2、创建测试方法 test开头
    def test_a(self):
        print("----test_a----")
        # assert 1!=2 #成功
        # assert 1<2 #成功
        assert "h" in "hello"

    def test_b(self):
        print("----test_b----")
        # assert 1==2 #失败
        # assert 1>2 #失败
        assert "h" not in "hello"

    # 用例有个问题，单独对这个重试策略：rerun 1 delay5
    # @pytest.mark.flaky(reruns = 1,reruns_delay=5)
    # def test_c(self):
    #     print("test_c")
    #     assert 0


# 3、创建setup,teardown
#     def setup(self):
#        print("----setup-----")
#
#     def teardown(self):
#        print("----teardown----")
#
# #4、创建setupclass,teardownclass
#
#     def setup_class(self):
#        print("----setup_class----")
#
#     def teardown_class(self):
#        print("----teardown_class----")

if __name__ == '__main__':
    pytest.main(["-s", "demo_pytest.py", "--html=移动端自动化测试报告.html", "-reruns 3"])

# pytest断言 assert

# assertEqual(1,2)
# pytest assert 1==2
# self.assertNotEqual(1, 2)
# pytest assert 1!=2
# self.assertTrue(1>2,"1>2是错误的") #失败
# pytest assert True / 1>2 1<2
# self.assertFalse(1>2)#成功
# pytest assert "h" not in ""hello"
# self.assertIn("h","hello")#成功
# self.assertNotIn("h", "hello") #失败
