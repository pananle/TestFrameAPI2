
from TestCase.Testdemo.login import login#导入login函数
from common.excel_handler import ExcelMothed#导入excel方法
from common.all_paths import casexlsx_path,log_path#导入excel路径，日志路径
from  common.logger_handler import get_logger#导入日志方法
import unittest
import ddt#导入ddt，数据驱动模式
data=ExcelMothed(casexlsx_path,'Sheet1')#初始化
case=data.get_case()#获取用例
data.excel_close()#关闭excel
@ddt.ddt
class TestLogin(unittest.TestCase):#定义测试类继承unittest.TestCase类
    @ddt.data(*case)
    def test_login_success(self,cases):
        info=eval(cases['data'])
        username=info['phone']
        password=info['verificationCode']
        expected_result=eval(cases['expected'])#预期结果
        actual_result=login(username,password)#调用被测函数
        try:
            self.assertTrue(expected_result == actual_result)  # 判断预期结果与实际结果是否一致
        except Exception as e:
            get_logger(log_path).info('用例未通过：{}'.format(e))#日志记录
            raise e#手动抛出异常
        else:
            get_logger(log_path).debug('用例通过')#日志记录

