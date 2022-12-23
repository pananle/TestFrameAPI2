

#get_logger()的参数我放到了yaml文件里，所以需要从common里import read_yaml方法、配置文件的路径
import logging
from common.read_yaml import read_yaml
from common.all_paths import config_path

log_info=read_yaml(config_path)['log']
def get_logger(filepath=None,
               fmtt=log_info['fmt'],
               logger_level=log_info['logger_level'],
               stream_level=log_info['stream_level'],
               handler_level=log_info['file_level']):
    logger = logging.getLogger()  # 初始化收集器
    # logger.handlers.clear()#清空收集器列表
    if not logger.handlers:
        logger.setLevel(logger_level)#设置日志等级
        stream_handler=logging.StreamHandler()#初始化处理器
        stream_handler.setLevel(stream_level)#设置处理器日志等级
        logger.addHandler(stream_handler)  # 处理器添加到收集器
        fmt = logging.Formatter(fmtt)  # 设置日志输出格式
        stream_handler.setFormatter(fmt)# 添加到处理器

        if filepath:
            file_handler=logging.FileHandler(filepath,'a',encoding='utf-8')#初始化文件输出处理器
            file_handler.setLevel(handler_level)#设置处理器日志等级
            file_handler.setFormatter(fmt)
            logger.addHandler(file_handler)  # 处理器添加到收集器
    return logger
