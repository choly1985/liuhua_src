import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from UI_AUTOMATION.test.page.M.gb_m_base_case import GBBaseCase
from UI_AUTOMATION.test.page.pageconfig.connect import GBConnect


class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        WIDTH = 320
        HEIGHT = 720
        PIXEL_RATIO = 3.0
        # UA = 'Mozilla/5.0 (Ljiangjiahaoinux; Android 4.1.1; GT-N7100 Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3'
        UA = 'Default'

        mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO},
                           "userAgent": UA}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        cls.driver = webdriver.Chrome(chrome_options=options)

        # option = webdriver.ChromeOptions()
        # option.add_argument('headless')  # 静默模式
        # cls.driver = webdriver.Chrome(chrome_options=option)

        # cls.driver = webdriver.Chrome()
        '''
        mobile_emulation = {
            # "deviceName": "iPhone 6"
            "deviceName": "iPhone X"
            # Or specify a specific build using the following two arguments
            # "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
            # "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
        }
        options = Options()
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        cls.driver = webdriver.Chrome(chrome_options=options)
        '''

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        pass


    def setUp(self):
        self.imgs = []
        self.addCleanup(self.cleanup)

    def cleanup(self):
        pass

    def login_GB(self):
        GBBaseCase(self.driver).gb_login()

    # def test_GB_wallet(self):
    #     '''电子钱包支付'''
    #     GBConnect().GB_adress_Turkey()
    #     # GBBaseCase(self.driver).gb_login()
    #     GBBaseCase(self.driver).gb_goodtobuy()
    #     GBBaseCase(self.driver).payment_wallet()
    #     GBBaseCase(self.driver).gb_checkorder()
    #
    # def test_GB_paypal_fast(self):
    #     '''paypal快捷支付'''
    #     GBConnect().GB_adress_Turkey()
    #     # GBBaseCase(self.driver).gb_login()
    #     GBBaseCase(self.driver).gb_goodtopaypal()
    #     GBBaseCase(self.driver).third_paypal()
    #     GBBaseCase(self.driver).gb_placeorder()
    #     GBBaseCase(self.driver).gb_checkorder()
    #
    # def test_GB_paypal(self):
    #     '''paypal支付'''
    #     GBConnect().GB_adress_Turkey()
    #     # GBBaseCase(self.driver).gb_login()
    #     GBBaseCase(self.driver).gb_goodtobuy()
    #     GBBaseCase(self.driver).payment_paypal()
    #     GBBaseCase(self.driver).third_paypal()
    #     GBBaseCase(self.driver).gb_checkorder()

    def test_GB_creditcard(self):
        '''信用卡creditcard支付'''
        GBConnect().GB_adress_Turkey()
        # GBConnect().GB_creditcard()
        GBBaseCase(self.driver).gb_login()
        GBBaseCase(self.driver).gb_goodtobuy()
        GBBaseCase(self.driver).payment_creditcard()
        GBBaseCase(self.driver).gb_checkorder()

if __name__ == "__main__":
    # unittest.main()
    # BaseTestCase().test_GB_paypal_fast()
    # BaseTestCase().test_GB_wallet()
    # BaseTestCase().test_GB_paypal()
    BaseTestCase().test_GB_creditcard()





