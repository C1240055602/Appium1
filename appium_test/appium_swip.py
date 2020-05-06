# encoding:utf8
import time

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

# 2、desired创建字典
desired_caps = dict()
# 3、platformName
desired_caps['platformName'] = 'Android'
# 4、platformVersion
desired_caps['platformVersion'] = '5.1'
# 5、deviceName
desired_caps['deviceName'] = 'Samsung_Galaxy_S6'
# 6、启动程序的包名appPackage
# 小米商城 com.xiaomi.shop/com.xiaomi.shop2.activity.MainActivity
# 计算器 com.android.calculator2/com.android.calculator2.Calculator
# 爱奇艺 com.qiyi.video/org.qiyi.android.video.MainActivity
# 设置 com.android.settings/com.android.settings.Settings}
desired_caps["appPackage"] = 'com.boxuegu'
# 7、启动界面名appActivity
desired_caps['appActivity'] = 'com.boxuegu.activity.MainFlutterActivity'

# 解决中文
desired_caps["unicodeKeyboard"] = True
desired_caps["resetKeyboard"] = True

# 8、http，连接appium服务器
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(5)

# 计算原坐标点
# 获取终止坐标Y轴-起始坐标Y，得到中心的值/2
# 起始坐标Y+ 除以2的值 ，滑动Y轴坐标
# 825-285 = 540/2 = 270(小米商城)
# 270+285 = 555  Y轴(小米商城)

# 999-489 = 510/2 = 255(爱奇艺)
# 255+489 = 744(爱奇艺)
#   700 x轴
# 拖动终止坐标
# Y轴
# 获取手机的宽和高，高度*3/4   {'width': 1080, 'height': 1920}
# driver可以获取
screen = driver.get_window_size()
# print(screen)
# screen*3/4
# time.sleep(5)
#
# driver.swipe(700, 744, 700, screen["height"] * 3 / 4, 3000)
# time.sleep(5)

# # 相对定位，获取手机的宽和高，* 相应比例
# # 向上X轴不变，y轴变化
# driver.swipe(screen["width"] * 0.5, screen["height"] * 3 / 4, screen["width"] * 0.5, screen["height"] * 1 / 4, 3000)
# time.sleep(5)
# # 向下X轴不变，y轴变化
# # driver.swipe(screen["width"] * 0.5, screen["height"] * 1 / 4, screen["width"] * 0.5, screen["height"] * 3 / 4, 3000)
# # time.sleep(5)
# # 向右Y轴不变，x轴变化
# driver.swipe(screen["width"] * 0.9, screen["height"] * 0.3, screen["width"] * 0.1, screen["height"] * 0.3, 3000)
# time.sleep(5)
# # 向右Y轴不变，x轴变化
# driver.swipe(screen["width"] * 0.9, screen["height"] * 0.3, screen["width"] * 0.1, screen["height"] * 0.3, 3000)
# time.sleep(5)
# # 向左Y轴不变，x轴变化
# driver.swipe(screen["width"] * 0.1, screen["height"] * 0.3, screen["width"] * 0.9, screen["height"] * 0.3, 3000)
# time.sleep(5)
#
# # driver.save_screenshot("jietu.png")
# driver.get_screenshot_as_file('screenshot/jietu.png')
# driver.swipe()

# 拖动终止坐标
# Y轴
# 获取手机的宽和高，高度*3/4
# driver可以获取

time.sleep(5)
driver.swipe(700, 750, 700, screen["height"] * 3 / 4, 3000)
time.sleep(5)

screen = driver.get_window_size()
# print(screen)
# screen*3/4
time.sleep(5)
driver.swipe(700, 750, 700, screen["height"] * 3 / 4, 3000)
time.sleep(5)
# 相对定位，获取手机的宽和高，* 相应比例
# 向上X轴不变，y轴变化
# driver.swipe(screen["width"]*0.5,screen["height"]*3/4,screen["width"]*0.5,screen["height"]*1/4,3000)
# time.sleep(5)
# 向下X轴不变，y轴变化
# driver.swipe(screen["width"]*0.5,screen["height"]*1/4,screen["width"]*0.5,screen["height"]*3/4,3000)

# 向右Y轴不变，x轴变化
driver.swipe(screen["width"] * 0.75, screen["height"] * 0.5, screen["width"] * 0.2, screen["height"] * 0.5, 3000)
# 向左Y轴不变，x轴变化
time.sleep(5)
# driver.swipe(screen["width"]*0.2,screen["height"]*0.5,screen["width"]*0.75,screen["height"]*0.5,3000)

# driver.save_screenshot("滑动截图.png")
driver.get_screenshot_as_file('screenshot/滑动截图文件.png')
# driver.swipe()
time.sleep(10)
driver.quit()

# 9、退出
driver.quit()
