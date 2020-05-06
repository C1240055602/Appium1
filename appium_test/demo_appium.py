# 1、导入包
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
# 6、启动程序的包名appPackage
# 计算器 com.android.calculator2/com.android.calculator2.Calculator
# 小米商城 com.xiaomi.shop/com.xiaomi.shop2.activity.MainActivity
# 天猫 com.tmall.wireless/com.tmall.wireless.maintab.module.TMMainTabActivity
# 博学谷 com.boxuegu/com.boxuegu.activity.MainFlutterActivity
# 博学谷2 com.boxuegu/com.boxuegu.activity.mycenter.SettingsActivity
# 小米视频 com.miui.video/com.miui.video.feature.main.MainTabActivity
# 京东 com.jingdong.app.mall/com.jingdong.app.mall.MainFrameActivity
# 阅读 com.duokan.reader/com.duokan.reader.DkMainActivity
# 爱奇艺 com.qiyi.video/org.qiyi.android.video.MainActivity
# 大众点评 com.dianping.v1/com.dianping.main.guide.MainActivity
# 米家 com.xiaomi.smarthome/com.xiaomi.smarthome.SmartHomeMainActivity
# 有品 com.xiaomi.youpin/com.xiaomi.youpin.activity.YouPinMainTabActivity
# 一点资讯 com.yidian.xiaomi/com.yidian.news.ui.navibar.NavibarHomeActivity
# 百度地图 com.baidu.BaiduMap/com.baidu.baidumaps.MapsActivity
# 设置 com.android.settings/com.android.settings.Settings}
# desired_caps["appPackage"] = 'com.qiyi.video'
desired_caps["appPackage"] = 'com.boxuegu'
# 7、启动界面名appActivity
desired_caps['appActivity'] = 'com.boxuegu.activity.MainFlutterActivity'
# 8、http，连接appium服务器
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# time.sleep(5)
# 隐式等待 driver.implicitly_wait(5)

# 显示等待
allow_btn = WebDriverWait(driver, 2, 0.5).until(
    lambda x: x.find_element_by_id("com.android.packageinstaller:id/permission_allow_button"))

# 1、定位允许按钮
# allow_btn = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
# 2、点击操作1
allow_btn.click()

time.sleep(10)
# driver.find_element_by_id("com.miui.calculator:id/btn_1_s").click()
# 获取数字1，name定位废弃了不用
# button = driver.find_elements_by_class_name("android.widget.Button")
# print(button)
# button[1].click()
# 获取数字1，xpath-文本定位
# xpath_text="//*[@text='1']"
# driver.find_element_by_xpath(xpath_text).click()
# driver.find_element_by_xpath("//*[@text='+']").click()
# driver.find_element_by_xpath("//*[@text='2']").click()
# driver.find_element_by_xpath("//*[@text='=']").click()
# xpath-id定位
# xpath_id = "//*[@resource-id='com.miui.calculator:id/btn_1_s']"
# driver.find_element_by_xpath(xpath_id).click()
# xpath - class定位
# xpath_class_1 = '//android.widget.Button'
# xpath_class_2 = "//*[@class='android.widget.TextView']"
# driver.find_elements_by_xpath(xpath_class_2)[6].click()

# xpath模糊定位contains text
# xpath_contains="//*[contains(@text,'锁屏、密码和指纹')]"
# driver.find_element_by_xpath(xpath_contains).click()
# xpath_contains_id = "//*[contains(@resource-id,'android:id/title')]"
# class @resource-id 换成class
# xpath_contains_list = driver.find_elements_by_xpath(xpath_contains_id)
# print(xpath_contains_list)


# starts-with
# xpath_starts = "//*[starts-with(@text,'双卡')]"
# driver.find_element_by_xpath(xpath_starts).click()

# 9、退出
driver.quit()
