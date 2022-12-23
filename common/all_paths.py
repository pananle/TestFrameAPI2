
# 这里把所有文件的目录路径都写在这里用变量接收，获取的时候直接调用变量就行。
import os
from datetime import datetime

dir_name1=os.path.dirname(os.path.abspath(__file__))
dir_name=os.path.dirname(dir_name1)
log_path=os.path.join(os.path.join(dir_name,'log'),'log.log')#log文件路径
casexlsx_path=os.path.join(os.path.join(dir_name,'data'),'TestAPI.xlsx')#测试用例excel文件路径
report_time = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")    # 以时间命名日志文件，格式为"年-月-日"
report_name = "{}.html".format(report_time)
report_path=os.path.join(os.path.join(dir_name,'reports'),report_name)#测试报告文件路径
config_path=os.path.join(os.path.join(dir_name,'conf'),'conf.yaml')#配置文件路径
case_path=os.path.join(dir_name,'TestCase')#测试用例代码路径


