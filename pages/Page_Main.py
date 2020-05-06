from PO.BasePage import Action


# 对象层 操作层
# 1、元素定位：允许按钮，点击我的
class BxgMainPage(Action):
    # 允许(暂不需要)按钮
    allow_btn_id = "com.boxuegu:id/negative_button"
    # 点击我的
    me_btn_xpath = '//*[starts-with(@text,"我的")]'

    # 2、元素操作：by_id_click、by_xpath_click
    # 允许按钮点击(暂不需要)
    def allow_click(self):
        self.by_id_click(self.allow_btn_id)

    def me_click(self):
        self.by_xpath_click(self.me_btn_xpath)
