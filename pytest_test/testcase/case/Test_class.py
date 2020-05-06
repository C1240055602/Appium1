import pytest


class T_Fixture:

    def case_a(self):
        print("----test_case_a----")
        assert 1

    def case_b(self):
        print("----test_case_b----")
        assert 0

if __name__ == '__main__':
    pytest.main(["-s", "test_class.py", "--html=移动端自动化测试报告.html"])
