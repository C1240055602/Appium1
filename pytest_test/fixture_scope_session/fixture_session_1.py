import pytest


def test_cart(login):
    print("用例1：登录成功后添加购物车")


if __name__ == '__main__':
    pytest.main(["-s", "fixture_session_1.py"])
