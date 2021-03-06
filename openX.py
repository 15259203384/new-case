import xlrd

class xlsx_open(object):

    
    def excel_to_list(self,datafile):
        data = []  # 新建个空列表，来乘装所有的数据
        wb = xlrd.open_workbook(datafile)  # 打开excel
        sh = wb.sheet_by_name('Sheet1')  # 获取工作簿
        header = sh.row_values(0)  # 获取标题行数据
        for i in range(1, sh.nrows):  # 跳过标题行，从第二行开始取数据
            d = dict(zip(header, sh.row_values(i)))  # 将标题和每行数据组装成字典
            data.append(d)
        return data  # 列表嵌套字典格式，每个元素是一个字典



