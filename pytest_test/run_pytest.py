import pytest

# 默认运行原则
# 1、test_*.py或_test.py
# 2、文件，test_开头函数
# 3、文件，Test开头的类，test_


# 自定义原则
# 1、pytest.ini
# 2、创建新的目录
# 3、文件
if __name__ == '__main__':
    print("这是一个运行测试用例的文件")
    pytest.main(["-s"])
