from config.config import *


class get_need(object):

    def linshi(self, name, ds,data,payload):
        if '登录' in name:
            headerse['token'] = ds.get('data').get('token')  #获取TOKEN
            headerse['iphone'] = str(data.get('mobile'))
            if '登录平台' in name:             #更换平台端参数
                headerse['platformId'] = '6'
                headerse['logintype'] = '1'
                headerse['employeeId'] = '68'
            elif 'app登录' in name:      #更换app登陆参数
                headerse['platformId'] = '5'
                headerse['logintype'] = '0'
                param['*app_id'] = ds.get('data').get('id')
                param['*app_token'] = ds.get('data').get('token')
                param['*app_iphone'] = data.get('mobile')
                param['*app_employeeId'] = ds.get('data').get('userInfo').get('employeeId')
                param['*app_name'] = ds.get('data').get('userInfo').get('name')
                param['*app_enterpriseId'] = ds.get('data').get('userInfo').get('enterpriseId')
                param['*app_departmentId'] = ds.get('data').get('userInfo').get('departmentId')
                param['*app_postId'] = ds.get('data').get('userInfo').get('postId')
                param['*app_jobNumber'] = ds.get('data').get('userInfo').get('jobNumber')
                param['*app_departmentName'] = ds.get('data').get('userInfo').get('departmentName')
                param['*app_postName'] = ds.get('data').get('userInfo').get('postName')
                param['*app_enterpriseName'] = ds.get('data').get('userInfo').get('enterpriseName')

            else:
                headerse['platformId'] = '9'
                headerse['logintype'] = '2'
                param['*iphone'] = data.get('mobile')
                if 'employeeId' in param.keys():
                    del param['employeeId']
        elif '查询可登陆企业' in name:
            headerse['employeeId'] = str(ds.get('data')[0].get('employeeId'))
            headerse['enterpriseId'] = str(ds.get('data')[0].get('enterpriseId'))
            param['enterpriseId'] = ds.get('data')[0].get('enterpriseId')
            param['*employeeId'] = ds.get('data')[0].get('employeeId')
            param['enterpriseName'] = ds.get('data')[0].get('enterpriseName')
        elif '新增人员界面' in name:
            param['employeeId'] = ds.get('data')
            param['phone'] = data.get('phone')
            param['jobNumber'] = data.get('jobNumber')
            param['idCard'] = data.get('idCard')
            param['name'] = data.get('name')
        elif '新增手机考勤组' in name:
            param['attendances_name'] = payload.get('YMMobile').get('attendancesName')
        elif '*查询所有移动考勤组' in name:
            if param.get('id') == None:
                param['attendances_name'] = ds.get('data')[0].get('attendancesName')
                param['id'] = ds.get('data')[0].get('mobileAttendanceId')
        elif '企业架构(主)' in name:
            param['*departmentName'] = ds.get('data').get('departmentName')
            param['*departmentId'] = ds.get('data').get('departmentId')
            param['*postId'] = ds.get('data').get('postId')
            param['*postName'] = ds.get('data').get('postName')
            param['*name'] = ds.get('data').get('name')
        elif '新增部门' in name:
            param['departmentName'] = data.get('departmentName')
            param['departmentId'] = ds.get('data').get('departmentId')
        elif '查看部门岗位' in name:
            param['postId'] = ds.get('data')[0].get('postId')
            param['postName'] = ds.get('data')[0].get('postName')
        elif '打卡规则列表' in name:
            if len(ds.get('entity').get('content')) > 4:
                param['punchId3'] = ds.get('entity').get('content')[3].get('punchId')
                param['punchId1'] = ds.get('entity').get('content')[1].get('punchId')
                param['punchId2'] = ds.get('entity').get('content')[2].get('punchId')
                param['punchId'] = ds.get('entity').get('content')[0].get('punchId')
            else:
                param['punchId'] = ds.get('entity').get('content')[0].get('punchId')
        elif '*上传企业logo图片' in name:
            param['logo'] = ds.get('data')
        elif '查询人事' in name:
            if param.get('employeeId') == ds.get('data').get('pageInfo').get('list')[0].get('employeeId'):
                pass
            else:
                param['employeeId'] = ds.get('data').get('pageInfo').get('list')[0].get('employeeId')
                param['phone'] = ds.get('data').get('pageInfo').get('list')[0].get('phone')
                param['jobNumber'] = ds.get('data').get('pageInfo').get('list')[0].get('jobNumber')
                param['idCard'] = ds.get('data').get('pageInfo').get('list')[0].get('idCard')
                param['name'] = ds.get('data').get('pageInfo').get('list')[0].get('name')
        elif '查询公司架构' in name:
            if param.get('departmentId') != None:
                pass
            else:
                param['departmentId'] = ds.get('data')[0].get('trees')[0].get('departmentId')
                param['departmentName'] = ds.get('data')[0].get('trees')[0].get('departmentName')
        elif '*查询所有角色列表' in name:
            param['roleId'] = ds.get('data').get('list')[0].get('roleId')
        elif '*查询所有补卡规则' in name:
            param['mendAttendanceRuleId'] = ds.get('data').get('rows')[0].get('mendAttendanceRuleId')
        elif '*查看发送消息' in name:
            if ds.get('data').get('list') != []:
                param['messageId'] = ds.get('data').get('list')[0].get('messageId')
        elif '排班规则' in name:
            param['schedulingId'] = ds.get('entity').get('content')[0].get('schedulingId')
        elif '*查看所有补卡规则' in name:
            param['mendAttendanceRuleId'] = ds.get('data').get('rows')[0].get('mendAttendanceRuleId')
        elif '*注册账户' in name:
            param['app_id'] = ds.get('data')
        elif '*APP端查看公告消息' in name:
            param['app_messageId_gg'] = ds.get('data').get('list')[0].get('messageId')
        elif '*APP端查看通知消息' in name:
            param['app_messageId_tz'] = ds.get('data').get('list')[0].get('messageId')
        elif '*上传头像图片' in name:
            param['heard_img'] = ds.get('data')
        elif 'App端补卡引导页面' in name:
            pd = [1, 2, 3, 12, 13]
            for i in range(len(ds.get('data'))):
                if ds.get('data')[i].get('type') == str(pd[0]) and ds.get('data')[i].get('titleName') == '补卡':  # 补卡
                    param['app_bkid'] = ds.get('data')[i].get('id')
                    param['app_mendAttendanceRuleId'] = ds.get('data')[i].get('contents').get('mendAttendanceRuleId')
                    pd[0] = 'ff'
                elif ds.get('data')[i].get('type') == str(pd[1]) and ds.get('data')[i].get('titleName') == '外出':  # 外出
                    param['app_wcid'] = ds.get('data')[i].get('id')
                    pd[1] = 'ff'
                elif ds.get('data')[i].get('type') == str(pd[3]) and ds.get('data')[i].get('titleName') == '出差':  # 出差
                    param['app_cxid'] = ds.get('data')[i].get('id')
                    pd[3] = 'ff'
                elif ds.get('data')[i].get('type') == str(pd[4]) and ds.get('data')[i].get('titleName') == '请假':  # 请假
                    param['app_qjid'] = ds.get('data')[i].get('id')
                    pd[4] = 'ff'
        elif '审批规则详情' in name:
            if '补卡' in name:
                param['app_bkid_sub'], param['app_bkid_aud'], param['app_bkid_CC'] = self.fenjie(ds)  # 自定义组件,审批人,抄送人
            elif '外出' in name:
                param['app_wcid_sub'], param['app_wcid_aud'], param['app_wcid_CC'] = self.fenjie(ds)  # 自定义组件,审批人,抄送人
            elif '出差' in name:
                param['app_cxid_sub'], param['app_cxid_aud'], param['app_cxid_CC'] = self.fenjie(ds)  # 自定义组件,审批人,抄送人
            elif '请假' in name:
                param['app_qjid_sub'], param['app_qjid_aud'], param['app_qjid_CC'] = self.fenjie(ds)  # 自定义组件,审批人,抄送人

    # def fenjie(self, ds):  # 分解考勤组件
    #     body = []
    #     aud = []
    #     CC = []
    #     for i in range(len(ds.get('data').get('approvers'))):
    #         bk = {}
    #         bk["approvalProcessId"] = ds.get('data').get('approvers')[i].get('approvalProcessId')
    #         bk['employeeId'] = ds.get('data').get('approvers')[i].get('employeeId')
    #         bk['sortNumber'] = ds.get('data').get('approvers')[i].get('sortNumber')
    #         bk['employeeName'] = ds.get('data').get('approvers')[i].get('employeeName')
    #         bk['headPortrait'] = ds.get('data').get('approvers')[i].get('headPortrait')
    #         if i > 3:
    #             continue
    #         aud.append(bk)
    #     for i in range(len(ds.get('data').get('copyers'))):
    #         CC.append(str(ds.get('data').get('copyers')[i].get('employeeId')))
    #     for i in range(len(ds.get('data').get('suiteFull'))):
    #         bk_k = {}
    #         bk_k['splcId'] = ds.get('data').get('suiteFull')[i].get('approvalProcessId')
    #         bk_k['optionsId'] = ds.get('data').get('suiteFull')[i].get('optionsId')
    #         bk_k['optionsSort'] = ds.get('data').get('suiteFull')[i].get('optionsSort')
    #         bk_k['userId'] = param.get('*app_employeeId')
    #         if len(ds.get('data').get('suiteFull')[i].get('approvalOptionsNodeDTO').get(
    #                 'approvalElementApprovalContentDTOS')) > 0:
    #             for ii in range(len(ds.get('data').get('suiteFull')[i].get('approvalOptionsNodeDTO').get(
    #                     'approvalElementApprovalContentDTOS'))):
    #                 if '图片 ' == ds.get('data').get('suiteFull')[i].get('approvalOptionsNodeDTO').get(
    #                         'optionsName') and i i == 0:
    #                     bk_k['value'] = insert[0]
    #                     del insert[0]
    #                 elif '时间 ' == ds.get('data').get('suiteFull')[i].get('approvalOptionsNodeDTO').get(
    #                         'optionsName') and i i == 0:
    #                     bk_k['value'] = insert[0]
    #                     del insert[0]
    #                 elif '单行输入框 ' == ds.get('data').get('suiteFull')[i].get('approvalOptionsNodeDTO').get(
    #                         'optionsName') and i i == 1:
    #                     bk_k['value'] = insert[0]
    #                     del insert[0]
    #                 elif '多行输入框 ' == ds.get('data').get('suiteFull')[i].get('approvalOptionsNodeDTO').get(
    #                         'optionsName') and i i == 1:
    #                     bk_k['value'] = insert[0]
    #                     del insert[0]
    #                 elif '定位 ' == ds.get('data').get('suiteFull')[i].get('approvalOptionsNodeDTO').get(
    #                         'optionsName') and ii < 2:
    #                     bk_k['value'] = insert[0]
    #                     del insert[0]
    #                 elif '单选框' == ds.get('data').get('suiteFull')[i].get('approvalOptionsNodeDTO').get(
    #                         'optionsName') and ii == 0:
    #                     bk_k['value'] = insert[0]
    #                     del insert[0]
    #                 elif '轨迹定位' == ds.get('data').get('suiteFull')[i].get('approvalOptionsNodeDTO').get(
    #                         'optionsName') and ii < 2:
    #                     bk_k['value'] = insert[0]
    #                     del insert[0]
    #                 else:
    #                     continue
    #                 bk_k['elementInfoId'] = ds.get('data').get('suiteFull')[i].get('approvalOptionsNodeDTO').get(
    #                     'approvalElementApprovalContentDTOS')[ii].get('elementInfoId')
    #                 d = copy.deepcopy(bk_k)
    #                 body.append(d)
    #         else:
    #             for ii in range(len(ds.get('data').get('suiteFull')[i].get('approvalOptionsNodeDTO').get(
    #                     'approvalElementContentDTOList'))):
    #                 bk_k['elementInfoId'] = ds.get('data').get('suiteFull')[i].get('approvalOptionsNodeDTO').get(
    #                     'approvalElementContentDTOList')[ii].get('elementInfoId')
    #
    #                 bk_k['value'] = insert[0]
    #                 del insert[0]
    #                 d = copy.deepcopy(bk_k)
    #                 body.append(d)
    #     return body, aud, CC
    #
    # def liuch(self, ds):
    #     if '提交申请' in name:
    #         if '补卡' in name:
    #             param['app_bkid_lc'] = ds.get('data')
    #         elif '外出' in name:
    #             param['app_wcid_lc'] = ds.get('data')
    #         elif '出差' in name:
    #             param['app_cxid_lc'] = ds.get('data')
    #         elif '请假' in name:
    #             param['app_qjid_lc'] = ds.get('data')
    #     elif '获取审批流程分类' in name:
    #         param['processGroupsId'] = []
    #         for i in range(len(ds.get('data'))):
    #             param['processGroupsId'].append(ds.get('data')[i].get('processGroupsId'))
    #     elif '获取假期列表' in name:
    #         param['hollid'] = []
    #         for i in range(len(ds.get('data').get('list'))):
    #             param['hollid'].append(ds.get('data').get('list')[i].get('leaveId'))
    #     elif '新增审批（第一步）' in name:
    #         param['one_id'] = ds.get('data')