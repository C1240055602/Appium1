from utils.LogUtil import my_log
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


# 1、定义类
class Action:
    def __init__(self, driver):
        self.driver = driver
        self.log = my_log("Base_Page")

    # 2、定义方法
    # click  id,xpath
    def by_xpath_click(self, value):
        """
        xpath 点击操作
        :param value:
        :return:
        """
        self.by_find_element(By.XPATH, value).click()

    def by_id_click(self, value):
        """
        id 点击操作
        :return:
        """
        self.by_find_element(By.ID, value).click()

    # send_keys
    def by_id_send_keys(self, value, send_value):
        """
        通过id定位元素，发送内容
        :param value:
        :param send_value:
        :return:
        """
        self.by_find_element(By.ID, value).send_keys(send_value)

    # WebDriverWait
    def by_find_element(self, by, value, timeout=30, poll=3):
        """
        隐式等待，寻找元素
        :param by:
        :param value:
        :param timeout:
        :param poll:
        :return:
        """
        WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))
        return self.driver.find_element(by, value)

    # toast
    def get_toast(self, text, timeout=30, poll=3):
        # 1、使用by_find_element寻找元素，类型xpath，value自定义
        # 2、webdriverwait获取信息，text
        # toast_loc = "//*[contains(@text,'手机号格式错误')]"
        toast_loc = "//*[contains(@text,'" + text + "')]"
        ele = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(By.XPATH, toast_loc))
        return ele.text
