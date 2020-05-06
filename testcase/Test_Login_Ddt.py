import unittest
from conf import Caps
from pages.Page_Main import BxgMainPage
from pages.Page_Login import BxgLoginPages
import time
import ddt

# 1、PO模式+unittest+ddt，导入包，继承unittest.TestCase
# 1、定义参数化数据：用户名，密码
# username,code
test_data = [
    {"username": "13331", "code": "131"},
    {"username": "@#$%^&*()", "code": "abcdef"}
]


@ddt.ddt
class Login(unittest.TestCase):
    # setupclass，初始化appium
    @classmethod
    def setUpClass(cls):
        # 初始化appium连接
        cls.driver = Caps.desired_caps()

    # 2、setup 启动app
    def setUp(self):
        self.driver.launch_app()
        self.bxgmain = BxgMainPage(self.driver)
        self.bxglogin = BxgLoginPages(self.driver)

    # 2、定义测试用例方法,test_login
    # 2、data数据驱动
    @ddt.data(*test_data)
    @ddt.unpack
    @unittest.skip("休息一下")
    def test_login(self, username, code):
        # list
        driver = Caps.desired_caps()
        bxgmain = BxgMainPage(driver)
        bxglogin = BxgLoginPages(driver)
        # 3、编写测试用例步骤
        # 登录测试用例
        # 1.点击允许暂不需要按钮
        bxgmain.allow_click()
        time.sleep(2)
        # 2.点击我的
        bxgmain.me_click()
        # 3.输入用户名
        bxglogin.username_send(username)  # 特殊字符，汉字
        # 4.输入验证码
        bxglogin.code_send(code)
        # 5.点击登录
        bxglogin.login_click()
        # 6.获取toast
        toast = bxglogin.toast()
        print(toast)

    # file_data数据驱动
    # 1、yaml测试用例编写 编写完成
    # 2、file_data实现数据驱动
    @ddt.file_data("Test_Login_Ddt.yml")
    def test_login_file(self, username, code):
        # list
        # driver = Caps.desired_caps()
        # bxgmain = BxgMainPage(driver)
        # bxglogin = BxgLoginPages(driver)
        # 3、编写测试用例步骤
        # 登录测试用例
        # 1.点击允许暂不需要按钮
        self.bxgmain.allow_click()
        time.sleep(2)
        # 2.点击我的
        self.bxgmain.me_click()
        # 3.输入用户名
        self.bxglogin.username_send(username)  # 特殊字符，汉字
        # 4.输入验证码
        self.bxglogin.code_send(code)
        # 5.点击登录
        self.bxglogin.login_click()
        # 6.获取toast
        toast = self.bxglogin.toast()
        print(toast)

    # 3、teardown 关闭app
    def tearDown(self):
        self.driver.close_app()

    # 4、关闭appium
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


# 4、运行
if __name__ == '__main__':
    unittest.main(verbosity=2)

# 3、file_data数据驱动

# 需求：提高运行的效率
# unittest fixture setup setupclass teartown teartownclass
# 1、setupclass，初始化appium
# 2、setup 启动app
# 3、teardown 关闭app
# 4、关闭appium
