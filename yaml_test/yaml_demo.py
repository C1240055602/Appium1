from utils.YamlUtil import YamlReader

# encoding:utf8
"""
1、创建yaml格式文件：yaml,yml
2、读取这个yaml文件
3、输出这个文件
"""

# 2、读取yaml文件
# 1.导入yaml包
import yaml

# 2.打开文件 with open  with open(file, ‘r’, encoding='utf-8') as f:
# with open("yaml_demo.yml", "r", encoding='utf-8') as f:
# 3.yaml safe_load
# 单个文档
# data = yaml.safe_load(f)
# 多个文档
#    data = yaml.safe_load_all(f)
# 3、输出文件内容
#    for i in data:
#        print(i)
# print(data)

# 1.初始化yamutil，参数文件名称
# reader = YamlReader("yaml_demo.yml")
reader = YamlReader("../conf/caps.yml")
# 2.调用data方法，输出结果
data = reader.data()
# data = reader.data_all()
print(data)
