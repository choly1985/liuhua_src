
import time
import unittest

from UI_AUTOMATION.test.testcase.gb_pc_form_case import FormTestCase
from UI_AUTOMATION.utils.HTMLTestRunner import HTMLTestRunner
from UI_AUTOMATION.utils.config import REPORT_PATH
from UI_AUTOMATION.utils.haoemail import Email
from utils.HTMLTestRunner import _TestResult

# # 构造测试集
suite = unittest.TestSuite()
# suite.addTest(FormTestCase('login_GB'))
#............................................................



# suite.addTest(FormTestCase('test_formtest_creditcard'))
suite.addTest(FormTestCase('test_formtest_ebanxinstalment'))
suite.addTest(FormTestCase('test_formtest_boleto'))
suite.addTest(FormTestCase('test_formtest_ideal'))
suite.addTest(FormTestCase('test_formtest_pse'))



# print(HTMLTestRunner.run(self.stopTime))

now_time = time.strftime('%Y%m%d-%H%M%S', time.localtime())
report = REPORT_PATH + '\\' + 'PAY_Report '+ now_time + '.html'
with open(report, "wb") as outfile:
    runner = HTMLTestRunner(stream=outfile, title=u"GB-PC-PAY_UI表单校验测试报告", description=u"用例执行情况：", verbosity=2, retry=0, save_last_try=False)
    runner.run(suite)

e = Email(path=report, message='''
本邮件是支付UI自动化测试报告，请下载或者使用浏览器查看附件内容. 
如果有任何问题，请及时联系：测试组. Thank you! 

-------------------------------------------- 
深圳市环球易购电子商务有限公司 
技术中心\电子项目部\质量管控组 
姜家豪 
TEL：18682436420 
Email：jiangjiahao@globalegrow.com 
''')
e.send()




