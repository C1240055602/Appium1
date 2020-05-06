# encoding:utf8
from selenium.webdriver.support.wait import WebDriverWait

from PO.BasePage import Action
from conf import Caps
import time


# 1、创建类，继承Action
class CapsTest(Action):
    # 2、初始化webdriver
    def __init__(self):
        driver = Caps.desired_caps()
        super().__init__(driver)

    # 3、登录这个方法，使用封装click,send_keys
    def login_test(self):
        # 显示等待
        # allow_btn = WebDriverWait(driver, 2, 0.5).until(
        #   lambda x: x.find_element_by_id("com.android.packageinstaller:id/permission_allow_button"))

        # 1、定位暂不需要按钮
        # allow_btn = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
        # 2、点击操作1
        # allow_btn.click()
        self.by_id_click("com.boxuegu:id/negative_button")
        time.sleep(5)
        # driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        # WebDriverWait(driver, 2, 0.5).until(
        #    lambda x: x.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")).click()

        # self.by_id_click("com.android.packageinstaller:id/permission_allow_button")

        # time.sleep(5)
        # 1、点击我的 id、class、xpath
        me = '//*[starts-with(@text,"我的")]'
        # driver.find_element_by_xpath(me).click()
        self.by_xpath_click(me)
        time.sleep(5)
        # 2、输入用户名
        username = "com.boxuegu:id/edit_usr"
        # driver.find_element_by_id(username).send_keys("13133")
        self.by_id_send_keys(username, 13133)
        time.sleep(2)
        # 3、输入验证码
        code = "com.boxuegu:id/security_code"
        # driver.find_element_by_id(code).send_keys("131")
        self.by_id_send_keys(code, 131)
        time.sleep(2)
        # 4、点击登录
        login_btn = "com.boxuegu:id/btn_login"
        # driver.find_element_by_id(login_btn).click()
        self.by_id_click(login_btn)

        # 5、获取toast信息
        # toast = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("//*[contains(@text,'手机号格式错误')]"))
        toast = self.get_toast('手机号格式错误')
        # print("toast1", toast.text)
        # toast = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath("//*[contains(@text,'手机号格式错误')]"))
        # print(toast.text)
        print(toast)
        # print("toast信息%s" % toast.text)


# 4、运行
if __name__ == "__main__":
    cap_test = CapsTest()
    cap_test.login_test()
