import unittest
from selenium import webdriver
from UI_AUTOMATION.test.page.PC.gb_pc_base_case import GBBaseCase
from UI_AUTOMATION.test.page.pageconfig.connect import GBConnect
# from UI_AUTOMATION.test.page.form
from ..page.form.form_pc import *

class FormTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # option = webdriver.ChromeOptions()
        # option.add_argument('headless')  # 静默模式
        # cls.driver = webdriver.Chrome(chrome_options=option)

        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        pass

    # def add_img(self):
    #     self.imgs.append(self.driver.get_screenshot_as_base64())
    #     return True

    def setUp(self):
        self.imgs = []
        self.addCleanup(self.cleanup)


    def cleanup(self):
        pass


    def login_GB(self):
        GBBaseCase(self.driver).gb_login()



    def test_formtest_creditcard(self):
        '''信用卡表单校验'''
        # GBBaseCase(self.driver).gb_login()
        # GBConnect().GB_adress_Brazil()
        # GBBaseCase(self.driver).gb_goodtobuy()
        # GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).get_payurl()
        GBFormCase(self.driver).test_formtest_creditcard()


    def test_formtest_ebanxinstalment(self):
        '''巴西分期表单校验'''
        # GBConnect().GB_adress_Brazil()
        # GBBaseCase(self.driver).gb_goodtobuy()
        # GBBaseCase(self.driver).gb_placeorder()
        GBBaseCase(self.driver).get_payurl()
        GBFormCase(self.driver).test_formtest_ebanxinstalment()

    def test_formtest_boleto(self):
        '''boleto表单校验'''
        # GBConnect().GB_adress_Brazil()
        # GBBaseCase(self.driver).gb_goodtobuy()
        # GBBaseCase(self.driver).gb_placeorder()
        GBFormCase(self.driver).test_formtest_boleto()

    def test_formtest_ideal(self):
        '''ideal表单校验'''
        # GBConnect().GB_adress_Brazil()
        # GBBaseCase(self.driver).gb_goodtobuy()
        # GBBaseCase(self.driver).gb_placeorder()
        GBFormCase(self.driver).test_formtest_ideal()

    def test_formtest_pse(self):
        '''pse表单校验'''
        # GBConnect().GB_adress_Brazil()
        # GBBaseCase(self.driver).gb_goodtobuy()
        # GBBaseCase(self.driver).gb_placeorder()
        GBFormCase(self.driver).test_formtest_pse()




if __name__ == "__main__":
    unittest.main()

    # FormTestCase().test_formtest_creditcard()

