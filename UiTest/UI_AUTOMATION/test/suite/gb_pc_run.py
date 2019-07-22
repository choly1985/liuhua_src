import time
import unittest
from UI_AUTOMATION.test.testcase.gb_pc_case import BaseTestCase
from UI_AUTOMATION.utils.HTMLTestRunner import HTMLTestRunner
# from UI_AUTOMATION.utils.HTMLTestRunner_Chart import HTMLTestRunner
# from UI_AUTOMATION.utils.HTMLTestRunner_cn import HTMLTestRunner
# from UI_AUTOMATION.utils.ExtentHTMLTestRunner import HTMLTestRunner
import time
from UI_AUTOMATION.utils.config import REPORT_PATH
from UI_AUTOMATION.utils.haoemail import Email
from UI_AUTOMATION.test.page.pageconfig.CI import GBConnect



# # 构造测试集
suite = unittest.TestSuite()
suite.addTest(BaseTestCase('login_GB'))
#............................................................
time.sleep(2)
# suite.addTest(BaseTestCase('test_GB_wallet'))
# # suite.addTest(BaseTestCase('test_GB_paypal_fast'))
# suite.addTest(BaseTestCase('test_GB_paypal'))
# # suite.addTest(BaseTestCase('test_GB_creditcard'))
# suite.addTest(BaseTestCase('test_GB_worldpay'))
# # suite.addTest(BaseTestCase('test_GB_ADN_CC'))
# # suite.addTest(BaseTestCase('test_GB_GC'))
# suite.addTest(BaseTestCase('test_PayU_TRCC'))
# suite.addTest(BaseTestCase('test_GB_ebanxinstalment'))
# suite.addTest(BaseTestCase('test_GB_boleto'))
# # suite.addTest(BaseTestCase('test_GB_WP_24'))  ## #postepay wp-qiwi  wp-p24 和sofort不能同时存在,切换后正常,后台设置之后在执行
# # #
# # #
# suite.addTest(BaseTestCase('test_GB_PayU_INNB'))
# # suite.addTest(BaseTestCase('test_GB_ideal'))    #第三方不稳定
# suite.addTest(BaseTestCase('test_GB_BANK_TRANSFER'))
# suite.addTest(BaseTestCase('test_GB_WESTERN'))
# # # #
# suite.addTest(BaseTestCase('test_EBX_MXCC'))
# suite.addTest(BaseTestCase('test_OXXO'))
# # suite.addTest(BaseTestCase('test_BankTransfer'))   ### GC信用卡和GC-banktransfer只能开启一个,后台设置之后在执行
# # suite.addTest(BaseTestCase('test_WP_QIWI'))   ### #postepay wp-qiwi  wp-p24 和sofort不能同时存在,切换后正常,后台设置之后在执行
# suite.addTest(BaseTestCase('test_yandex_money'))
# suite.addTest(BaseTestCase('test_ADN_RUCT'))
# # #
# suite.addTest(BaseTestCase('test_PSE'))
# suite.addTest(BaseTestCase('test_EBX_AGPC'))  #1
# suite.addTest(BaseTestCase('test_ADN_BEBC'))  # 1
# suite.addTest(BaseTestCase('test_EPS'))
# suite.addTest(BaseTestCase('test_SOFORT_SSL'))   ### #postepay wp-qiwi  wp-p24 和sofort不能同时存在,切换后正常,后台设置之后在执行
# suite.addTest(BaseTestCase('test_ADN_DEGP'))
suite.addTest(BaseTestCase('test_WP_DEGP'))


# suite.addTest(BaseTestCase('test_LipaPay'))     # 第三方网址已换，报502暂时跑不了。
# suite.addTest(BaseTestCase('test_ADN_MYOB'))
# suite.addTest(BaseTestCase('test_ADN_THOB'))
# suite.addTest(BaseTestCase('test_EBX_SVPG'))
# # suite.addTest(BaseTestCase('test_Zero_OrderPayment'))   # 1 必须邮费为0元
# suite.addTest(BaseTestCase('test_ADN_TRSP'))
# # suite.addTest(BaseTestCase('test_Postepay')) ### #postepay wp-qiwi  wp-p24 和sofort不能同时存在,切换后正常,后台设置之后在执行
# suite.addTest(BaseTestCase('test_PagoEfectivo'))
# suite.addTest(BaseTestCase('test_SQ_ESCC1'))   #   同样第三方问题，跑不了
suite.addTest(BaseTestCase('test_SQ_ESCC2'))   #   同样第三方问题，跑不了,收银台不展示。
# suite.addTest(BaseTestCase('test_poli'))
# # # # # #
# suite.addTest(BaseTestCase('test_Webmoney'))   # 只可验证跳转
# # # # #
# suite.addTest(BaseTestCase('test_GB_ADN_PTMB'))
# suite.addTest(BaseTestCase('test_ADN_IDATM'))
# suite.addTest(BaseTestCase('test_ADN_IDACS'))
# # suite.addTest(BaseTestCase('test_PayU_BKM'))  # 第三方及其不稳定,建议单独执行。
# suite.addTest(BaseTestCase('test_WPG_Pay'))
#
# # suite.addTest(BaseTestCase('test_GB_ZYPaytm'))          #改服务器host ip才能支付成功
# suite.addTest(BaseTestCase('test_DLC_Boleto'))
# suite.addTest(BaseTestCase('test_WP_SOFORT_SW'))
# suite.addTest(BaseTestCase('test_WP_PTMB'))
# suite.addTest(BaseTestCase('test_PayU_UPI'))   # 只可验证跳转
# suite.addTest(BaseTestCase('test_DGPAY_PHdp'))   # 只可验证跳转




'''
def create_test_suite():
    test_list_path = "../testcase"
    test_unit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(test_list_path, pattern="test_*.py")
    for test_suite in discover:
        for test_case in test_suite:
            test_unit.addTest(test_case)
            print(test_case)

    return test_unit
all_test = create_test_suite()
'''

now_time = time.strftime('%Y%m%d-%H%M%S', time.localtime())
report = REPORT_PATH + '\\' + 'PAY_Report ' + now_time + '.html'
# print(report)

### 从代码执行结果里面获取数据      HTMLTestRunner
with open(report, "wb") as outfile:
    # runner = HTMLTestRunner(stream=outfile, title=u"GB-PC-PAY_UITest", description=u"用例执行情况：")
    runner = HTMLTestRunner(stream=outfile, title=u"GB-PC-PAY_UITest", description=u"用例执行情况：", verbosity=2, retry=0, save_last_try=True)
    aa = runner.run(suite)
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
print('''***CI确认发送：‘y’***\n***CI不发送  ：‘n’***''')
while 1:
    choose = input('输入命令：')
    if choose == 'y' and 'Y':
        print("CI已发送！")
        break
    if choose == 'n' and 'N':
        print("CI已取消发送，并程序结束！！！")
        exit(0)
    else:
        print("输入命令有误，请重新输入!")
conn = GBConnect()    ##发CI接口
conn.CI_pc_date(runner, aa)



