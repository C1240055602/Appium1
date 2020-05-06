from PO.BasePage import Action


class BxgLoginPages(Action):
    # 用户名
    username_id = "com.boxuegu:id/edit_usr"
    # 验证码
    code_id = "com.boxuegu:id/security_code"
    # 点击登录
    login_btn_id = "com.boxuegu:id/btn_login"
    # toast
    toast_xpath = '手机号格式错误'

    # by_id_send_keys,by_id_click,get_toast
    def username_send(self, send_value):
        self.by_id_send_keys(self.username_id, send_value)

    def code_send(self, send_value):
        self.by_id_send_keys(self.code_id, send_value)

    def login_click(self):
        self.by_id_click(self.login_btn_id)

    def toast(self):
        return self.get_toast(self.toast_xpath)
