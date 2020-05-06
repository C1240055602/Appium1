import pytest

"""
1、fixture作为参数传入
2、fixture作为函数传入
"""


# fixture作为参数传入
# 1、定义fixture方法，命名不要使用test开头，跟用例区分
@pytest.fixture()
def before():
    print("----before----")
    return "这个是一个fixture"


@pytest.fixture(scope="function")
def after():
    print("----after----")
    return "这个是一个fixture_after"


# 2、使用@pytest.fixture装饰 步骤1方法
# 3、定义测试用例方法test，把fixture函数名称当用参数传入
def test_1(before):
    res = before
    print("接收的fixture信息", res)
    print("----test_1----")


def test_2(before):
    print("test2,接收的fixture信息", before)


# 1、定义2个fixture
# 2、定义方法，before,after参数传递
def test_3(before, after):
    print(before)
    print("test3")
    print(after)


class TestFixture:
    def setup(self):
        print("----setup---")

    def test_a(self, before):
        print("----test_a----")

    def test_b(self, after):
        print("----test_b----")


if __name__ == '__main__':
    pytest.main(["-s", "pytest_fixture_func.py"])
