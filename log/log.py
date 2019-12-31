import logging
import json
from config.config import *


def log_info(case_name, url, data, expect_res,pload,respon):
    #打印所有的数据
    if isinstance(data,dict):
        data = json.dumps(data, ensure_ascii=False)  # 如果data是字典格式，转化为字符串
    if isinstance(pload,dict):
        data = json.dumps(pload, ensure_ascii=False)
    logging.info("测试用例：{}".format(case_name))
    logging.info("url：{}".format(url))
    logging.info("请求参数：{}".format(data))
    logging.info("期望结果：{}".format(expect_res))
    logging.info('请求pload参数:{}'.format(pload))
    logging.info('实际返回值:{}'.format(respon))
