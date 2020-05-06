from conf import Caps
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = Caps.desired_caps()

# 显示等待 定位暂不需要按钮
allow_btn = WebDriverWait(driver, 2, 0.5).until(
    lambda x: x.find_element_by_id("com.boxuegu:id/negative_button"))

# 2、点击操作1
allow_btn.click()
time.sleep(5)

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
