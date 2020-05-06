import pytest
import allure

#1、title

@allure.feature("这里是一级标签：feature")
class Test_Fixture:
    #1、创建step步骤方法
    #2、增加allure step
    #3、用例来调用step方法
    @allure.step("步骤1")
    def step_1(self):
        print("这是步骤1")

    @allure.step("步骤2")
    def step_2(self):
        print("这是步骤2")

    @allure.step("步骤3")
    def step_3(self):
        print("这是步骤3")

    @allure.title("测试用例标题1")
    @allure.description("测试用例1的描述")
    @allure.story("这里是二级标签:a")
    @allure.severity("critical")
    def case_a(self):
        print("----test_a----")
        self.step_1()
        self.step_2()
        assert 1

    @allure.title("测试用例标题2")
    @allure.description("测试用例2的描述")
    @allure.story("这里是二级标签:a")
    @allure.severity(allure.severity_level.BLOCKER)
    def case_b(self):
        print("----test_b----")
        self.step_3()
        assert 0


    #1、新建方法
    name_password_list = [("xiaoming", "123123"), ("xiaohong", "456456")]
    @pytest.mark.parametrize(("name", "password"), name_password_list)
    def case_dynamic(self,name,password):
        print(name)
        print(password)
        allure.dynamic.title(name)
        self.step_4()
    #2、定义参数化
    #3、allure动态生成title

    def step_4(self):
        with allure.step("第1步："):
            pass
        with allure.step("第2步："):
            pass

if __name__ == '__main__':
    pytest.main(["-s", "test_class.py", "--html=移动端自动化测试报告.html"])
