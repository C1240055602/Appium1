# 1、导入包，ddt,unittest
import ddt
import unittest


@ddt.ddt
class TestDdt(unittest.TestCase):
    # 1、json处理
    # 1.列表
    @ddt.file_data("test_data_list.json")
    @unittest.skip("休息一下")
    def test_json_list(self, value):
        print(f"test_json_list:{value}")

    # 2.字典
    @ddt.file_data("test_data_dict.json")
    @unittest.skip("稍候回来")
    def test_json_dict(self, value):
        print(f"test_json_dict:{value}")

    # 3.字典嵌套字典
    @ddt.file_data("test_data_dict_dict.json")
    # @unittest.skip("休息一下")
    def test_json_dict_dict(self, name, age):
        print(f"test_json_dict_dict:name:{name},age:{age}")

    # 2、yaml处理
    # 1.列表
    @ddt.file_data("test_data_list.yml")
    @unittest.skip("休息一下")
    def test_yml_list(self, value):
        print(f"test_yml_list:{value}")

    # 2.字典
    @ddt.file_data("test_data_dict.yml")
    @unittest.skip("稍候回来")
    def test_json_dict(self, value):
        print(f"test_yml_dict:{value}")

    # 3.字典嵌套字典
    @ddt.file_data("test_data_dict_dict.yml")
    # @unittest.skip("休息一下")
    def test_json_dict_dict(self, name, age):
        print(f"test_json_yml_dict:name:{name},age:{age}")
