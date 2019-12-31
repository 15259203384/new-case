import requests
import time
import json
from config.config import *
from data.answer import Answer
import json
from log.log import *
import copy
from NEED import get_need

class send_url(object):

    def get_data(self, data, files=None, user=None):
        #获取测试用例参数
        print(headerse)
        name=data.get('name')   #名称
        url=URL+data.get('url')     #接口地址
        method=data.get('method')     #请求方式
        new_data=eval(data.get('data') )    #输入data参数
        payload=data.get('payload')   #输入pload参数
        expected=data.get('expected')  #得到期望结果
        style=str(data.get('style') )      #其他杂项处理方图片名称式，二进制形式，第一位代表图片是否多个，第二位代表传入play参数
        img_name=data.get('img_name')  #
        need=data.get('need')
        repen=data.get('repen')
        if img_name != '':              # 处理图片
            files=self.make_img(img_name,style)
        if repen !='':               #传入替代参数
            if style[1:2]==1:
                payload=self.replay(eval(repen),payload)
            else:
                new_data=self.replay(eval(repen),new_data)
        if method.upper() == 'GET':  # get请求
            respon = requests.get(url=url, headers=headerse, params=new_data).text
        elif method.upper() == 'POST':  # post请求
            if style[0:1] == 1:
                respon = requests.post(url, headers=headerse, params=new_data, data=payload, files=files).text
            else:
                respon = requests.post(url, headers=headerse, params=new_data, data=payload, files=files).text
        else:
            respon=''
        print(respon)
        respon=json.loads(respon)
        if '*' in name:
            get_need().linshi(name,respon,new_data,payload)  # 根据用例名称获取动态需要的数据，*代表添加数据
        log_info(name, url, new_data, expected, payload,respon)
        Answer().labe(respon,expected,name)

    def need_get(self,data,respon):  #获取参数
        fram = copy.deepcopy(respon)
        for tatle in data:
            self.get_need(fram,data)


    def replay(self,repen,data):   #传入参数时
        for tatle in repen:
            if type(tatle) is list:
                # 传入列表代表获取和保存参数名不同
                data[tatle[0]]=param[tatle[1]]
            else:
                data[tatle]=param[tatle]

    def make_img(self,img_name,style):
        # 处理图片
        if style == 1:
            img2 = eval(img_name)
            files = []
            for i in range(len(img2)):
                files.append(('files', open(img_path + '\\' + img2[i], 'rb')))
            return files
        else:
            files = [('file', open(img_path + '\\' + img_name, 'rb'))]  # 上传图片
            return files