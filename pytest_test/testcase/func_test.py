import pytest


class TestFixture:

    def test_a(self):
        print("----test_a----")
        assert 1

    def test_b(self):
        print("----test_b----")
        assert 0


if __name__ == '__main__':
    pytest.main(["-s", "test_class.py", "--html=移动端自动化测试报告.html"])
