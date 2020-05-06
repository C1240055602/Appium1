# 1、导入logging包
import logging

# 2、设置配置信息，日志的级别，输出格式level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 3、定义日志的名称
logger = logging.getLogger("log哈哈哈")
# 4、打印相关的日志信息
# info
logger.info("这是一个info的信息")
# debug
logger.debug("这是一个debug的信息")
# warning
logger.warning("这是一个warning的信息")
