import unittest
from library.HTMLTestRunnerNew import HTMLTestRunner#导入第三方模块
from  common.all_paths import report_path,case_path#导入报告路径，测试用例的路径

loader=unittest.TestLoader()#初始化用例的加载器
test_suite=loader.discover(case_path)#自动加载测试用例
with open(report_path,'wb') as f:
    runner=HTMLTestRunner(f,title='自动化测试报告',description='shop',tester='tester')
    runner.run(test_suite)#运行

