from UI_AUTOMATION.utils.config import Config
from selenium.webdriver.support.ui import Select
import pymysql
from UI_AUTOMATION.test.page.pageconfig.haoselenium import *
from UI_AUTOMATION.utils.config import Config
from selenium.webdriver.common.action_chains import ActionChains  # 引入 ActionChains 类
from selenium.webdriver.common.keys import Keys

# from UI_AUTOMATION.utils.HTMLTestRunner import HTMLTestRunner


class GBBaseCase():

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
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def gb_login(self):
        self.headers = {'User-Agent': self.ua}

        # self.driver = driver

        # try:
        #     self.driver.get(self.GBloginURL)
        #     self.driver.maximize_window()
        #     self.driver.find_element_by_id("email").send_keys(self.username)
        #     self.driver.find_element_by_id("password").send_keys(self.password)
        #     self.driver.find_element_by_id("js-btnSubmit").click()
        # except Exception as msg:
        #     print(u"异常原因%s" % msg)
        #     self.add_img()
        #     raise
        # sleep(2)

        url = "https://m.gearbest.net/"
        login_url = "https://loginm.gearbest.net/m-users-a-sign.htm"
        self.driver.get(login_url)
        sleep(2)
        # self.driver.find_element_by_xpath("//*[@placeholder='E-mail address']").send_keys(Keys.F12)
        # sleep(1)
        # self.driver.find_element_by_xpath('//*[@class="ck_checkoutTotalBtn font-32"]').send_keys(Keys.CONTROL, Keys.SHIFT, 'm')  # control + a 全选
        sleep(0.5)
        self.driver.find_element_by_xpath("//*[@placeholder='E-mail address']").send_keys('jiangjiahao@globalegrow.com')
        self.driver.find_element_by_xpath("//*[@placeholder='Password']").send_keys('abc456456')
        self.driver.find_element_by_xpath("//*[@class='btn btnLight']").click()


    def gb_goodtobuy(self):
            self.driver.set_page_load_timeout(8)
            try:
                self.driver.get("https://m.gearbest.net/wallets/pp_1771338.html?wid=1433363")
            except TimeoutException:
                self.driver.execute_script('window.stop()')
            self.driver.execute_script("var q=document.body.scrollTop=500")
            try:
                selenium_wait.is_clickable(self, "//*[@class='btn goodsBtnBuyNow press js-btnShowAttrPanel']", 6)
                sleep(0.5)
                self.driver.find_element_by_xpath("//*[@class='btn goodsBtnBuyNow press js-btnShowAttrPanel']").click()
                sleep(1)
                self.driver.find_element_by_xpath("//*[@class='btn goodsBtnBuyNow js-buyNow']").click()  # 商品点击购买

            except Exception as msg:
                print(u"异常原因%s" % msg)
                self.add_img()
                raise
            sleep(5)

    def gb_goodtopaypal(self):
        self.driver.set_page_load_timeout(8)
        try:
            self.driver.get("https://m.gearbest.net/smart-watches/pp_009814268018.html?wid=1039065")
        except TimeoutException:
            self.driver.execute_script('window.stop()')
        self.driver.execute_script("var q=document.body.scrollTop=500")
        try:
            selenium_wait.is_clickable(self, "//*[@class='btn goodsBtnBuyNow press js-btnShowAttrPanel']", 6)
            sleep(0.5)
            self.driver.find_element_by_xpath("//*[@class='btn goodsBtnBuyNow press js-btnShowAttrPanel']").click()
            sleep(2)
            self.driver.find_element_by_xpath("//*[@class='btn goodsBtnPaypal js-buyNowWithPaypal']").click()  # 商品点击购买

        except Exception as msg:
            print(u"异常原因%s" % msg)
            self.add_img()
            raise
        sleep(5)

    def gb_placeorder(self):
        # self.headers = {'User-Agent': self.ua}
        # self.driver.execute_script("var q=document.documentElement.scrollTop=500")
        self.driver.implicitly_wait(5)
        sleep(1)
        try:
             self.driver.find_element_by_xpath('//*[@class="ck_checkoutTotalBtn font-32"]').click()       # 点击购买  placeOrder btn block toPayBtn
        except Exception as msg:
            print(u"异常原因%s" % msg)
            self.add_img()
        sleep(4)

    def paymentplatform(self):
        self.headers = {'User-Agent': self.ua}
        selenium_wait.is_clickable(self, "//*[@class='placeOrder btn block toPayBtn']")
        try:
            self.driver.execute_script("document.documentElement.scrollTop = 100000")
            sleep(0.5)
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 点击购买  placeOrder btn block toPayBtn
        except Exception as msg:
            print(u"异常原因%s" % msg)
            pamentordersn = self.driver.find_element_by_xpath("//*[@class='pc_orderinf']/dl[1]/dd").text
            print("收银台订单号：", pamentordersn)
            print('当前页面url：', self.driver.current_url)
            # BaseTestCase.add_img()
            self.add_img()
            raise
        sleep(2)

    def payment_paypal(self):
        sleep(1)
        try:
            self.driver.execute_script("document.documentElement.scrollTop = 100000")
            sleep(1)
            self.driver.find_element_by_xpath("//*[@src='https://uidesign.gbtcdn.com/check_out/paypal.png?impolicy==true']").click()
            sleep(0.5)
            self.driver.find_element_by_xpath('//*[@class="ck_checkoutTotalBtn font-32"]').click()  # 点击购买  placeOrder btn block toPayBtn

        except Exception as msg:
            print(u"异常原因%s" % msg)
            # pamentordersn = self.driver.find_element_by_xpath("//*[@class='pc_orderinf']/dl[1]/dd").text
            # print("收银台订单号：", pamentordersn)
            print('当前页面url：', self.driver.current_url)
            # self.add_img()
            # raise
        sleep(4)

    def payment_creditcard(self):
        selenium_wait.is_clickable(self, "//*[@class='placeOrder btn block toPayBtn']")
        try:
            self.driver.find_element_by_xpath('//*[@class="creditcard"]').click()
            sleep(0.5)
            self.driver.find_element_by_xpath('//*[@class="btn block font-32 m_toPayBtn"]').click()

            self.driver.find_element_by_xpath("//*[@placeholder='Card Holder']").send_keys("hao")
            self.driver.find_element_by_xpath("//*[@placeholder='Card Number']").send_keys("6011111111111117")
            # self.driver.find_element_by_xpath('//*[@class="logoChangeTips"]').click()
            # self.driver.find_element_by_xpath('//*[@src="https://uidesign.gbtcdn.com/check_out/M/discover.png?imbypass=true"]').click()
            self.driver.find_element_by_xpath("//*[@placeholder='Security Code']").send_keys("100")
            sleep(0.5)
            Select(self.driver.find_element_by_xpath('//*[@name="expirationMonth"]')).select_by_value("5")  ## 实例化Select 月份
            sleep(0.5)
            Select(self.driver.find_element_by_xpath('//*[@name="expirationYear"]')).select_by_value("2020")  # 实例化Select 年份
            sleep(0.8)
            self.driver.find_element_by_xpath("//*[@class='btn block font-32 m_toPayBtn']").click()  # 点击购买  placeOrder btn block toPayBtn
            sleep(3)
        except Exception as msg:
            print(u"异常原因%s" % msg)
            pamentordersn = self.driver.find_element_by_xpath("//*[@class='pc_orderinf']/dl[1]/dd").text
            print("收银台订单号：", pamentordersn)
            print('当前页面url：', self.driver.current_url)
            self.add_img()
            raise
        sleep(4)

    def payment_worldpay(self):
        selenium_wait.is_clickable(self, "//*[@class='placeOrder btn block toPayBtn']")
        try:
            self.driver.find_element_by_xpath('//*[@class="pc_content_list"]/dl[1]/dt/label/span/em[1]/img').click()
            self.driver.find_element_by_xpath("//*[@placeholder='Card Holder']").send_keys("hao")
            self.driver.find_element_by_xpath("//*[@placeholder='Card Number']").send_keys("4444333322221111")
            self.driver.find_element_by_xpath("//*[@placeholder='Security Code']").send_keys("111")
            sleep(0.5)
            Select(self.driver.find_element_by_xpath('//*[@id="content_wrap"]/div[1]/div[1]/dl[1]/dd/div/div[2]/div/select')).select_by_value("5")  ## 实例化Select 月份
            sleep(0.5)
            Select(self.driver.find_element_by_xpath('//*[@id="content_wrap"]/div[1]/div[1]/dl[1]/dd/div/div[3]/div/select')).select_by_value("2020")  # 实例化Select 年份
            sleep(1)
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 点击购买  placeOrder btn block toPayBtn
            # selenium_wait.test_visibility_of(self, "//*[@class='placeOrder btn block toPayBtn']")
            # sleep(1)
        except Exception as msg:
            print(u"异常原因%s" % msg)
            pamentordersn = self.driver.find_element_by_xpath("//*[@class='pc_orderinf']/dl[1]/dd").text
            print('当前页面url：', self.driver.current_url)
            print("收银台订单号：", pamentordersn)
            self.add_img()
            raise
        sleep(4)


    def payment_adn_cc(self):
        selenium_wait.is_clickable(self, "//*[@class='placeOrder btn block toPayBtn']")
        try:
            self.driver.find_element_by_xpath('//*[@class="pc_content_list"]/dl[1]/dt/label/span/em[1]/img').click()
            self.driver.find_element_by_xpath("//*[@placeholder='Card Holder']").send_keys("hao")
            self.driver.find_element_by_xpath("//*[@placeholder='Card Number']").send_keys("4111111111111111")
            self.driver.find_element_by_xpath("//*[@placeholder='Security Code']").send_keys("737")
            sleep(0.5)
            Select(self.driver.find_element_by_xpath('//*[@id="content_wrap"]/div[1]/div[1]/dl[1]/dd/div/div[2]/div/select')).select_by_value("10")  ## 实例化Select 月份
            sleep(0.5)
            Select(self.driver.find_element_by_xpath('//*[@id="content_wrap"]/div[1]/div[1]/dl[1]/dd/div/div[3]/div/select')).select_by_value("2020")  # 实例化Select 年份
            sleep(0.5)
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 点击购买  placeOrder btn block toPayBtn
        except Exception as msg:
            print(u"异常原因%s" % msg)
            pamentordersn = self.driver.find_element_by_xpath("//*[@class='pc_orderinf']/dl[1]/dd").text
            print("收银台订单号：", pamentordersn)
            print('当前页面url：', self.driver.current_url)
            self.add_img()
            raise
        sleep(4)


    def payment_GC(self):
        selenium_wait.is_clickable(self, "//*[@class='placeOrder btn block toPayBtn']")
        try:
            self.driver.find_element_by_xpath('//*[@class="pc_content_list"]/dl[1]/dt/label/span/em[1]/img').click()
            self.driver.find_element_by_xpath("//*[@placeholder='Card Holder']").send_keys("hao")
            self.driver.find_element_by_xpath("//*[@placeholder='Card Number']").send_keys("5200000000000007")
            self.driver.find_element_by_xpath("//*[@placeholder='Security Code']").send_keys("111")
            sleep(0.5)
            Select(self.driver.find_element_by_xpath('//*[@id="content_wrap"]/div[1]/div[1]/dl[1]/dd/div/div[2]/div/select')).select_by_value("10")  ## 实例化Select 月份
            sleep(0.5)
            Select(self.driver.find_element_by_xpath('//*[@id="content_wrap"]/div[1]/div[1]/dl[1]/dd/div/div[3]/div/select')).select_by_value("2020")  # 实例化Select 年份
            sleep(0.5)
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 点击购买  placeOrder btn block toPayBtn
            sleep(8)
            title = EC.title_is('GearBest: Online Shopping - Best Gear at Best Prices')
            if title(self.driver) == False:
                sleep(8)
                try:
                    self.driver.switch_to.frame(self.driver.find_element_by_id('authWindow'))
                    self.driver.find_element_by_xpath("//*[@type='password']").send_keys("1234")
                    sleep(2)
                    self.driver.find_element_by_xpath(
                        "//*[@name='UsernamePasswordEntry']").click()  # 点击购买  placeOrder btn block toPayBtn
                except Exception as msg:
                    print(u"异常原因%s" % msg)
                    self.add_img()
                    raise
                    self.driver.implicitly_wait(5)
            else:
                pass
        except Exception as msg:
            print(u"异常原因%s" % msg)
            pamentordersn = self.driver.find_element_by_xpath("//*[@class='pc_orderinf']/dl[1]/dd").text
            print("收银台订单号：", pamentordersn)
            print('当前页面url：', self.driver.current_url)
            self.add_img()
            raise
        sleep(8)

    def payment_ebanxinstalment(self):
        selenium_wait.is_clickable(self, "//*[@class='placeOrder btn block toPayBtn']")
        try:
            self.driver.find_element_by_xpath('//*[@class="pc_content_list"]/dl[1]/dt/label/span/em[1]/img').click()
            self.driver.find_element_by_xpath('//*[@class="formList_select installments"]').click()
            sleep(0.5)
            self.driver.find_element_by_xpath('//*[@class="formList_select installments"]/option[3]').click()
            self.driver.find_element_by_xpath('//*[@id="content_wrap"]/div[1]/div[1]/dl[1]/dd/div/div[2]/div[1]/div/input[1]').send_keys("04268600558")
            self.driver.find_element_by_xpath("//*[@placeholder='Titular do cartão']").send_keys("hao")
            self.driver.find_element_by_xpath("//*[@placeholder='Número de cartão']").send_keys("4111111111111111")
            self.driver.find_element_by_xpath("//*[@placeholder='Código de segurança']").send_keys("111")
            sleep(0.5)
            Select(self.driver.find_element_by_xpath('//*[@id="content_wrap"]/div[1]/div[1]/dl[1]/dd/div/div[4]/div/select')).select_by_value("5")  ## 实例化Select 月份
            sleep(0.5)
            Select(self.driver.find_element_by_xpath('//*[@id="content_wrap"]/div[1]/div[1]/dl[1]/dd/div/div[5]/div/select')).select_by_value("2020")  # 实例化Select 年份
            sleep(0.5)
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 点击购买  placeOrder btn block toPayBtn
        except Exception as msg:
            print(u"异常原因%s" % msg)
            pamentordersn = self.driver.find_element_by_xpath("//*[@class='pc_orderinf']/dl[1]/dd").text
            print("收银台订单号：", pamentordersn)
            print('当前页面url：', self.driver.current_url)
            self.add_img()
            raise
        sleep(5)

    def payment_PayU_TRCC(self):
        selenium_wait.is_clickable(self, "//*[@class='placeOrder btn block toPayBtn']")
        try:
            self.driver.find_element_by_xpath('//*[@src="https://uidesign.gbtcdn.com/GB/images/others/tr_installment_logo.png"]').click()
            sleep(0.5)
            self.driver.find_element_by_xpath("//*[@class='paychannel checked']/dd/div/div[1]/div/input").send_keys("4355084355084358")
            sleep(0.2)
            self.driver.execute_script("var q=document.body.scrollTop=500")
            sleep(0.3)
            self.driver.find_element_by_xpath('//*[@src="https://uidesign.gbtcdn.com/GB/images/others/tr_installment_logo.png"]').click()
            sleep(2)
            self.driver.find_element_by_xpath("//*[@class='paychannel checked']/dd/div/div[2]/div/select").click()  # 选择分期
            sleep(1)
            self.driver.find_element_by_xpath("//*[@class='paychannel checked']/dd/div/div[2]/div/select/option[4]").click()  # 选择分期
            sleep(0.3)
            Select(self.driver.find_element_by_xpath('//*[@class="paychannel checked"]/dd/div/div[3]/div/select')).select_by_value("12")  ## 实例化Select 月份
            sleep(0.5)
            Select(self.driver.find_element_by_xpath('//*[@class="paychannel checked"]/dd/div/div[4]/div/select')).select_by_value("2018")  # 实例化Select 年份
            sleep(0.2)
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()
            sleep(0.5)
            self.driver.find_element_by_xpath("//*[@class='paychannel checked']/dd/div/div[5]/div[1]/input").send_keys("000")
            self.driver.find_element_by_xpath("//*[@class='paychannel checked']/dd/div/div[6]/div/input").send_keys("hao")
            sleep(0.2)
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()
            sleep(0.5)
            self.driver.find_element_by_xpath("//*[@class='currency_select']").click()
            self.driver.find_element_by_xpath("//*[@class='currency_select']/option[2]").click()
            sleep(0.2)
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()
            sleep(3)
            selenium_wait.is_clickable(self ,"//*[@id='submitbutton']")
            self.driver.find_element_by_xpath('//*[@name="password"]').send_keys('a')
            self.driver.find_element_by_id('submitbutton').click()
            sleep(6)

        except Exception as msg:
            print(u"异常原因%s" % msg)
            pamentordersn = self.driver.find_element_by_xpath("//*[@class='pc_orderinf']/dl[1]/dd").text
            print("收银台订单号：", pamentordersn)
            print('当前页面url：', self.driver.current_url)
            self.add_img()
            raise
        sleep(4)

    def payment_PayU_BKM(self):
        selenium_wait.is_clickable(self, "//*[@class='placeOrder btn block toPayBtn']")
        try:
            self.driver.find_element_by_xpath('//*[@src="https://css.gbtcdn.com/imagecache/GB3/images/domeimg/pay_method/PayU_BKM.png"]').click()
            sleep(0.5)
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 点击购买  placeOrder btn block toPayBtn
            sleep(0.5)
            self.driver.find_element_by_xpath("//*[@class='currency_select']").click()
            self.driver.find_element_by_xpath("//*[@class='currency_select']/option[2]").click()
            sleep(0.5)
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 点击购买  placeOrder btn block toPayBtn
        except Exception as msg:
            print(u"异常原因%s" % msg)
            pamentordersn = self.driver.find_element_by_xpath("//*[@class='pc_orderinf']/dl[1]/dd").text
            print("收银台订单号：", pamentordersn)
            print('当前页面url：', self.driver.current_url)
            self.add_img()
            raise
        sleep(1)
        self.driver.set_page_load_timeout(14)
        try:
            selenium_wait.is_clickable(self, "//*[@id='loginBtn']")
        except TimeoutException:
            self.driver.execute_script('window.stop()')
        try:
            self.driver.find_element_by_id("loginBtn").click()
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_id('username').send_keys('neticaret5@bkm.com')
            self.driver.find_element_by_id('passwordPwd').send_keys('147258')
            sleep(1)
            try:
                self.driver.find_element_by_id("loginBtn").click()
            except:
                pass

            self.driver.set_page_load_timeout(10)
            try:
                selenium_wait.is_clickable(self, '//*[@type="submit"]')
            except TimeoutException:
                self.driver.execute_script('window.stop()')
            # sleep(1)
            EC.title_contains("BKM Express")
            # self.driver.refresh()
            sleep(2)
            self.driver.find_element_by_xpath('//*[@id="installment-select"]/tbody/tr[3]/td[1]/label').click()
            sleep(0.3)
            self.driver.find_element_by_xpath('//*[@id="submit-card"]').click()
            # sleep(4)

            self.driver.set_page_load_timeout(10)
            try:
                selenium_wait.is_clickable(self, '//*[@type="submit"]')
            except TimeoutException:
                self.driver.execute_script('window.stop()')
            self.driver.refresh()
            sleep(2)
            try:
                self.driver.find_element_by_xpath('//*[@type="submit"]').click()
                self.driver.find_element_by_xpath('//*[@id="otp"]').send_keys('123456')
            except:
                self.driver.find_element_by_xpath('//*[@id="otp"]').clear()
                self.driver.find_element_by_xpath('//*[@id="otp"]').send_keys('123456')
            try:
                self.driver.find_element_by_xpath('//*[@type="submit"]').click()
            except:
                pass
            sleep(3)
        except Exception as msg:
            print(u"异常原因%s" % msg)
            self.add_img()
            raise
        sleep(3)

    def payment_boleto(self):
        selenium_wait.is_clickable(self, "//*[@class='placeOrder btn block toPayBtn']")
        try:
            self.driver.execute_script("var q=document.body.scrollTop=500")
            # self.driver.find_element_by_xpath('//*[@class="pc_content_list"]/dl[4]/dt/label/span/em/img').click()
            self.driver.find_element_by_xpath('//*[@src="https://icss1.gearbest.com/imagecache/GB2/images/boleto3.jpg"]').click()
            sleep(0.5)
            self.driver.find_element_by_xpath('//*[@id="content_wrap"]/div[1]/div[1]/dl[4]/dd/div/div[1]/div[1]/div/input[1]').send_keys("04268600558")
            sleep(0.5)
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 点击购买  placeOrder btn block toPayBtn
            sleep(0.5)
            self.driver.find_element_by_xpath("//*[@class='currency_select']").click()
            self.driver.find_element_by_xpath("//*[@class='currency_select']/option[2]").click()
            sleep(0.5)
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 点击购买  placeOrder btn block toPayBtn
        except Exception as msg:
            print(u"异常原因%s" % msg)
            pamentordersn = self.driver.find_element_by_xpath("//*[@class='pc_orderinf']/dl[1]/dd").text
            print("收银台订单号：", pamentordersn)
            print('当前页面url：', self.driver.current_url)
            self.add_img()
            raise
        sleep(4)

    def payment_ADN_PTMB(self):
        selenium_wait.is_clickable(self, "//*[@class='placeOrder btn block toPayBtn']")
        selenium_wait.is_clickable(self, '//*[@src="https://uidesign.gbtcdn.com/check_out/Mutibanco_m.png?impolicy=high"]')
        try:
            self.driver.find_element_by_xpath('//*[@src="https://uidesign.gbtcdn.com/check_out/Mutibanco_m.png?impolicy=high"]').click()
            sleep(0.5)
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 点击购买  placeOrder btn block toPayBtn
            sleep(0.5)
            self.driver.find_element_by_xpath("//*[@class='currency_select']").click()
            self.driver.find_element_by_xpath("//*[@class='currency_select']/option[2]").click()
            sleep(0.5)
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 点击购买  placeOrder btn block toPayBtn
            sleep(4)
            self.driver.find_element_by_xpath("//*[@id='mainSubmit']").click()  # 第三方点击contiun
        except Exception as msg:
            print(u"异常原因%s" % msg)
            pamentordersn = self.driver.find_element_by_xpath("//*[@class='pc_orderinf']/dl[1]/dd").text
            print("收银台订单号：", pamentordersn)
            print('当前页面url：', self.driver.current_url)
            self.add_img()
            raise
        sleep(4)

    def payment_WP_24(self):
        selenium_wait.is_clickable(self, "//*[@class='placeOrder btn block toPayBtn']")
        try:
            self.driver.find_element_by_xpath('//*[@src="https://icss1.gearbest.com/imagecache/GB2/images/domeimg/pay_method/przelewy24.jpg"]').click()
            sleep(0.5)
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 点击购买  placeOrder btn block toPayBtn
            sleep(0.7)
            self.driver.find_element_by_xpath("//*[@class='currency_select']").click()
            self.driver.find_element_by_xpath("//*[@class='currency_select']/option[2]").click()
            sleep(0.5)
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 点击购买  placeOrder btn block toPayBtn
            sleep(6)
            self.driver.find_element_by_xpath('//*[@src="/images/buttons/makepayment.gif"]').click()  # 第三方点击contiun
        except Exception as msg:
            print(u"异常原因%s" % msg)
            pamentordersn = self.driver.find_element_by_xpath("//*[@class='pc_orderinf']/dl[1]/dd").text
            print("收银台订单号：", pamentordersn)
            print('当前页面url：', self.driver.current_url)
            self.add_img()
            raise
        sleep(5)

    def payment_wallet(self):
        # selenium_wait.is_clickable(self, "//*[@class='btn block font-32 m_toPayBtn']")
        sleep(1)
        try:
            self.driver.execute_script("document.documentElement.scrollTop = 100000")
            sleep(1)
            self.driver.find_element_by_xpath("//*[@class='paymentChannel_walletSelect ckPub_select check']").click()
            sleep(0.5)
            self.driver.find_element_by_xpath("//*[@type='password']").send_keys('123456')
            sleep(1)
            self.driver.find_element_by_xpath('//*[@class="ck_checkoutTotalBtn font-32"]').click()       # 点击购买  placeOrder btn block toPayBtn

        except Exception as msg:
            print(u"异常原因%s" % msg)
            # pamentordersn = self.driver.find_element_by_xpath("//*[@class='pc_orderinf']/dl[1]/dd").text
            # print("收银台订单号：", pamentordersn)
            print('当前页面url：', self.driver.current_url)
            # self.add_img()
            # raise
        sleep(4)

    def payment_ZYPaytm (self):
        selenium_wait.is_clickable(self, "//*[@class='placeOrder btn block toPayBtn']")
        try:
            self.driver.find_element_by_xpath('//*[@src="https://uidesign.gbtcdn.com/check_out/paytm.png?01"]').click()
            sleep(0.5)
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 点击购买  placeOrder btn block toPayBtn
            sleep(0.5)
            self.driver.find_element_by_xpath("//*[@class='currency_select']").click()   #切换币种
            self.driver.find_element_by_xpath("//*[@class='currency_select']/option[2]").click()
            sleep(0.5)
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 点击购买  placeOrder btn block toPayBtn
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
            self.driver.find_element_by_xpath("//*[@id='cn1']").send_keys('1232132132132132132')
            sleep(1)
            Select(self.driver.find_element_by_xpath("//*[@id='dcExpMonth']")).select_by_value("05")
            Select(self.driver.find_element_by_xpath("//*[@id='dcExpYear']")).select_by_value("2020")
            sleep(0.5)
            self.driver.find_element_by_xpath("//*[@id='dcCvvBox']").send_keys('123')
            sleep(0.5)
            self.driver.find_element_by_xpath("//*[@id='dcSubmit']").click()
            sleep(2)
            selenium_wait.is_clickable(self, "//*[@type='submit']")
            self.driver.find_element_by_id('OTP').send_keys('1234')
            self.driver.find_element_by_xpath("//*[@type='submit']").click()

        except Exception as msg:
            print(u"异常原因%s" % msg)
            pamentordersn = self.driver.find_element_by_xpath("//*[@class='pc_orderinf']/dl[1]/dd").text
            print("收银台订单号：", pamentordersn)
            print('当前页面url：', self.driver.current_url)
            self.add_img()
            raise
        sleep(2)

    def third_paypal(self):
        # self.headers = {'User-Agent': self.ua}
        # Log in to your PayPal account
        # PayPal结账 - 选择付款方式
        sleep(10)
        selenium_wait.is_clickable(self, "//*[@id='checkoutAsAGuestBtn']", 8)
        print(self.driver.title)
        title = EC.title_is('Log in to your PayPal account')
        if title(self.driver) == False:
            sleep(1)
            try:
                self.driver.execute_script("window.scrollTo(100,850)")
                self.driver.find_element_by_xpath("//*[@class='btn full confirmButton continueButton']").click()  # 继续
                try:
                    sleep(2)
                    self.driver.find_element_by_xpath("//*[@id='confirmButtonTop']").click()  # 点击立即付款
                except:
                    pass
            except Exception as msg:
                print(u"异常原因%s" % msg)
                self.add_img()
                raise
            self.driver.implicitly_wait(5)
        else:
            try:
                sleep(1)
                self.driver.find_element_by_xpath("//*[@id='email']").send_keys(self.PPusername)
                sleep(0.5)
                self.driver.find_element_by_xpath("//*[@id='password']").send_keys(self.PPpassword)  # 输入PP账号密码
                sleep(0.5)
                self.driver.find_element_by_xpath("//*[@id='btnLogin']").click()  # 登陆提交订单
                sleep(15)
                self.driver.execute_script("window.scrollTo(100,850)")
                self.driver.find_element_by_xpath("//*[@id='button']").click()  # 点击立即付款
                sleep(2)
                try:
                    self.driver.find_element_by_xpath("//*[@id='confirmButtonTop']").click()  # 继续
                except:
                    pass
            except Exception as msg:
                print(u"异常原因%s" % msg)
                self.add_img()
                raise
            self.driver.implicitly_wait(5)

    def gb_checkorder(self):
        # self.headers = {'User-Agent': self.ua}
        try:
            selenium_wait.is_element(self, "//*[@class='payment_title']")
        except:
            sleep(4)
            pass
        sleep(1)
        # print(self.driver.title)

        try:
            paymentresult = self.driver.find_element_by_xpath('//*[@id="siteWrap"]/div/div/div/h3/span').text
            print("支付结果提示语：", paymentresult)
            global ordersn
            ordersn = self.driver.find_element_by_xpath('//*[@id="siteWrap"]/div/div/div/p[2]/span[2]').text
            print("订单号为：", ordersn)
            sleep(1)
            connect = pymysql.connect(host=self.host, port=self.post, user=self.user, passwd=self.passwd, db=self.db, charset='utf8')
            cursor = connect.cursor()
            cursor.execute("SELECT pay_status FROM pay_gateway_16 WHERE parent_order_sn=('%s')"%(ordersn))
            status = cursor.fetchall()
            status = str(status)
            status = status[2:3]
            print("此订单状态为：【%s】"%(status)," (0-未支付 1-处理中 2-已支付 3-退款中 4-退款成功 5退款失败 6支付失败)")
            cursor.close()
        except Exception as msg:
            print(u"异常原因%s" % msg)
            self.add_img()
            raise

    def gb_checkorder_pending(self):
        self.headers = {'User-Agent': self.ua}
        selenium_wait.is_element(self, "//*[@class='pay_title']")
        try:
            paymentresult = self.driver.find_element_by_xpath("//*[@class='pay_title']").text
            print("支付结果提示语：", paymentresult)
            global ordersn
            ordersn = self.driver.find_element_by_xpath("//*[@class='payOnline_padding']/p[1]/b[1]").text
            ordersn = str(ordersn)
            ordersn = ordersn[:-1]
            print("订单号为：", ordersn)
            sleep(1)
            connect = pymysql.connect(host=self.host, port=self.post, user=self.user, passwd=self.passwd, db=self.db, charset='utf8')
            cursor = connect.cursor()
            cursor.execute("SELECT pay_status FROM pay_gateway_16 WHERE parent_order_sn=('%s')"%(ordersn))
            status = cursor.fetchall()
            status = str(status)
            status = status[2:3]
            print("此订单状态为：【%s】"%(status)," (0-未支付 1-处理中 2-已支付 3-退款中 4-退款成功 5退款失败 6支付失败)")
            cursor.close()
        except Exception as msg:
            print(u"异常原因%s" % msg)
            self.add_img()
            raise

    def gb_checkorder_Submitting(self):
        self.headers = {'User-Agent': self.ua}
        selenium_wait.is_element(self, "//*[@class='pay_title']")
        try:
            paymentresult = self.driver.find_element_by_xpath("//*[@class='pay_title']").text
            print("支付结果提示语：", paymentresult)
            global ordersn
            ordersn = self.driver.find_element_by_xpath("//*[@class='pay_title']/em[1]").text
            ordersn = str(ordersn)
            ordersn = ordersn[0:20]
            print("订单号为：", ordersn)
            sleep(1)
            connect = pymysql.connect(host=self.host, port=self.post, user=self.user, passwd=self.passwd, db=self.db, charset='utf8')
            cursor = connect.cursor()
            cursor.execute("SELECT pay_status FROM pay_gateway_16 WHERE parent_order_sn=('%s')" %(ordersn))
            status = cursor.fetchall()
            status = str(status)
            status = status[2:3]
            print("此订单状态为：【%s】" % (status), " (0-未支付 1-处理中 2-已支付 3-退款中 4-退款成功 5退款失败 6支付失败)")
            cursor.close()
        except Exception as msg:
            print(u"异常原因%s" % msg)
            self.add_img()
            raise

    def gb_form_test(self):
        selenium_wait.is_clickable(self, "//*[@class='placeOrder btn block toPayBtn']")
        try:
            # self.driver.get("https://cashier.gearbest.net/?token=O181207009733161906EMV&lang=en&source=uCenter&pipelineCode=GB&countryCode=TR&platform=1&parentOrderSn=18120600973318360410")
            # self.driver.maximize_window()
            sleep(0.5)
            self.driver.find_element_by_xpath('//*[@src="https://uidesign.gbtcdn.com/GB/images/others/check_out/57x35/discover.png?imbypass=true"]').click()
            sleep(0.5)
            print("Card numbers校验：")
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()   #激活校验
            selenium_assert.is_text_equal(self, '//*[@curchannel="CREDITCARD"]/div[1]/div/p', 'Please enter your card number.' ,'Card numbers为空校验')

            self.driver.find_element_by_xpath("//*[@placeholder='Card Number']").send_keys("hhhh")
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 激活校验
            selenium_assert.is_text_equal(self, '//*[@curchannel="CREDITCARD"]/div[1]/div/p',
                                          'Please enter numbers only.',
                                          'Card numbers全字母错误校验')

            self.driver.find_element_by_xpath("//*[@placeholder='Card Number']").clear()
            self.driver.find_element_by_xpath("//*[@placeholder='Card Number']").send_keys("1234567890")
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()   #激活校验
            selenium_assert.is_text_equal(self, '//*[@curchannel="CREDITCARD"]/div[1]/div/p', 'Card numbers must contain between 12 and 20 numerical characters.' ,'Card numbers长度校验')

            self.driver.find_element_by_xpath("//*[@placeholder='Card Number']").clear()
            self.driver.find_element_by_xpath("//*[@placeholder='Card Number']").send_keys("123456789012")
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 激活校验
            selenium_assert.is_text_equal(self, '//*[@curchannel="CREDITCARD"]/div[1]/div/p',
                                          'Invalid card numbers. Please kindly make sure that your card numbers are correct.',
                                          'Card numbers无效卡校验')
            self.driver.find_element_by_xpath("//*[@placeholder='Card Number']").clear()
            self.driver.find_element_by_xpath("//*[@placeholder='Card Number']").send_keys("6011111111111117")
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 激活校验
            selenium_assert.isElementExist(self, '//*[@curchannel="CREDITCARD"]/div[1]/div/p', 'Card numbers有效卡校验')
            print("------------------------------------------------------------------")

            print("date校验：")
            sleep(0.3)
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 激活校验
            selenium_assert.is_text_equal(self, "//*[@paychannel='CREDITCARD']/dd/div/div[2]/p", 'Please select your card expiry date.', 'date为空校验')
            Select(self.driver.find_element_by_xpath('//*[@id="content_wrap"]/div[1]/div[1]/dl[1]/dd/div/div[2]/div/select')).select_by_value("10")  ## 实例化Select 月份
            sleep(0.3)
            Select(self.driver.find_element_by_xpath('//*[@id="content_wrap"]/div[1]/div[1]/dl[1]/dd/div/div[3]/div/select')).select_by_value("2018")  # 实例化Select 年份
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 激活校验
            selenium_assert.is_text_equal(self, '//*[@paychannel="CREDITCARD"]/dd/div/div[2]/p', "Expiry Month' and 'Expiry Year' together must be a date in the future.", 'date小于今日校验')

            Select(self.driver.find_element_by_xpath('//*[@id="content_wrap"]/div[1]/div[1]/dl[1]/dd/div/div[3]/div/select')).select_by_value("2022")  # 实例化Select 年份
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 激活校验
            selenium_assert.isElementExist(self, '//*[@paychannel="CREDITCARD"]/dd/div/div[2]/p', 'date正常填写校验')
            print("------------------------------------------------------------------")

            print("非Am卡——SecurityCode校验:")
            selenium_assert.is_text_equal(self, '//*[@paychannel="CREDITCARD"]/dd/div/div[4]/p', 'Please enter the Security Code.' ,'SecurityCode为空校验')

            self.driver.find_element_by_xpath("//*[@placeholder='Security Code']").send_keys("ddd")
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 激活校验
            selenium_assert.is_text_equal(self, '//*[@paychannel="CREDITCARD"]/dd/div/div[4]/p', "Please enter numbers only.",'SecurityCode非纯数字校验')

            self.driver.find_element_by_xpath("//*[@placeholder='Security Code']").clear()
            self.driver.find_element_by_xpath("//*[@placeholder='Security Code']").send_keys("11")
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 激活校验
            selenium_assert.is_text_equal(self, '//*[@paychannel="CREDITCARD"]/dd/div/div[4]/p', 'Please enter 3 digits' ,'SecurityCode长度不够校验')

            self.driver.find_element_by_xpath("//*[@placeholder='Security Code']").clear()
            self.driver.find_element_by_xpath("//*[@placeholder='Security Code']").send_keys("111")
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 激活校验
            selenium_assert.isElementExist(self, '//*[@paychannel="CREDITCARD"]/dd/div/div[4]/p', 'SecurityCode长度正确校验')

            print("Am卡——SecurityCode校验:")
            self.driver.find_element_by_xpath(
                '//*[@src="https://uidesign.gbtcdn.com/GB/images/others/check_out/57x35/american-express.png?imbypass=true"]').click()
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 激活校验
            selenium_assert.is_text_equal(self, '//*[@paychannel="CREDITCARD"]/dd/div/div[4]/p',
                                          'Please enter 4 digits', 'SecurityCode为空校验')

            self.driver.find_element_by_xpath("//*[@placeholder='Security Code']").clear()
            self.driver.find_element_by_xpath("//*[@placeholder='Security Code']").send_keys("ddd")
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 激活校验
            selenium_assert.is_text_equal(self, '//*[@paychannel="CREDITCARD"]/dd/div/div[4]/p',
                                          "Please enter numbers only.", 'SecurityCode非纯数字校验')


            self.driver.find_element_by_xpath("//*[@placeholder='Security Code']").clear()
            self.driver.find_element_by_xpath("//*[@placeholder='Security Code']").send_keys("1111")
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 激活校验
            selenium_assert.isElementExist(self, '//*[@paychannel="CREDITCARD"]/dd/div/div[4]/p', 'SecurityCode长度正确校验')
            print("------------------------------------------------------------------")

            print("Cardholder校验：")
            selenium_assert.is_text_equal(self, '//*[@paychannel="CREDITCARD"]/dd/div/div[5]/p', "Please enter the card holder's name" ,'Cardholder为空校验')

            self.driver.find_element_by_xpath("//*[@placeholder='Card Holder']").send_keys("2")
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 激活校验
            selenium_assert.is_text_equal(self, '//*[@paychannel="CREDITCARD"]/dd/div/div[5]/p', "Card holder's name can't be numeric.", 'Cardholder纯数字错误校验')

            self.driver.find_element_by_xpath("//*[@placeholder='Card Holder']").send_keys("2s")
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 激活校验
            selenium_assert.isElementExist(self, '//*[@paychannel="CREDITCARD"]/dd/div/div[5]/p', 'Cardholder填写正确校验')
            sleep(1)

        except Exception as msg:
            print(u"异常原因%s" % msg)
            self.add_img()
            raise





# if __name__ == "__main__":
#     GBBaseCase.main()


