from UI_AUTOMATION.utils.config import Config
from selenium.webdriver.support.ui import Select
import pymysql
from UI_AUTOMATION.test.page.pageconfig.haoselenium import *
from UI_AUTOMATION.utils.config import Config
from selenium.webdriver.support.wait import WebDriverWait
from UI_AUTOMATION.test.page.pageconfig.connect import GBConnect
from UI_AUTOMATION.test.page.base_page import *
from UI_AUTOMATION.test.page.PC.pc_locators import *
from UI_AUTOMATION.test.page.PC.pc_home_page import *


class GBBaseCase(BasePage):
    def __init__(self, driver):
        self.Connection = 'keep-alive'
        self.driver = driver

        c = Config().get('GB')
        self.ua = c.get('UA')
        self.url = c.get('GBURL')
        self.username = c.get('GBusername')
        self.password = c.get('GBpassword')
        self.GBloginURL = c.get('GBloginURL')
        self.GBgood = c.get('GBgood')
        self.PPusername = c.get('PPusername')
        self.PPpassword = c.get('PPpassword')
        self.GBselfcenter = c.get('GBselfcenter')
        self.userId = c.get('userId')

        c = Config().get('mysql')
        self.host = c.get('host')
        self.post = c.get('post')
        self.user = c.get('user')
        self.passwd = c.get('passwd')
        self.db = c.get('db')
        # print(self.userId)

    def add_img(self):
        self.imgs.append(self.get_screenshot_as_base64())
        return True

    def gb_login(self):
        # self.headers = {'User-Agent': self.ua}
        # self.driver = driver

        pc = HomePage(self.driver)
        lg = LoginPage(self.driver)
        pc.get(self.GBloginURL)
        # self.add_img()
        # pc.close_pop_win()  #关闭弹窗
        # pc.sign_in()       #点击进入登录页面
        lg.login(self.username, self.password)
        # WebDriverWait(self.driver, 10).until(EC.title_is("GearBest: Online Shopping - Best Gear at Best Prices"))
        sleep(1)

    def gb_goodtobuy(self):
        # self.driver.refresh()
        sleep(0.5)
        # self.driver.set_page_load_timeout(5)
        try:
            self.driver.get(self.GBgood)
            b = 0
            while b != 5:
                try:
                    self.find_element(*GoodsInfoPageLoc.buy_button)
                    b = 5
                except:
                    b = b + 1
                    self.driver.refresh()
                    sleep(1)
        except TimeoutException:
            self.driver.execute_script('window.stop()')
        # self.driver.execute_script("var q=document.body.scrollTop=300")

        self.find_element(*GoodsInfoPageLoc.buy_button)
        try:
            self.click(*GoodsInfoPageLoc.num_plus)
            self.click(*GoodsInfoPageLoc.buy_button)
        except:
            self.driver.refresh()
            self.click(*GoodsInfoPageLoc.num_plus)
            self.click(*GoodsInfoPageLoc.buy_button)
        sleep(4)

    def gb_goodtopaypal(self):
        self.driver.set_page_load_timeout(5)
        # self.driver.refresh()
        sleep(2)
        try:
            self.get(self.GBgood)
            b = 0
            while b != 5:
                try:
                    self.find_element_now(*GoodsInfoPageLoc.paypal_button)
                    self.click(*GoodsInfoPageLoc.paypal_button)
                    b = 5
                except:
                    b = b + 1
                    self.driver.refresh()
                    sleep(1)
        except TimeoutException:
            self.driver.execute_script('window.stop()')

        self.find_element(*GoodsInfoPageLoc.paypal_button)
        try:
            self.click(*GoodsInfoPageLoc.num_plus)
            self.click(*GoodsInfoPageLoc.paypal_button)
        except:
            self.driver.refresh()
            self.click(*GoodsInfoPageLoc.num_plus)
            self.click(*GoodsInfoPageLoc.paypal_button)

        sleep(5)

    def gb_placeorder(self):
        # self.headers = {'User-Agent': self.ua}
        # self.driver.execute_script("var q=document.documentElement.scrollTop=500")
        sleep(1)
        # try:
        #     self.driver.switch_to.alert
        #     self.driver.switch_to.alert.accept()  # 点击弹出上面的X按钮
        # except:
        #     pass
        try:
            self.click(*PlaceInfoPageLoc.place_button)  # pleace your order
        except:
            self.driver.refresh()
            sleep(1)
            self.driver.execute_script("var q=document.documentElement.scrollTop=500")
            try:
                self.click(*PlaceInfoPageLoc.place_button)  # pleace your order
            except:
                self.driver.refresh()
                sleep(1)
                self.click(*PlaceInfoPageLoc.place_button)  # pleace your order
        sleep(4)

    def get_payurl(self):
        # self.headers = {'User-Agent': self.ua}
        url = GBConnect().GB_payurl()
        self.get(url)
        self.driver.maximize_window()
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        print('收银台url：', self.driver.current_url)
        sleep(0.5)

    def get_payurl_m(self):
        # self.headers = {'User-Agent': self.ua}
        url = GBConnect().GB_payurl()
        self.get(url)
        # self.driver.maximize_window()
        # self.find_element(*PaymentInfoPageLoc.pay_button)
        # self.driver.refresh()
        print('收银台url：', self.driver.current_url)
        sleep(0.5)

    def paymentplatform(self):
        # self.headers = {'User-Agent': self.ua}
        self.find_element(*PaymentInfoPageLoc.pay_button)
        print('收银台url：', self.driver.current_url)
        try:
            self.click(*PaymentInfoPageLoc.paypal_src)
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 点击购买  placeOrder btn block toPayBtn
        except Exception as msg:
            print(u"异常原因%s" % msg)
            pamentordersn = self.driver.find_element_by_xpath("//*[@class='pc_orderinf']/dl[1]/dd").text
            print("收银台订单号：", pamentordersn)
            # BaseTestCase.add_img()
            self.add_img()
            raise
        sleep(2)

    def obs_credit_channel(self, channel1):
        js = 'window.open("http://www.obs-pay.com");'  # 通过执行js，开启一个新的窗口
        self.driver.execute_script(js)
        pay_windows = self.driver.current_window_handle
        window_1 = self.driver.current_window_handle
        # 获得打开的所有的窗口句柄
        windows = self.driver.window_handles
        # 切换到最新的窗口
        for current_window in windows:
            if current_window != window_1:
                self.driver.switch_to.window(current_window)
        # self.get("http://www.obs-pay.com")
        sleep(1)
        # obs_handle = self.driver.current_window_handle
        # self.obs_handle = obs_handle
        # sleep(0.5)
        self.driver.find_element_by_xpath("//*[@name='username']").send_keys("zhangwei")
        self.driver.find_element_by_xpath("//*[@name='password']").send_keys("zhang1wei")
        sleep(0.5)
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        sleep(1)
        self.driver.get("http://www.obs-pay.com/#/pay/channel-platform-country/list")
        sleep(1.5)
        self.driver.find_element_by_xpath("//*[contains(text(),'Turkey')]/../../td[5]/div/button[1]/span").click()
        sleep(0.5)
        start_ele = '//*[contains(text(), "%s")]' % channel1
        end_ele = '//*[contains(text(), "%s")]/../li[1]' % channel1
        start = self.driver.find_element_by_xpath(start_ele)
        end = self.driver.find_element_by_xpath(end_ele)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(start, end)
        actions.perform()
        sleep(0.5)
        self.driver.find_element_by_xpath("//*[contains(text(),'确定')]").click()
        sleep(0.5)
        self.driver.close()
        self.driver.switch_to.window(pay_windows)

    def payment_creditcard(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        self.obs_credit_channel("checkout_credit")
        # pay_windows = self.driver.current_window_handle
        # GBBaseCase.obs_creditcard()
        # sleep(0.5)
        # self.driver.switch_to.window(pay_windows)
        self.click(*PaymentInfoPageLoc.creditcard_src)
        self.send_keys("hao", *PaymentInfoPageLoc.creditcard_holder)
        self.send_keys("6011111111111117", *PaymentInfoPageLoc.creditcard_Number)
        self.send_keys("100", *PaymentInfoPageLoc.creditcard_Code)
        self.send_Skeys("4", *PaymentInfoPageLoc.creditcard_mouth)
        self.send_Skeys("2035", *PaymentInfoPageLoc.creditcard_day)
        sleep(0.8)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(4)

    def payment_worldpay(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        self.obs_credit_channel("worldpay")
        # GBBaseCase.obs_credit_channel(self, "worldpay")
        self.click(*PaymentInfoPageLoc.creditcard_src)
        self.send_keys("hao", *PaymentInfoPageLoc.creditcard_holder)
        self.send_keys("4444333322221111", *PaymentInfoPageLoc.creditcard_Number)
        self.send_keys("111", *PaymentInfoPageLoc.creditcard_Code)
        self.send_Skeys("5", *PaymentInfoPageLoc.creditcard_mouth)
        self.send_Skeys("2020", *PaymentInfoPageLoc.creditcard_day)
        sleep(0.8)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(4)


    def payment_adn_cc(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        self.obs_credit_channel("ADN_CC")
        self.click(*PaymentInfoPageLoc.creditcard_src)
        self.send_keys("hao", *PaymentInfoPageLoc.creditcard_holder)
        self.send_keys("4111111111111111", *PaymentInfoPageLoc.creditcard_Number)
        self.send_keys("737", *PaymentInfoPageLoc.creditcard_Code)
        self.send_Skeys("10", *PaymentInfoPageLoc.creditcard_mouth)
        self.send_Skeys("2020", *PaymentInfoPageLoc.creditcard_day)
        sleep(0.8)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(4)

    def payment_GC(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        self.obs_credit_channel("GC")
        self.click(*PaymentInfoPageLoc.creditcard_src)
        self.send_keys("hao", *PaymentInfoPageLoc.creditcard_holder)
        self.send_keys("5200000000000007", *PaymentInfoPageLoc.creditcard_Number)
        self.send_keys("111", *PaymentInfoPageLoc.creditcard_Code)
        self.send_Skeys("10", *PaymentInfoPageLoc.creditcard_mouth)
        self.send_Skeys("2020", *PaymentInfoPageLoc.creditcard_day)
        sleep(0.8)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(8)
        title = self.driver.title
        # title = EC.title_is('GearBest: Online Shopping - Best Gear at Best Prices')
        print(title, "title")
        if title == 'GearBest: Online Shopping - Best Gear at Best Prices':
            sleep(8)
            try:
                self.switch_frame(self.driver.find_element_by_id('authWindow'))
            except:
                pass
            self.send_keys("1234", *ThirdInfoPageLoc.GC_password)
            self.send_keys("1234", *ThirdInfoPageLoc.GC_Entry)
            sleep(4)
        else:
            pass


    def payment_ebanxinstalment(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        self.click(*PaymentInfoPageLoc.ebanxinstalment_src)
        self.click(*PaymentInfoPageLoc.ebanxinstalment_installments)
        self.send_keys("04268600558", *PaymentInfoPageLoc.ebanxinstalment_CPF)
        self.send_keys("hao", *PaymentInfoPageLoc.ebanxinstalment_Titular)
        self.send_keys("4111111111111111", *PaymentInfoPageLoc.ebanxinstalment_Nmero)
        self.send_keys("111", *PaymentInfoPageLoc.ebanxinstalment_Cdigo)
        self.send_Skeys("5", *PaymentInfoPageLoc.ebanxinstalment_Month)
        self.send_Skeys("2020", *PaymentInfoPageLoc.ebanxinstalment_Year)
        self.click(*PaymentInfoPageLoc.pay_button)

        sleep(5)

    def payment_PayU_TRCC(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        self.click(*PaymentInfoPageLoc.TRCC_src)
        self.send_keys("4355084355084358", *PaymentInfoPageLoc.TRCC_Number)
        self.driver.execute_script("var q=document.body.scrollTop=500")
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(5)
        self.click(*PaymentInfoPageLoc.pay_button)

        self.click(*PaymentInfoPageLoc.TRCC_Installments)
        self.click(*PaymentInfoPageLoc.TRCC_select)

        self.send_Skeys("12", *PaymentInfoPageLoc.TRCC_Month)
        self.send_Skeys("2019", *PaymentInfoPageLoc.TRCC_Year)
        self.send_keys("000", *PaymentInfoPageLoc.TRCC_code)
        self.send_keys("hao", *PaymentInfoPageLoc.TRCC_holder)
        self.click(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.pay_currencyselect)
        self.click(*PaymentInfoPageLoc.pay_currencyconfirm)
        self.click(*PaymentInfoPageLoc.pay_button)

        sleep(5)
        try:
            selenium_wait.is_clickable(self, "//*[@id='submitbutton']")
            self.driver.find_element_by_xpath('//*[@name="password"]').send_keys('a')
            self.driver.find_element_by_id('submitbutton').click()
            sleep(1)
        except:
            pass
        try:
            self.driver.switch_to.alert
            self.driver.switch_to.alert.accept()  # 点击弹出上面的X按钮
        except BaseException:
            pass
        sleep(5)

    def payment_PayU_BKM(self):

        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(1)
        print('收银台url：', self.driver.current_url)

        self.click(*PaymentInfoPageLoc.BKM_src)
        self.click(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.BKM_select)
        self.click(*PaymentInfoPageLoc.BKM_select1)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(2)
        self.driver.set_page_load_timeout(14)
        try:
            self.find_element(*ThirdInfoPageLoc.BKM_loginBtn)
        except TimeoutException:
            self.driver.execute_script('window.stop()')
        try:
            self.click(*ThirdInfoPageLoc.BKM_loginBtn)
            self.driver.implicitly_wait(5)
            self.send_keys('neticaret3@bkm.com', *ThirdInfoPageLoc.BKM_username)
            self.send_keys('147258', *ThirdInfoPageLoc.BKM_passwordPwd)
        except:
            self.driver.refresh()
            sleep(2)
            self.send_keys('neticaret5@bkm.com', *ThirdInfoPageLoc.BKM_username)
            self.send_keys('147258', *ThirdInfoPageLoc.BKM_passwordPwd)
        sleep(1)
        try:
            self.click(*ThirdInfoPageLoc.BKM_loginBtn)
        except:
            pass
        self.driver.set_page_load_timeout(10)
        try:
            self.find_element(*ThirdInfoPageLoc.BKM_submit)
        except TimeoutException:
            self.driver.execute_script('window.stop()')
        EC.title_contains("BKM Express")
        sleep(2)
        try:
            self.click(*ThirdInfoPageLoc.BKM_installmentselect)
            sleep(0.3)
        except:
            self.driver.refresh()
            self.click(*ThirdInfoPageLoc.BKM_installmentselect)
            sleep(0.3)
        self.click(*ThirdInfoPageLoc.BKM_submitcard)
        self.driver.set_page_load_timeout(10)
        try:
            self.find_element(*ThirdInfoPageLoc.BKM_submit)
        except TimeoutException:
            self.driver.execute_script('window.stop()')
        sleep(3)
        try:
            self.click(*ThirdInfoPageLoc.BKM_submit)
            self.send_keys("123456", ThirdInfoPageLoc.BKM_otp)
        except:
            self.driver.refresh()
            sleep(2)
            self.send_keys("123456", ThirdInfoPageLoc.BKM_otp)
        sleep(1)
        try:
            self.click(*ThirdInfoPageLoc.BKM_submitcard)
        except:
            pass
        sleep(3)


    def payment_boleto(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)

        self.click(*PaymentInfoPageLoc.boleto_src)
        self.send_keys("04268600558", *PaymentInfoPageLoc.boleto_cpf)
        self.click(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.boleto_select)
        self.click(*PaymentInfoPageLoc.boleto_select1)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(4)


    def payment_ADN_PTMB(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        self.find_element(*PaymentInfoPageLoc.PTMB_src)
        self.click(*PaymentInfoPageLoc.PTMB_src)
        self.click(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.PTMB_select)
        self.click(*PaymentInfoPageLoc.PTMB_select1)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(4)
        self.send_keys("5@ee.com", *ThirdInfoPageLoc.PTMB_shopperEmail)
        self.click(*ThirdInfoPageLoc.PTMB_mainSubmit)
        sleep(2)
        self.click(*ThirdInfoPageLoc.PTMB_mainSubmit)
        sleep(3)

    def payment_WP_PTMB(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        self.find_element(*PaymentInfoPageLoc.WP_PTMB_src)
        self.click(*PaymentInfoPageLoc.WP_PTMB_src)
        self.click(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.PTMB_select)
        self.click(*PaymentInfoPageLoc.PTMB_select1)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(4)
        self.click(*ThirdInfoPageLoc.WP24_contiun)
        sleep(3)

    def payment_WP_24(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        self.click(*PaymentInfoPageLoc.WP24_src)
        self.click(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.WP24_select)
        self.click(*PaymentInfoPageLoc.WP24_select1)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(6)
        self.click(*ThirdInfoPageLoc.WP24_contiun)
        sleep(5)


    def payment_wallet(self):

        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        sleep(0.5)
        try:
            self.click(*PaymentInfoPageLoc.Wallet_ele)
            self.send_keys(123456, *PaymentInfoPageLoc.Wallet_input)
            self.click(*PaymentInfoPageLoc.pay_button)
        except Exception as msg:
            print(u"异常原因%s" % msg)
            pamentordersn = self.driver.find_element_by_xpath("//*[@class='pc_orderinf']/dl[1]/dd").text
            print("收银台订单号：", pamentordersn)
            print('当前页面url：', self.driver.current_url)
            raise
        sleep(4)

    def payment_ZYPaytm(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)

        try:
            self.driver.find_element_by_xpath('//*[@src="https://uidesign.gbtcdn.com/check_out/paytm.png?01"]').click()
            sleep(0.5)
            self.driver.find_element_by_xpath(
                "//*[@class='placeOrder btn block toPayBtn']").click()  # 点击购买  placeOrder btn block toPayBtn
            sleep(0.5)
            self.driver.find_element_by_xpath("//*[@class='currency_select']").click()  # 切换币种
            self.driver.find_element_by_xpath("//*[@class='currency_select']/option[2]").click()
            sleep(0.5)
            self.driver.find_element_by_xpath(
                "//*[@class='placeOrder btn block toPayBtn']").click()  # 点击购买  placeOrder btn block toPayBtn
        except Exception as msg:
            print(u"异常原因%s" % msg)
            pamentordersn = self.driver.find_element_by_xpath("//*[@class='pc_orderinf']/dl[1]/dd").text
            print("收银台订单号：", pamentordersn)
            print('当前页面url：', self.driver.current_url)
            self.add_img()
            raise
        sleep(2)
        selenium_wait.is_clickable(self, "//*[@id='dcSubmit']")
        try:
            self.driver.find_element_by_xpath("//*[@id='cn1']").send_keys('4444333322221111')
            sleep(1)
            Select(self.driver.find_element_by_xpath("//*[@id='dcExpMonth']")).select_by_value("05")
            Select(self.driver.find_element_by_xpath("//*[@id='dcExpYear']")).select_by_value("2020")
            sleep(0.5)
            self.driver.find_element_by_xpath("//*[@id='dcCvvBox']").send_keys('123')
            sleep(0.5)
            self.driver.find_element_by_xpath("//*[@id='dcSubmit']").click()
            sleep(2)
            selenium_wait.is_clickable(self, "//*[@type='submit']")
            self.driver.find_element_by_id('OTP').send_keys('123123')
            self.driver.find_element_by_xpath("//*[@type='submit']").click()

        except Exception as msg:
            print(u"异常原因%s" % msg)
            pamentordersn = self.driver.find_element_by_xpath("//*[@class='pc_orderinf']/dl[1]/dd").text
            print("收银台订单号：", pamentordersn)
            print('当前页面url：', self.driver.current_url)
            self.add_img()
            raise
        sleep(2)

    def payment_PayU_INNB(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        self.click(*PaymentInfoPageLoc.INNB_src)
        Select(self.driver.find_element_by_xpath('//*[@name="payuInnbBankCode"]')).select_by_visible_text(
            "Andhra Bank")
        self.click(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.pay_currencyselect)
        self.click(*PaymentInfoPageLoc.pay_currencyconfirm)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(2)
        self.find_element(*ThirdInfoPageLoc.INNB_successButton)
        try:
            self.click(*ThirdInfoPageLoc.INNB_successButton)
        except:
            pass
        sleep(2)


    def payment_ideal(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        self.click(*PaymentInfoPageLoc.ideal_src)
        self.send_Skeys("INGBNL2A", *PaymentInfoPageLoc.ideal_Bank)
        self.click(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.pay_currencyselect)
        self.click(*PaymentInfoPageLoc.pay_currencyconfirm)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(2)
        self.find_element(*ThirdInfoPageLoc.ideal_submit)
        self.click(*ThirdInfoPageLoc.ideal_submit)
        sleep(4)


    def payment_EBX_MXCC(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        self.find_element(*PaymentInfoPageLoc.MXCC_src)
        self.click(*PaymentInfoPageLoc.MXCC_src)
        self.send_keys("hhhhhh", *PaymentInfoPageLoc.MXCC_titular)
        self.send_keys("4111111111111111", *PaymentInfoPageLoc.MXCC_Nmero)
        self.send_Skeys("12", *PaymentInfoPageLoc.MXCC_mouth)
        self.send_Skeys("2020", *PaymentInfoPageLoc.MXCC_year)
        self.send_keys("111", *PaymentInfoPageLoc.MXCC_Cdigo)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(4)


    def payment_OXXO(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        self.find_element(*PaymentInfoPageLoc.OXXO_src)
        self.click(*PaymentInfoPageLoc.OXXO_src)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(4)


    def payment_BankTransfer(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.BankTransfer_src)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(4)


    def payment_WP_QIWI(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.WPQIWI_src)
        self.send_keys("123456789", *PaymentInfoPageLoc.WPQIWI_phone)
        self.click(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.pay_currencyselect)
        self.click(*PaymentInfoPageLoc.pay_currencyconfirm)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(3)
        self.find_element(*ThirdInfoPageLoc.WPQIWI_makepayment)
        self.click(*ThirdInfoPageLoc.WPQIWI_makepayment)
        sleep(4)


    def payment_yandex_money(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.yandexmoney_src)
        self.click(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.pay_currencyselect)
        self.click(*PaymentInfoPageLoc.pay_currencyconfirm)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(8)
        self.find_element(*ThirdInfoPageLoc.yandexmoney_button)
        self.driver.refresh()
        sleep(1)
        self.send_keys("4444444444444448", *ThirdInfoPageLoc.yandexmoney_cardNumber)
        self.send_keys("12", *ThirdInfoPageLoc.yandexmoney_MM)
        self.send_keys("20", *ThirdInfoPageLoc.yandexmoney_YY)
        self.send_keys("111", *ThirdInfoPageLoc.yandexmoney_cardCvc)
        self.click(*ThirdInfoPageLoc.yandexmoney_button)
        self.click(*ThirdInfoPageLoc.yandexmoney_html)
        sleep(6)


    def payment_ADN_RUCT(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        self.click(*PaymentInfoPageLoc.RUCT_src)
        self.click(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.pay_currencyselect)
        self.click(*PaymentInfoPageLoc.pay_currencyconfirm)
        self.click(*PaymentInfoPageLoc.pay_button)
        self.find_element(*ThirdInfoPageLoc.RUCT_authorised)
        self.click(*ThirdInfoPageLoc.RUCT_authorised)
        sleep(5)


    def payment_ADN_IDATM(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        current_url1 = self.driver.current_url
        footerB = False
        while footerB == False:
            sleep(0.5)
            self.driver.refresh()
            self.get(current_url1)
            sleep(0.5)
            self.click(*PaymentInfoPageLoc.IDATM_src)
            sleep(0.2)
            self.click(*PaymentInfoPageLoc.pay_button)
            self.click(*PaymentInfoPageLoc.pay_currencyselect)
            self.click(*PaymentInfoPageLoc.pay_currencyconfirm)
            self.click(*PaymentInfoPageLoc.pay_button)
            sleep(5)
            self.find_element(*ThirdInfoPageLoc.IDATM_mainSubmit)
            self.click(*ThirdInfoPageLoc.IDATM_mainSubmit)
            self.send_keys("jiang", *ThirdInfoPageLoc.IDATM_firstName)
            self.send_keys("jiahao", *ThirdInfoPageLoc.IDATM_lastName)
            self.send_keys("jiangjiahao@globalegrowIn.com", *ThirdInfoPageLoc.IDATM_shopperEmail)
            sleep(1)
            try:
                self.click(*ThirdInfoPageLoc.IDATM_mainSubmit)
            except:
                pass
            sleep(4)
            footerB = selenium_wait.is_clickable(self, "//*[@class='footerB']")
        self.click(*ThirdInfoPageLoc.IDATM_footerB)
        self.driver.refresh()
        sleep(4)


    def payment_ADN_IDACS(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        current_url1 = self.driver.current_url
        footerB = False
        while footerB == False:
            sleep(0.5)
            self.driver.refresh()
            self.get(current_url1)
            sleep(0.5)
            self.click(*PaymentInfoPageLoc.IDACS_src)
            sleep(0.2)
            self.click(*PaymentInfoPageLoc.pay_button)
            self.click(*PaymentInfoPageLoc.pay_currencyselect)
            self.click(*PaymentInfoPageLoc.pay_currencyconfirm)
            self.click(*PaymentInfoPageLoc.pay_button)
            sleep(5)
            # self.find_element(*ThirdInfoPageLoc.IDATM_mainSubmit)
            # self.click(*ThirdInfoPageLoc.IDATM_mainSubmit)
            self.send_keys("jiang", *ThirdInfoPageLoc.IDACS_firstName)
            self.send_keys("jiahao", *ThirdInfoPageLoc.IDACS_lastName)
            self.send_keys("jiangjiahao@globalegrowIn.com", *ThirdInfoPageLoc.IDACS_shopperEmail)
            sleep(1)
            try:
                self.click(*ThirdInfoPageLoc.IDACS_mainSubmit)
            except:
                pass
            sleep(4)
            footerB = selenium_wait.is_clickable(self, "//*[@class='footerB']")
        self.click(*ThirdInfoPageLoc.IDATM_footerB)
        self.driver.refresh()
        sleep(4)

    def payment_PSE(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        print('收银台url：', self.driver.current_url)
        self.driver.refresh()
        sleep(0.5)
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.PSE_src)
        self.send_Skeys("banco_agrario", *PaymentInfoPageLoc.PSE_pseBankCode)
        self.send_Skeys("Cédula Ciudadana", *PaymentInfoPageLoc.PSE_documentType)
        self.send_keys("12", *PaymentInfoPageLoc.PSE_tel)
        self.click(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.pay_currencyselect)
        self.click(*PaymentInfoPageLoc.pay_currencyconfirm)
        self.click(*PaymentInfoPageLoc.pay_button)
        self.find_element(*ThirdInfoPageLoc.PSE_YES)
        self.click(*ThirdInfoPageLoc.PSE_YES)
        sleep(4)


    def payment_EBX_AGPC(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        self.click(*PaymentInfoPageLoc.AGPC_src)
        self.send_Skeys("CUIT", *PaymentInfoPageLoc.AGPC_select)
        self.send_keys("12345678901", *PaymentInfoPageLoc.AGPC_tel)
        self.click(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.pay_currencyselect)
        self.click(*PaymentInfoPageLoc.pay_currencyconfirm)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(2)


    def payment_ADN_BEBC(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        self.click(*PaymentInfoPageLoc.BEBC_src)
        self.send_keys("6703444444444449", *PaymentInfoPageLoc.BEBC_number)
        self.send_Skeys("10", *PaymentInfoPageLoc.BEBC_month)
        self.send_Skeys("2020", *PaymentInfoPageLoc.BEBC_year)
        self.send_keys("hao", *PaymentInfoPageLoc.BEBC_holder)
        self.click(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.pay_currencyselect)
        self.click(*PaymentInfoPageLoc.pay_currencyconfirm)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(3)
        self.driver.refresh()
        sleep(0.5)
        self.send_keys("user", *ThirdInfoPageLoc.BEBC_username)
        sleep(0.2)
        self.send_keys("password", *ThirdInfoPageLoc.BEBC_password)
        self.click(*ThirdInfoPageLoc.BEBC_submit)
        sleep(2)


    def payment_EPS(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        self.click(*PaymentInfoPageLoc.EPS_src)
        sleep(0.8)
        self.click(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.pay_currencyselect)
        self.click(*PaymentInfoPageLoc.pay_currencyconfirm)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(2)
        self.find_element(*ThirdInfoPageLoc.EPS_authorised)
        self.click(*ThirdInfoPageLoc.EPS_authorised)
        sleep(2)


    def payment_SOFORT_SSL(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        self.click(*PaymentInfoPageLoc.SOFORT_src)
        self.click(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.pay_currencyselect)
        self.click(*PaymentInfoPageLoc.pay_currencyconfirm)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(3)
        self.click(*ThirdInfoPageLoc.SOFORT_makepayment)
        sleep(2)



    def payment_ADN_DEGP(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        self.click(*PaymentInfoPageLoc.ADN_DEGP_src)
        self.click(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.pay_currencyselect)
        self.click(*PaymentInfoPageLoc.pay_currencyconfirm)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(4)
        # self.click(*ThirdInfoPageLoc.WP24_contiun)
        self.send_keys("Test", *ThirdInfoPageLoc.DEGP_bic_selection)
        # self.click(*ThirdInfoPageLoc.DEGP_mainSubmit)
        sleep(2)
        self.click(*ThirdInfoPageLoc.DEGP_Bank)
        self.click(*ThirdInfoPageLoc.DEGP_mainSubmit)
        sleep(2)
        self.send_keys("10", *ThirdInfoPageLoc.DEGP_sc)
        self.send_keys("4000", *ThirdInfoPageLoc.DEGP_extensionSc)
        self.send_keys("Any", *ThirdInfoPageLoc.DEGP_customerName1)
        self.send_keys("DE36444488881234567890", *ThirdInfoPageLoc.DEGP_customerIBAN)
        sleep(0.5)
        self.click(*ThirdInfoPageLoc.DEGP_submit)
        # self.driver.find_element_by_xpath(*ThirdInfoPageLoc.DEGP_submit).click()
        sleep(1)

    def payment_WP_DEGP(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        self.click(*PaymentInfoPageLoc.WP_DEGP_src)
        self.click(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.pay_currencyselect)
        self.click(*PaymentInfoPageLoc.pay_currencyconfirm)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(4)
        self.click(*ThirdInfoPageLoc.WP24_contiun)
        sleep(2)

    def payment_LipaPay(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        self.click(*PaymentInfoPageLoc.LipaPay_src)
        self.click(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.pay_currencyselect)
        self.click(*PaymentInfoPageLoc.pay_currencyconfirm)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(2)
        windows = self.driver.current_window_handle
        self.click(*ThirdInfoPageLoc.LipaPay_left)
        # sleep(1)
        # self.send_keys("jiangjiahao@globalegrowNG.com", *ThirdInfoPageLoc.LipaPay_email)
        sleep(0.5)
        self.click(*ThirdInfoPageLoc.LipaPay_btn)
        sleep(1)
        self.driver.switch_to.window(windows)
        sleep(2)
        self.driver.find_elements_by_xpath('//*[@id="dialogMain"]/div/a')[2].click()
        # sleep(2)
        # self.driver.find_elements_by_xpath('//*[@id="dialogMain"]/div/a')[2].click()
        sleep(3)
        self.click(*ThirdInfoPageLoc.LipaPay_shopping_btn)
        sleep(2)


    def payment_ADN_MYOB(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        print('收银台url：', self.driver.current_url)
        self.driver.refresh()
        sleep(0.5)
        self.click(*PaymentInfoPageLoc.MYOB_src)
        self.click(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.pay_currencyselect)
        self.click(*PaymentInfoPageLoc.pay_currencyconfirm)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(2)
        self.click(*ThirdInfoPageLoc.MYOB_authorised)
        sleep(2)


    def payment_ADN_THOB(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        print('收银台url：', self.driver.current_url)
        self.driver.refresh()
        sleep(0.5)
        self.click(*PaymentInfoPageLoc.THOB_src)
        self.click(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.pay_currencyselect)
        self.click(*PaymentInfoPageLoc.pay_currencyconfirm)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(2)
        self.click(*ThirdInfoPageLoc.MYOB_authorised)
        sleep(2)

    def payment_BANK_TRANSFER(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        print('收银台url：', self.driver.current_url)
        self.driver.refresh()
        sleep(0.5)
        self.click(*PaymentInfoPageLoc.BANK_TRANSFER_src)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(2)


    def payment_WESTERN(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        print('收银台url：', self.driver.current_url)
        self.driver.refresh()
        sleep(0.5)
        self.click(*PaymentInfoPageLoc.WESTERN_src)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(2)


    def payment_EBX_SVPG(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        print('收银台url：', self.driver.current_url)
        self.driver.refresh()
        sleep(0.5)
        self.click(*PaymentInfoPageLoc.EBX_SVPG_src)
        self.send_Skeys("RUT (Ról Único Tributário)", *PaymentInfoPageLoc.EBX_SVPG_doc)
        self.send_keys("12345678", *PaymentInfoPageLoc.EBX_SVPG_number)
        sleep(0.5)
        self.click(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.pay_currencyselect)
        self.click(*PaymentInfoPageLoc.pay_currencyconfirm)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(2)
        self.click(*ThirdInfoPageLoc.PSE_YES)
        sleep(2)

    def payment_ADN_TRSP(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        self.click(*PaymentInfoPageLoc.ADN_TRSP_src)
        self.send_Skeys("337", *PaymentInfoPageLoc.ADN_TRSP_issuerId)

        self.click(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.pay_currencyselect)
        self.click(*PaymentInfoPageLoc.pay_currencyconfirm)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(2)
        self.click(*ThirdInfoPageLoc.mainSubmit)
        sleep(2)

    def payment_Postepay(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        self.click(*PaymentInfoPageLoc.Postepay_src)
        self.click(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.pay_currencyselect)
        self.click(*PaymentInfoPageLoc.pay_currencyconfirm)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(5)
        self.click(*ThirdInfoPageLoc.WP24_contiun)
        sleep(2)


    def payment_PagoEfectivo(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        self.click(*PaymentInfoPageLoc.PagoEfectivo_src)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(2)



    def payment_SQ_ESCC1(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        self.click(*PaymentInfoPageLoc.SQ_ESCC1_src)
        self.click(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.pay_currencyselect)
        self.click(*PaymentInfoPageLoc.pay_currencyconfirm)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(4)
        self.driver.switch_to.frame(self.driver.find_element_by_id('sq-identification-pp3'))
        self.click(*ThirdInfoPageLoc.SQ_ESCC1_primary)
        sleep(0.5)
        self.click(*ThirdInfoPageLoc.SQ_ESCC1_primary)
        self.send_keys("Maria José", *ThirdInfoPageLoc.SQ_ESCC1_given_names)
        self.send_keys("Barroso Rajoy", *ThirdInfoPageLoc.SQ_ESCC1_surnames)
        self.send_keys("20/12/2020", *ThirdInfoPageLoc.SQ_ESCC1_date_of_birth)
        self.send_keys("12345678Z", *ThirdInfoPageLoc.SQ_ESCC1_nin)
        self.click(*ThirdInfoPageLoc.SQ_ESCC1_terms_accepted)
        # sleep(1)
        # self.click(*ThirdInfoPageLoc.SQ_ESCC1_primary)
        sleep(1.5)
        self.send_keys("55444", *ThirdInfoPageLoc.SQ_ESCC1_validation_code)
        self.click(*ThirdInfoPageLoc.SQ_ESCC1_primary)
        sleep(2.5)
        self.click(*ThirdInfoPageLoc.SQ_ESCC1_component)
        sleep(0.5)
        self.click(*ThirdInfoPageLoc.SQ_ESCC1_primary)
        sleep(10)

    def payment_SQ_ESCC2(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        self.click(*PaymentInfoPageLoc.SQ_ESCC1_src)
        self.click(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.pay_currencyselect)
        self.click(*PaymentInfoPageLoc.pay_currencyconfirm)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(4)
        self.driver.switch_to.frame(self.driver.find_element_by_id('sq-identification-pp3'))
        self.click(*ThirdInfoPageLoc.SQ_ESCC1_primary)
        sleep(0.5)
        self.click(*ThirdInfoPageLoc.SQ_ESCC1_primary)
        self.send_keys("Maria José", *ThirdInfoPageLoc.SQ_ESCC1_given_names)
        self.send_keys("Barroso Rajoy", *ThirdInfoPageLoc.SQ_ESCC1_surnames)
        self.send_keys("20/12/2020", *ThirdInfoPageLoc.SQ_ESCC1_date_of_birth)
        self.send_keys("12345678Z", *ThirdInfoPageLoc.SQ_ESCC1_nin)
        self.click(*ThirdInfoPageLoc.SQ_ESCC1_terms_accepted)
        # sleep(1)
        # self.click(*ThirdInfoPageLoc.SQ_ESCC1_primary)
        sleep(1.5)
        self.send_keys("55444", *ThirdInfoPageLoc.SQ_ESCC1_validation_code)
        self.click(*ThirdInfoPageLoc.SQ_ESCC1_primary)
        sleep(2.5)
        self.click(*ThirdInfoPageLoc.SQ_ESCC1_component)
        sleep(0.5)
        self.click(*ThirdInfoPageLoc.SQ_ESCC1_primary)
        sleep(10)


    def payment_Zero_OrderPayment(self):
        # self.headers = {'User-Agent': self.ua}
        self.driver.execute_script("var q=document.documentElement.scrollTop=500")
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(
            "//*[@class='ckSm_dropdownIcon']").click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@class='ckSm_dropdownBox']/ul/li[1]/div/p/span[2]").click()
        sleep(0.5)
        self.driver.find_element_by_xpath("//*[@class='ckDc_title']").click()
        sleep(0.5)
        self.driver.find_element_by_xpath("//input[@placeholder='Promotion Code']").send_keys("JJH123456")
        sleep(0.5)
        self.driver.find_element_by_xpath(
            "//*[@class='ckDc_couponApply btn strong']").click()
        sleep(1.5)
        try:
            try:
                self.driver.find_element_by_xpath(
                    "//*[@class='ckOl_totalBtn btn middle strong']").click()  # pleace your order
            except:
                self.driver.find_element_by_xpath(
                    "//*[@class='ckOl_totalBtn btn middle strong']").click()  # pleace your order
        except Exception as msg:
            print(u"异常原因%s" % msg)
            self.add_img()
        sleep(4)

    def payment_poli(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        self.click(*PaymentInfoPageLoc.poli_src)
        self.click(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.pay_currencyselect)
        self.driver.find_element_by_xpath("//*[@class='currency_select']/option[3]").click()
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(4)
        self.click(*ThirdInfoPageLoc.poli_continue)
        sleep(4)
        self.send_keys("DemoShopper", *ThirdInfoPageLoc.poli_Username)
        self.send_keys("DemoShopper", *ThirdInfoPageLoc.poli_Password)
        self.click(*ThirdInfoPageLoc.poli_LoginButton)
        sleep(5)
        self.click(*ThirdInfoPageLoc.poli_textContinue)
        sleep(3)
        self.click(*ThirdInfoPageLoc.poli_primarybutton)
        sleep(5)
        self.click(*ThirdInfoPageLoc.poli_ConfirmButton)


    def payment_Webmoney(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        self.click(*PaymentInfoPageLoc.Webmoney_src)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(8)
        print(self.driver.title)
        title = self.driver.title
        # title = EC.title_is('Merchant WebMoney Transfer')
        if title == 'Merchant WebMoney Transfer' or title == 'Paymaster':
            print("Webmoney可正常跳转至第三方。")
        else:
            print("Webmoney跳转第三方有异常")
            self.add_img()
            self.save_screen_shot()


    def payment_WPG_Pay(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.driver.refresh()
        sleep(0.5)
        print('收银台url：', self.driver.current_url)
        self.click(*PaymentInfoPageLoc.WPG_Pay_src)
        self.click(*PaymentInfoPageLoc.pay_button)
        handles = self.driver.window_handles  # 获取当前全部窗口句柄集合
        print(handles)  # 输出句柄集合
        for handle in handles:  # 切换窗口
            if handle != self.driver.current_window_handle:
                print('switch to second window', handle)
                # self.driver.close()  # 关闭第一个窗口
                self.driver.switch_to.window(handle)  # 切换到第二个窗口
        sleep(0.5)
        self.send_keys("583241254", *ThirdInfoPageLoc.WPG_Pay_email)
        sleep(1)

    def payment_DLC_Boleto(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        print('收银台url：', self.driver.current_url)
        self.driver.refresh()
        sleep(0.5)
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.DLC_Boleto_src)
        self.send_keys("33518524100", *PaymentInfoPageLoc.DLC_Boleto_cpf)
        self.click(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.pay_currencyselect)
        self.click(*PaymentInfoPageLoc.pay_currencyconfirm)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(4)

    def payment_WP_SOFORT_SW(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        print('收银台url：', self.driver.current_url)
        self.driver.refresh()
        sleep(0.5)
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.WP_SOFORT_SW_src)
        self.click(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.pay_currencyselect)
        self.click(*PaymentInfoPageLoc.pay_currencyconfirm)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(3)
        self.click(*ThirdInfoPageLoc.SOFORT_makepayment)
        sleep(2)

    def payment_PayU_UPI(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        print('收银台url：', self.driver.current_url)
        self.driver.refresh()
        sleep(0.5)
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.PayU_UPI_src)
        self.click(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.pay_currencyselect)
        self.click(*PaymentInfoPageLoc.pay_currencyconfirm)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(5)
        # self.send_keys("ayush123@axis", *ThirdInfoPageLoc.PayU_UPI_upiVpa)
        # self.click(*ThirdInfoPageLoc.PayU_UPI_button)
        # sleep(5)
        title = self.driver.title
        # title = EC.title_is('Merchant WebMoney Transfer')
        if title == 'Citrus Checkout':
            print("PayU_UPI可正常跳转至第三方。")
        else:
            print("PayU_UPI跳转第三方有异常")
            self.add_img()
            self.save_screen_shot()

    def payment_DGPAY_PHdp(self):
        self.find_element(*PaymentInfoPageLoc.pay_button)
        print('收银台url：', self.driver.current_url)
        self.driver.refresh()
        sleep(0.5)
        self.find_element(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.DGPAY_PHdp_src)
        self.click(*PaymentInfoPageLoc.pay_button)
        self.click(*PaymentInfoPageLoc.pay_currencyselect)
        self.click(*PaymentInfoPageLoc.pay_currencyconfirm)
        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(5)
        # self.send_keys("ayush123@axis", *ThirdInfoPageLoc.PayU_UPI_upiVpa)
        # self.click(*ThirdInfoPageLoc.PayU_UPI_button)
        # sleep(5)
        title = self.driver.title
        # title = EC.title_is('Merchant WebMoney Transfer')
        if title == 'Dragonpay Online Payment System':
            print("DGPAY_PHdp可正常跳转至第三方。")
        else:
            print("DGPAY_PHdp跳转第三方有异常")
            self.add_img()
            self.save_screen_shot()

    def third_paypal(self):
        # self.headers = {'User-Agent': self.ua}
        sleep(12)
        print(self.driver.title)
        title = EC.title_is('PayPal Checkout - Log in')  # PayPal结账 - 核对您的付款   PayPal结账 - 登录   登陆 'PayPal结账 - 登录'
        if title(self.driver) == False:
            sleep(3)
            try:
                self.driver.execute_script("window.scrollTo(100,850)")
                self.driver.find_element_by_xpath("//*[@id='confirmButtonTop']").click()  # 点击立即付款
            except Exception as msg:
                print(u"异常原因%s" % msg)
                self.add_img()
                raise
            self.driver.implicitly_wait(5)
        else:
            try:
                # print(self.driver.current_url)
                self.driver.switch_to.frame(self.driver.find_element_by_name('injectedUl'))
                # aa1 = self.driver.find_element_by_xpath(
                #     "//*[@class='button actionContinue scTrack:unifiedlogin-login-submit']").text()
                # print(aa1(self.driver))
                # if aa1(self.driver) == 'Log In':
                sleep(1)
                self.driver.find_element_by_xpath("//*[@id='email']").send_keys(self.PPusername)
                sleep(1)
                self.driver.find_element_by_xpath("//*[@id='password']").send_keys(self.PPpassword)  # 输入PP账号密码
                sleep(1)
                # browser.find_element_by_xpath("//*[@='keepMeLoggedIn']")  #保持登录
                self.driver.find_element_by_xpath(
                    "//*[@class='button actionContinue scTrack:unifiedlogin-login-submit']").click()  # 登陆提交订单
                sleep(14)
                self.driver.execute_script("window.scrollTo(100,850)")
                self.driver.find_element_by_xpath("//*[@id='confirmButtonTop']").click()  # 点击立即付款
            except Exception as msg:
                print(u"异常原因%s" % msg)
                self.add_img()
                raise
            self.driver.implicitly_wait(5)


    def gb_checkorder(self):
        # self.headers = {'User-Agent': self.ua}
        # selenium_wait.is_element(self, "//*[@class='pay_title']")
        sleep(1)
        # self.find_title("//*[@class='pay_title']")
        # print(self.driver.title)
        # self.find_element("//*[@class='pay_title']")
        try:
            try:
                paymentresult = self.driver.find_element_by_xpath("//*[@class='pay_title']").text
            except:
                self.driver.refresh()
                sleep(1)
            paymentresult = self.driver.find_element_by_xpath("//*[@class='pay_title']").text
            print("支付结果提示语：", paymentresult)
            global ordersn
            try:
                ordersn = self.driver.find_element_by_xpath("//*[@class='payOnline_sucess']/p[2]/b[1]").text  # paid
            except:
                try:
                    ordersn = self.driver.find_element_by_xpath(
                        "//*[@class='payOnline_padding']/p[1]/b[1]").text  # pending
                except:
                    try:
                        ordersn = self.driver.find_element_by_xpath(
                            "//*[@class='payOffline_default']/p[1]/b[1]").text  # Appreciate
                    except:
                        try:
                            ordersn = self.driver.find_element_by_xpath(
                                "//*[@class='pay_title']/em[1]").text  # Submitting
                        except:
                            print("fail or no_result")
            ordersn = str(ordersn)
            if len(ordersn) == 20:
                pass
            else:
                ordersn = ordersn[:-1]
            print("订单号为：", ordersn)
            connect = pymysql.connect(host=self.host, port=self.post, user=self.user, passwd=self.passwd, db=self.db,
                                      charset='utf8')
            cursor = connect.cursor()
            cursor.execute("SELECT pay_status FROM pay_gateway_16 WHERE parent_order_sn=('%s')" % (ordersn))
            status = cursor.fetchall()
            status = str(status)
            status = status[2:3]
            print("此订单状态为：【%s】" % (status), " (0-未支付 1-处理中 2-已支付 3-退款中 4-退款成功 5退款失败 6支付失败)")
            cursor.close()
            # self.driver.refresh()
        except Exception as msg:
            print(u"异常原因%s" % msg)
            # self.add_img()
            self.save_screen_shot()
            raise

    # def gb_checkorder111(self):
    #     # self.headers = {'User-Agent': self.ua}
    #     # selenium_wait.is_element(self, "//*[@class='pay_title']")
    #     sleep(1)
    #     # print(self.driver.title)
    #
    #     print("sddfsdfdsff", self.is_element_exist("//*[@class='pay_title']"))
    #     try:
    #         try:
    #             paymentresult = self.driver.find_element_by_xpath("//*[@class='pay_title']").text
    #         except:
    #             self.driver.refresh()
    #             sleep(1)
    #             paymentresult = self.driver.find_element_by_xpath("//*[@class='pay_title']").text
    #         print("支付结果提示语：", paymentresult)
    #         global ordersn
    #         try:
    #             ordersn = self.driver.find_element_by_xpath("//*[@class='payOnline_sucess']/p[2]/b[1]").text  # paid
    #         except:
    #             try:
    #                 ordersn = self.driver.find_element_by_xpath(
    #                     "//*[@class='payOnline_padding']/p[1]/b[1]").text  # pending
    #             except:
    #                 try:
    #                     ordersn = self.driver.find_element_by_xpath(
    #                         "//*[@class='payOffline_default']/p[1]/b[1]").text  # Appreciate
    #                 except:
    #                     try:
    #                         ordersn = self.driver.find_element_by_xpath(
    #                             "//*[@class='pay_title']/em[1]").text  # Submitting
    #                     except:
    #
    #                         print("fail or no_result")
    #         ordersn = str(ordersn)
    #         if len(ordersn) == 20:
    #             pass
    #         else:
    #             ordersn = ordersn[:-1]
    #         print("订单号为：", ordersn)
    #         connect = pymysql.connect(host=self.host, port=self.post, user=self.user, passwd=self.passwd, db=self.db,
    #                                   charset='utf8')
    #         cursor = connect.cursor()
    #         cursor.execute("SELECT pay_status FROM pay_gateway_16 WHERE parent_order_sn=('%s')" % (ordersn))
    #         status = cursor.fetchall()
    #         status = str(status)
    #         status = status[2:3]
    #         print("此订单状态为：【%s】" % (status), " (0-未支付 1-处理中 2-已支付 3-退款中 4-退款成功 5退款失败 6支付失败)")
    #         cursor.close()
    #         sleep(1)
    #         # self.driver.refresh()
    #     except Exception as msg:
    #         print(u"异常原因%s" % msg)
    #         self.add_img()
    #         self.save_screen_shot()
    #         raise
    #
    # def gb_checkorder_pending(self):
    #     self.headers = {'User-Agent': self.ua}
    #     selenium_wait.is_element(self, "//*[@class='pay_title']")
    #     sleep(2)
    #     try:
    #         paymentresult = self.driver.find_element_by_xpath("//*[@class='pay_title']").text
    #         print("支付结果提示语：", paymentresult)
    #         global ordersn
    #         ordersn = self.driver.find_element_by_xpath("//*[@class='payOnline_padding']/p[1]/b[1]").text
    #         ordersn = str(ordersn)
    #         ordersn = ordersn[:-1]
    #         print("订单号为：", ordersn)
    #         sleep(1)
    #         connect = pymysql.connect(host=self.host, port=self.post, user=self.user, passwd=self.passwd, db=self.db,
    #                                   charset='utf8')
    #         cursor = connect.cursor()
    #         cursor.execute("SELECT pay_status FROM pay_gateway_16 WHERE parent_order_sn=('%s')" % (ordersn))
    #         status = cursor.fetchall()
    #         status = str(status)
    #         status = status[2:3]
    #         print("此订单状态为：【%s】" % (status), " (0-未支付 1-处理中 2-已支付 3-退款中 4-退款成功 5退款失败 6支付失败)")
    #         cursor.close()
    #         self.driver.refresh()
    #     except Exception as msg:
    #         print(u"异常原因%s" % msg)
    #         self.add_img()
    #         raise
    #
    # def gb_checkorder_Appreciate(self):
    #     self.headers = {'User-Agent': self.ua}
    #     selenium_wait.is_element(self, "//*[@class='pay_title']")
    #     sleep(2)
    #
    #     try:
    #         paymentresult = self.driver.find_element_by_xpath("//*[@class='pay_title']").text
    #         print("支付结果提示语：", paymentresult)
    #         global ordersn
    #         ordersn = self.driver.find_element_by_xpath("//*[@class='payOffline_default']/p[1]/b[1]").text
    #         ordersn = str(ordersn)
    #         ordersn = ordersn[:-1]
    #         print("订单号为：", ordersn)
    #         sleep(1)
    #         connect = pymysql.connect(host=self.host, port=self.post, user=self.user, passwd=self.passwd, db=self.db,
    #                                   charset='utf8')
    #         cursor = connect.cursor()
    #         cursor.execute("SELECT pay_status FROM pay_gateway_16 WHERE parent_order_sn=('%s')" % (ordersn))
    #         status = cursor.fetchall()
    #         status = str(status)
    #         status = status[2:3]
    #         print("此订单状态为：【%s】" % (status), " (0-未支付 1-处理中 2-已支付 3-退款中 4-退款成功 5退款失败 6支付失败)")
    #         cursor.close()
    #         self.driver.refresh()
    #
    #     except Exception as msg:
    #         print(u"异常原因%s" % msg)
    #         self.add_img()
    #         raise
    #
    # def gb_checkorder_Submitting(self):
    #     self.headers = {'User-Agent': self.ua}
    #     selenium_wait.is_element(self, "//*[@class='pay_title']")
    #     sleep(2)
    #
    #     try:
    #         paymentresult = self.driver.find_element_by_xpath("//*[@class='pay_title']").text
    #         print("支付结果提示语：", paymentresult)
    #         global ordersn
    #         ordersn = self.driver.find_element_by_xpath("//*[@class='pay_title']/em[1]").text
    #         ordersn = str(ordersn)
    #         ordersn = ordersn[0:20]
    #         print("订单号为：", ordersn)
    #         sleep(1)
    #         connect = pymysql.connect(host=self.host, port=self.post, user=self.user, passwd=self.passwd, db=self.db,
    #                                   charset='utf8')
    #         cursor = connect.cursor()
    #         cursor.execute("SELECT pay_status FROM pay_gateway_16 WHERE parent_order_sn=('%s')" % (ordersn))
    #         status = cursor.fetchall()
    #         status = str(status)
    #         status = status[2:3]
    #         print("此订单状态为：【%s】" % (status), " (0-未支付 1-处理中 2-已支付 3-退款中 4-退款成功 5退款失败 6支付失败)")
    #         cursor.close()
    #         self.driver.refresh()
    #
    #     except Exception as msg:
    #         print(u"异常原因%s" % msg)
    #         self.add_img()
    #         raise

# if __name__ == "__main__":
#     GBBaseCase.main()


