import pytest

"""
1、fixture作为参数传入
2、fixture作为函数传入
"""


# fixture作为参数传入
# 1、定义fixture方法，命名不要使用test开头，跟用例区分
@pytest.fixture(scope="class")
def before():
    print("----before----")
    return "这个是一个fixture"


# 2、使用@pytest.fixture装饰 步骤1方法
# 3、定义测试类，测试用例方法test

# class，fixture，class里面所有用例执行之前  执行一次
# 1、类方法增加fixture调用
# 2、修改fixture参数scope  = class

# @pytest.mark.usefixtures("before")
class TestFixture:

    def setup_class(self):
        print("----setup_class")

    def setup(self):
        print("----setup---")

    def test_a(self, before):
        print("----test_a----")

    def test_b(self, before):
        print("----test_b----")


if __name__ == '__main__':
    pytest.main(["-s", "pytest_fixture_class.py"])