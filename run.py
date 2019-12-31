import unittest
import sys
import os
from lib.HTMLTestReportCN import HTMLTestRunner
from ddt import ddt,data,file_data,unpack
sys.path.append('..')
from config.config import *
from openX import xlsx_open
#from lib.HTMLTestRunner import HTMLTestRunner
#from send_emali import *
from data import Get_data

datta = tuple(xlsx_open().excel_to_list(test_case_path) )  #打开EXCLE


@ddt
class run_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.info('测试开始==========================================')

    @classmethod
    def tearDownClass(cls):
        logging.info('测试结束==========================================')
        logging.info("共失败条:{}条,失败用例:{}".format(len(fild),",".join(fild),len(fild)) + '\n')
        sys.stdout.write("失败用例:{}".format(",".join(fild)) + '\n')
        sys.stdout.flush()

    def setUp(self):
        logging.info('开始执行用例**************************************')

    def tearDown(self):
        logging.info('一个用例执行完毕**********************************'+'\n'+'\n')


    @data(*datta)
    # ddt处理数据，整理成列表套字典
    def test_YunMai(self,vlue):
        tt=Get_data.send_url()
        tt.get_data(vlue)

if __name__=='__main__':
    #discover = unittest.defaultTestLoader.discover(test_case_path, pattern='test*.py')
    case_names=[]
    for name in datta:
        case_names.append(name.get('name'))
    s = unittest.TestSuite()  # 实例化
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(run_test))  # 加载用例
    print(report_file)
    with open(report_file, 'wb') as f:  # 从配置文件中读取
        result = HTMLTestRunner(stream=f, title="新增员工一日游", description="测试描述：测试结果详情请查看附件", tester='hj').run(s,case_names)    #.run(discover)
   # if send_email_after_run:
    #    send_email(report_file)
