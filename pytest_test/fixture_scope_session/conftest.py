import pytest


# scope=session，多个py测试用例，调用一次fixture
# 登录  - 购物车 - 支付
# conftest.py 固定 位置放在项目的目录下，对哪目录有效

# 1、编写conftest.py,定义scope=session fixture 登录功能
@pytest.fixture(scope="session")
def login():
    print("这是开始登录：登录已成功")

# 2、创建多个文件.py，2个文件
# 3、1个文件 打印   添加购物车功能
# 4、1个文件 打印   支付功能
# 5、运行：命令行下运行
