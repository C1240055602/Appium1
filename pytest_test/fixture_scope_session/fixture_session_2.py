import pytest


def test_pay(login):
    print("用例2，登录成功后执行支付")


if __name__ == '__main__':
    pytest.main(["-s", "fixture_session_2.py"])
