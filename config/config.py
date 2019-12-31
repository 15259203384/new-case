import logging
import os
import time

today = time.strftime('%Y%m%d', time.localtime())
now = time.strftime('%Y%m%d_%H%M%S', time.localtime())

prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 当前文件的上一级的上一级目录（增加一级）
log_file = os.path.join(prj_path, 'log', 'log_{}.txt'.format(today))  # 更改路径到log目录下
test_case_path = os.path.join(prj_path, 'testcase','1.xlsx')   # 用例目录
report_file= os.path.join(prj_path, 'html', '{}'.format(time.strftime("%Y%m%d%H%M%S", time.localtime()))+'.html')   # html测试报告地址
img_path=os.path.join(prj_path, 'img')   # 图片地址

URL='https://kq.4000750222.com'   #测试网址

#日志格式
logging.basicConfig(level=logging.DEBUG,
                    filename=log_file,
                    datefmt='%Y/%m/%d %H:%M:%S',
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
                    filemode='a')

fild=[]    #存储，失败用例名称

headerse={'Host': 'kq.4000750222.com',
          'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 75.0.3770.80 Safari / 537.36'}

param={}   #存储，动态参数