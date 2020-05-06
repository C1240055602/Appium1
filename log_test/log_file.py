import logging

# 1、设置logger名称
logger = logging.getLogger("log_file")
# 2、设置log级别总开关 INFO
logger.setLevel(logging.INFO)
# 3、创建handler， 控制台，文件
fh_stream = logging.StreamHandler()

fh_file = logging.FileHandler("test.log")

# 4、设置控制台日志级别，文件日志级别
fh_stream.setLevel(logging.WARNING)

fh_file.setLevel(logging.DEBUG)
# 5、定义输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh_stream.setFormatter(formatter)
fh_file.setFormatter(formatter)

# 6、添加handler
logger.addHandler(fh_stream)
logger.addHandler(fh_file)
# 7、运行输出
logger.info("这是一个info信息")
logger.debug("这是一个debug信息")
logger.warning("这是一个warning信息")
