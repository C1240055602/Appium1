# encoding:utf8
import time

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

# 2、desired创建字典
desired_caps = dict()
# 3、platformName
# desired_caps['platformName'] = 'Android'
# # 4、platformVersion
# desired_caps['platformVersion'] = '8.0.0'
# # 5、deviceName
# desired_caps['deviceName'] = 'MI_5'
# # 6、启动程序的包名appPackage
# desired_caps["appPackage"] = 'com.qiyi.video'
# # 7、启动界面名appActivity
# desired_caps['appActivity'] = 'org.qiyi.android.video.MainActivity'
desired_caps['platformName'] = 'Android'
# 4、platformVersion
desired_caps['platformVersion'] = '5.1'
# 5、deviceName
desired_caps['deviceName'] = 'Samsung_Galaxy_S6'

desired_caps["appPackage"] = 'com.boxuegu'
# 7、启动界面名appActivity
desired_caps['appActivity'] = 'com.boxuegu.activity.MainFlutterActivity'
# 解决中文
desired_caps["unicodeKeyboard"] = True
desired_caps["resetKeyboard"] = True

# 获取toast automationName = uiautomator2
desired_caps["automationName"] = 'uiautomator2'

# 8、http，连接appium服务器
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# time.sleep(5)
# # 1、点击我的 id、class、xpath
# me = '//*[starts-with(@text,"我的")]'
# driver.find_element_by_xpath(me).click()
# time.sleep(5)
#
# # 点击未登录 com.qiyi.video:id/phone_my_main_head_layout  com.qiyi.video:id/ugc_feed_friends_name_and_class
# # com.qiyi.video:id/ugc_feed_friends_name
# ulogin_btn = "com.qiyi.video:id/ugc_feed_friends_name_and_class"
# driver.find_element_by_id(ulogin_btn).click()
# time.sleep(5)
# # 2、输入用户名
# username = "com.qiyi.video:id/phoneMyAccountEmail"
# driver.find_element_by_id(username).send_keys("2121908201@qq.com")
# time.sleep(2)
# # 3、输入密码
# code = "com.qiyi.video:id/phoneMyAccountPwd"
# driver.find_element_by_id(code).send_keys("1234567QWEqwe")
# time.sleep(2)
# # 4、点击登录  不要延时，因为toast信息很短会无效
# login_btn = "com.qiyi.video:id/phoneMyAccountLogin"
# driver.find_element_by_id(login_btn).click()
#
# # 5、获取toast信息   lambda表达式方法体   模糊匹配 "//*[contains(@text,'帐号或密码错误')]"
# # lambda x: x.find_element_by_xpath("//*[contains(@text,'帐号或密码错误')]")
# toast_message = "帐号或密码错误"
# message = '//*[@text=\'{}\']'.format(toast_message)
# toast_element = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(message))
# # toast: object = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("//*[contains(@text,'帐号或密码错误')]"))
# print(toast_element.text)

# 1、显示等待 定位暂不需要按钮
allow_btn = WebDriverWait(driver, 2, 0.5).until(
    lambda x: x.find_element_by_id("com.boxuegu:id/negative_button"))
# 2、点击操作1
allow_btn.click()
time.sleep(5)
# WebDriverWait(driver, 2, 0.5).until(lambda x: x.find_element_by_id("com.boxuegu:id/negative_button")).click()

time.sleep(5)
# 1、点击我的 id、class、xpath
me = '//*[starts-with(@text,"我的")]'
driver.find_element_by_xpath(me).click()
time.sleep(5)
# 2、输入用户名
username = "com.boxuegu:id/edit_usr"
driver.find_element_by_id(username).send_keys("12341235")
time.sleep(2)
# 3、输入验证码
code = "com.boxuegu:id/security_code"
driver.find_element_by_id(code).send_keys("1234")
time.sleep(2)
# 4、点击登录
login_btn = "com.boxuegu:id/btn_login"
driver.find_element_by_id(login_btn).click()

# 5、获取toast信息
toast = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("//*[contains(@text,'手机号格式错误')]"))
print(toast.text)
