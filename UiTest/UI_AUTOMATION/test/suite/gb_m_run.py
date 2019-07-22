
import time
import unittest

from UI_AUTOMATION.test.testcase.gb_m_case import BaseTestCase
from UI_AUTOMATION.utils.HTMLTestRunner import HTMLTestRunner
from UI_AUTOMATION.utils.config import REPORT_PATH
from UI_AUTOMATION.utils.haoemail import Email

# # 构造测试集
suite = unittest.TestSuite()
suite.addTest(BaseTestCase('login_GB'))
#............................................................

# suite.addTest(BaseTestCase('test_GB_wallet'))
# suite.addTest(BaseTestCase('test_GB_paypal_fast'))
# suite.addTest(BaseTestCase('test_GB_paypal'))
suite.addTest(BaseTestCase('test_GB_creditcard'))




now_time = time.strftime('%Y%m%d-%H%M%S', time.localtime())
report = REPORT_PATH + '\\' + 'PAY_Report '+ now_time + '.html'
with open(report, "wb") as outfile:
    runner = HTMLTestRunner(stream=outfile, title=u"GB-M-PAY_UI测试报告", description=u"用例执行情况：", verbosity=2, retry=0, save_last_try=False)
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





