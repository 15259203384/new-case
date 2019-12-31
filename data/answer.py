import unittest
import sys
from config.config import *

class Answer(unittest.TestCase):


    def labe(self,respon,expected,name):
        self.name=name
        self.respon=respon
        self.expected=expected
        expected=eval(expected)
        # print(list(expected.keys()))
        self.every(respon,expected)

    def every(self,respon,expected):
        #对比期望结果里所有数据和格式
        if type(expected) is list:
            #参数为列表时分解
            for i in range(len(expected)):
                self.every(respon[i],expected[i])
        else:
            for key in expected.keys():
                if type(expected.get(key)) is list:
                    # 参数为列表时分解
                    for i in range(len(expected.get(key))):
                        self.every(respon.get(key)[i], expected.get(key)[i])
                elif type(expected.get(key)) is dict:
                    # 参数为字典时分解
                    self.every(respon.get(key), expected.get(key))
                elif key in list(respon.keys()):
                    # 进行最终判断
                    self.pise(respon.get(key),expected.get(key))

    def pise(self,data,expected):
        try:
            self.assertEqual(data, expected)
        except Exception as e:
            # self.assertEqual(respon.get(key), expected.get(key))
            sys.stdout.write("出现错误！！！预期值:{} != 实际值:{}".format(self.expected, self.respon) + '\n')
            sys.stdout.flush()
            fild.append(self.name)
            logging.error('用例执行失败，失败原因; 预期值:{} != 实际值:{}'.format(expected, data))
            raise RuntimeError(e)
            # print(e)