import unittest
from selenium import webdriver
from UI_AUTOMATION.utils.config import DRIVER_PATH
from UI_AUTOMATION.test.page.PC.gb_pc_base_case import GBBaseCase
from UI_AUTOMATION.test.page.pageconfig.connect import GBConnect
from UI_AUTOMATION.test.page.PC import *
# from UI_AUTOMATION.test.page.form
# from ..page.form.form_pc import *

# unittest.TestCase
class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # option = webdriver.ChromeOptions()
        # option.add_argument('headless')  # 静默模式
        # cls.driver = webdriver.Chrome(chrome_options=option)
        DRIVER = DRIVER_PATH + '\chromedriver.exe'
        GECKO = DRIVER_PATH + '\geckodriver.exe'
        # self.driver = webdriver.Chrome(executable_path=DRIVER)
        cls.driver = webdriver.Chrome(executable_path=DRIVER)

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        pass
    # def add_img(self):
    #     self.imgs.append(self.driver.get_screenshot_as_base64())
    #     return True

    def setUp(self):
        # 在是python3.x 中，如果在这里初始化driver ，因为3.x版本 unittest 运行机制不同，会导致用力失败时截图失败
        self.imgs = []
        self.addCleanup(self.cleanup)

    def cleanup(self):
        pass

    def login_GB(self):
        GBBaseCase(self.driver).gb_login()

    def test_GB_wallet(self):
        '''电子钱包支付'''
        GBConnect().GB_adress_Turkey()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_wallet()
        GBBaseCase(self.driver).gb_checkorder()

    def test_GB_paypal(self):
        '''普通paypal'''
        GBConnect().GB_adress_Turkey()
        # GBBaseCase(self.driver).gb_login()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).paymentplatform()
        GBBaseCase(self.driver).third_paypal()
        GBBaseCase(self.driver).gb_checkorder()

    def test_GB_paypal_fast(self):
        '''快捷paypal'''
        GBConnect().GB_adress_Turkey()
        # GBBaseCase(self.driver).gb_login()
        GBBaseCase(self.driver).gb_goodtopaypal()
        GBBaseCase(self.driver).third_paypal()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).gb_checkorder()

    def test_GB_creditcard(self):
        '''信用卡creditcard'''
        GBConnect().GB_adress_Turkey()
        GBConnect().GB_creditcard()
        GBConnect().GB_CREDITCARD_channel_checkout_credit()
        # GBBaseCase(self.driver).obs_creditchannel_creditcard()
        # GBBaseCase(self.driver).gb_login()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_creditcard()
        GBBaseCase(self.driver).gb_checkorder()

    def test_GB_worldpay(self):
        '''信用卡worldpay'''
        GBConnect().GB_adress_Turkey()
        GBConnect().GB_worldpay()
        GBConnect().GB_CREDITCARD_channel_worldpay()
        # GBBaseCase(self.driver).gb_login()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_worldpay()
        GBBaseCase(self.driver).gb_checkorder()

    def test_GB_ADN_CC(self):
        '''信用卡ADN_CC'''
        GBConnect().GB_adress_Turkey()
        GBConnect().GB_ADN_CC()
        GBConnect().GB_CREDITCARD_channel_ADN_CC()
        # GBBaseCase(self.driver).gb_login()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_adn_cc()
        GBBaseCase(self.driver).gb_checkorder()

    def test_GB_GC(self):
        '''信用卡GC'''
        GBConnect().GB_adress_Turkey()
        GBConnect().GB_GC()
        GBConnect().GB_CREDITCARD_channel_GC()
        # GBBaseCase(self.driver).gb_login()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_GC()
        GBBaseCase(self.driver).gb_checkorder()

    def test_GB_ebanxinstalment(self):
        '''巴西分期ebanxinstalment'''
        GBConnect().GB_adress_Brazil()
        # GBConnect().GB_sort_Brazil()
        # GBBaseCase(self.driver).gb_login()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_ebanxinstalment()
        GBBaseCase(self.driver).gb_checkorder()

    def test_GB_boleto(self):
        '''boleto支付'''
        GBConnect().GB_adress_Brazil()
        # GBConnect().GB_sort_Brazil()
        # GBBaseCase(self.driver).gb_login()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_boleto()
        # GBBaseCase(self.driver).gb_checkorder_Submitting()
        GBBaseCase(self.driver).gb_checkorder()

    def test_GB_ADN_PTMB(self):
        '''ADN_PTMB支付'''
        GBConnect().GB_adress_Portugal()
        # GBBaseCase(self.driver).gb_login()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_ADN_PTMB()
        # GBBaseCase(self.driver).gb_checkorder_Submitting()
        GBBaseCase(self.driver).gb_checkorder()

    def test_GB_WP_24(self):
        ''' WP_24支付 '''
        GBConnect().GB_adress_Poland()
        # GBBaseCase(self.driver).gb_login()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_WP_24()
        # GBBaseCase(self.driver).gb_checkorder_pending()
        GBBaseCase(self.driver).gb_checkorder()


    def test_GB_ZYPaytm(self):
        '''ZYPaytm支付'''
        GBConnect().GB_adress_India()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_ZYPaytm()
        GBBaseCase(self.driver).gb_checkorder()

    def test_GB_PayU_INNB(self):
        '''PayU_INNB支付'''
        GBConnect().GB_adress_India()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_PayU_INNB()
        GBBaseCase(self.driver).gb_checkorder()

    def test_GB_ideal(self):
        '''ideal支付'''
        GBConnect().GB_adress_India()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_ideal()
        # GBBaseCase(self.driver).gb_checkorder_pending()
        GBBaseCase(self.driver).gb_checkorder()

    def test_GB_BANK_TRANSFER(self):
        '''BANK_TRANSFER支付'''
        GBConnect().GB_adress_India()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_BANK_TRANSFER()
        # GBBaseCase(self.driver).gb_checkorder_pending()
        GBBaseCase(self.driver).gb_checkorder()

    def test_GB_WESTERN(self):
        '''WESTERN支付'''
        GBConnect().GB_adress_India()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_WESTERN()
        # GBBaseCase(self.driver).gb_checkorder_pending()
        GBBaseCase(self.driver).gb_checkorder()

    def test_PayU_TRCC(self):
        '''PayU_TRCC支付'''
        GBConnect().GB_adress_Turkey()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_PayU_TRCC()
        # GBBaseCase(self.driver).gb_checkorder_pending()
        GBBaseCase(self.driver).gb_checkorder()


    def test_PayU_BKM(self):
        '''PayU_BKM支付'''
        GBConnect().GB_adress_Turkey()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_PayU_BKM()
        # GBBaseCase(self.driver).gb_checkorder_pending()
        GBBaseCase(self.driver).gb_checkorder()


    def test_EBX_MXCC(self):
        '''EBX_MXCC支付'''
        GBConnect().GB_adress_Mexico()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_EBX_MXCC()
        GBBaseCase(self.driver).gb_checkorder()


    def test_OXXO(self):
        '''OXXO支付'''
        GBConnect().GB_adress_Mexico()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_OXXO()
        # GBBaseCase(self.driver).gb_checkorder_Submitting()
        GBBaseCase(self.driver).gb_checkorder()


    def test_BankTransfer(self):
        '''BankTransfer支付'''
        GBConnect().GB_adress_Mexico()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_BankTransfer()
        # GBBaseCase(self.driver).gb_checkorder_Submitting()
        GBBaseCase(self.driver).gb_checkorder()


    def test_WP_QIWI(self):
        '''WP_QIWI支付'''
        GBConnect().GB_adress_Russian()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_WP_QIWI()
        # GBBaseCase(self.driver).gb_checkorder_pending()
        GBBaseCase(self.driver).gb_checkorder()


    def test_yandex_money(self):
        '''yandex_money支付'''
        GBConnect().GB_adress_Russian()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_yandex_money()
        GBBaseCase(self.driver).gb_checkorder()

    def test_ADN_RUCT(self):
        '''ADN_RUCT支付'''
        GBConnect().GB_adress_Russian()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_ADN_RUCT()
        # GBBaseCase(self.driver).gb_checkorder_Appreciate()
        GBBaseCase(self.driver).gb_checkorder()



    def test_ADN_IDATM(self):
        '''ADN_IDATM支付'''
        GBConnect().GB_adress_Indonesia()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_ADN_IDATM()
        # GBBaseCase(self.driver).gb_checkorder_Submitting()
        GBBaseCase(self.driver).gb_checkorder()


    def test_ADN_IDACS(self):
        '''ADN_IDACS支付'''
        GBConnect().GB_adress_Indonesia()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_ADN_IDACS()
        # GBBaseCase(self.driver).gb_checkorder_Submitting()
        GBBaseCase(self.driver).gb_checkorder()


    def test_PSE(self):
        '''PSE支付'''
        GBConnect().GB_adress_Colombia()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_PSE()
        GBBaseCase(self.driver).gb_checkorder()

    def test_EBX_AGPC(self):
        '''EBX_AGPC支付'''
        GBConnect().GB_adress_Argentina()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_EBX_AGPC()
        GBBaseCase(self.driver).gb_checkorder()


    def test_ADN_BEBC(self):
        '''ADN_BEBC支付'''
        GBConnect().GB_adress_Belgium()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_ADN_BEBC()
        GBBaseCase(self.driver).gb_checkorder()

    def test_EPS(self):
        '''EPS支付'''
        GBConnect().GB_adress_Austria()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_EPS()
        GBBaseCase(self.driver).gb_checkorder()

    def test_SOFORT_SSL(self):
        '''SOFORT_SSL支付'''
        GBConnect().GB_adress_Austria()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_SOFORT_SSL()
        GBBaseCase(self.driver).gb_checkorder()

    def test_ADN_DEGP(self):
        '''ADN_DEGP支付'''
        GBConnect().GB_adress_Germany()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_ADN_DEGP()
        GBBaseCase(self.driver).gb_checkorder()

    def test_WP_DEGP(self):
        '''WP_DEGP支付'''
        GBConnect().GB_adress_Germany()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_WP_DEGP()
        GBBaseCase(self.driver).gb_checkorder()


    def test_LipaPay(self):
        '''LipaPay支付'''
        GBConnect().GB_adress_Nigeria()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_LipaPay()
        GBBaseCase(self.driver).gb_checkorder()

    def test_ADN_MYOB(self):
        '''ADN_MYOB支付'''
        GBConnect().GB_adress_Malaysia()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_ADN_MYOB()
        GBBaseCase(self.driver).gb_checkorder()

    def test_ADN_THOB(self):
        '''ADN_THOB支付'''
        GBConnect().GB_adress_Thailand()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_ADN_THOB()
        GBBaseCase(self.driver).gb_checkorder()

    def test_EBX_SVPG(self):
        '''EBX_SVPG支付'''
        GBConnect().GB_adress_Chile()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_EBX_SVPG()
        GBBaseCase(self.driver).gb_checkorder()

    def test_ADN_TRSP(self):
        '''ADN_TRSP支付'''
        GBConnect().GB_adress_Slovakia()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_ADN_TRSP()
        GBBaseCase(self.driver).gb_checkorder()

    def test_Postepay(self):
        '''Postepay(WP_PSTP)支付'''
        GBConnect().GB_adress_Italy()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_Postepay()
        GBBaseCase(self.driver).gb_checkorder()

    def test_PagoEfectivo(self):
        '''PagoEfectivo支付'''
        GBConnect().GB_adress_Peru()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_PagoEfectivo()
        GBBaseCase(self.driver).gb_checkorder()

    def test_SQ_ESCC1(self):
        '''SQ_ESCC1支付'''
        GBConnect().GB_adress_Spain()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_SQ_ESCC1()
        GBBaseCase(self.driver).gb_checkorder()

    def test_SQ_ESCC2(self):
        '''SQ_ESCC2支付'''
        GBConnect().GB_adress_Spain()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_SQ_ESCC2()
        GBBaseCase(self.driver).gb_checkorder()

    def test_Zero_OrderPayment(self):
        '''Zero_OrderPayment支付'''
        # GBConnect().GB_adress_Malaysia()
        GBConnect().GB_adress_US()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).payment_Zero_OrderPayment()
        GBBaseCase(self.driver).gb_checkorder()

    def test_poli(self):
        '''poli支付'''
        GBConnect().GB_adress_Brazilpoli()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_poli()
        GBBaseCase(self.driver).gb_checkorder()

    def test_Webmoney(self):
        '''Webmoney支付'''
        GBConnect().GB_adress_Turkey()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_Webmoney()

    def test_DLC_Boleto(self):
        '''DLC_Boleto支付'''
        GBConnect().GB_adress_Brazil()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_DLC_Boleto()
        GBBaseCase(self.driver).gb_checkorder()

    def test_WP_SOFORT_SW(self):
        '''WP_SOFORT_SW支付'''
        GBConnect().GB_adress_Switzerland()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_WP_SOFORT_SW()
        GBBaseCase(self.driver).gb_checkorder()

    def test_WP_PTMB(self):
        '''WP_PTMB支付'''
        GBConnect().GB_adress_Portugal()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_WP_PTMB()
        GBBaseCase(self.driver).gb_checkorder()

    def test_PayU_UPI(self):
        '''PayU_UPI支付'''
        GBConnect().GB_adress_India()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_PayU_UPI()

    def test_DGPAY_PHdp(self):
        '''PayU_UPI支付'''
        GBConnect().GB_adress_Philippines()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_DGPAY_PHdp()

    def test_WPG_Pay(self):
        '''WPG_Pay支付'''
        GBConnect().GB_adress_Brazil()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).payment_WPG_Pay()



if __name__ == "__main__":
    unittest.main()
    # BaseTestCase().test_GB_paypal_fast()
    # BaseTestCase().test_formtest()
    # BaseTestCase().test_GB_wallet()

