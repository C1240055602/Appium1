import pytest


@pytest.fixture(scope="module")
def before():
    print("----before----")
    return "这个是一个fixture"


# module，在当前.py包含所有用例，执行前只执行一次fixture
# 1、定义多个用例，类，方法
# 2、修改scope参数
# 3、fixture调用

def test_c(before):
    print("----test_c----")


def test_d(before):
    print("----test_d----")


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
    pytest.main(["-s", "pytest_fixture_module.py"])
