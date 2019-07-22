from UI_AUTOMATION.utils.config import Config
from selenium.webdriver.support.ui import Select
from ..base_page import *

import pymysql
from UI_AUTOMATION.test.page.pageconfig.haoselenium import *


class GBFormCase(selenium_wait, BasePage):

    def __init__(self, driver):

        self.Connection = 'keep-alive'
        self.driver = driver


    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True


    def test_formtest_creditcard(self):
        self.is_clickable("//*[@class='placeOrder btn block toPayBtn']")
        print(self.driver.current_url)
        sleep(0.5)
        self.driver.find_element_by_xpath('//*[@class="m_payTitle"]').click()
        print("1111111111")
        self.driver.find_element_by_xpath('//*[@src="https://uidesign.zafcdn.com/ZF/image/z_promo/20190418_9281/discover.png"]').click()
        sleep(1)
        print("------------------------------------------------------------------")
        print("billing address元素个数校验：")
        self.driver.find_element_by_xpath('//*[@class="credit_editAddress"]').click()
        sleep(1)
        num = len(self.driver.find_elements_by_xpath("//*[@class='credit_editForm']/div"))
        n = 10
        if num == 10:
            print("billing address元素%d个校验通过" %n)
        else:
            print("billing address元素%d个校验不通过，请检查！！！！！！！！！！！" %n)

        print("------------------------------------------------------------------")
        try:
            sleep(0.5)
            self.driver.find_element_by_xpath('//*[@src="https://uidesign.gbtcdn.com/GB/images/others/check_out/57x35/discover.png?imbypass=true"]').click()
            sleep(0.5)
            print("Card numbers校验：")
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 激活校验
            sleep(0.5)
            self.is_text_equal('//*[@curchannel="CREDITCARD"]/div[1]/div/p', 'Please enter your card number.', 'Card numbers为空校验')

            self.form_input("//*[@placeholder='Card Number']", "1234567890")
            self.is_text_equal('//*[@curchannel="CREDITCARD"]/div[1]/div/p', 'Card numbers must contain between 12 and 20 numerical characters.' ,'Card numbers长度校验')

            self.form_input("//*[@placeholder='Card Number']", "123456789012")
            self.is_text_equal('//*[@curchannel="CREDITCARD"]/div[1]/div/p',
                                          'Invalid card numbers. Please kindly make sure that your card numbers are correct.',
                                          'Card numbers无效卡校验')

            self.form_input("//*[@placeholder='Card Number']", "6011111111111117")
            self.isElementExist('//*[@curchannel="CREDITCARD"]/div[1]/div/p', 'Card numbers有效卡校验')
            print("------------------------------------------------------------------")


            print("date校验：")
            sleep(0.3)
            self.form_activation()  # 激活校验

            Select(self.driver.find_element_by_xpath('//*[@curchannel="CREDITCARD"]/div[2]/div/select')).select_by_value("1")  ## 实例化Select 月份
            # sleep(0.3)
            Select(self.driver.find_element_by_xpath('//*[@curchannel="CREDITCARD"]/div[3]/div/select')).select_by_value("2019")  # 实例化Select 年份
            self.form_activation() # 激活校验
            self.is_text_equal('//*[@paychannel="CREDITCARD"]/dd/div/div[2]/p', "Expiry Month' and 'Expiry Year' together must be a date in the future.", 'date小于今日校验')

            Select(self.driver.find_element_by_xpath('//*[@curchannel="CREDITCARD"]/div[3]/div/select')).select_by_value("2022")  # 实例化Select 年份
            self.form_activation() # 激活校验
            self.isElementExist('//*[@paychannel="CREDITCARD"]/dd/div/div[2]/p', 'date正常填写校验')
            print("------------------------------------------------------------------")

            print("非Am卡——SecurityCode校验:")
            self.is_text_equal('//*[@paychannel="CREDITCARD"]/dd/div/div[4]/p', 'Please enter the Security Code.' ,'SecurityCode为空校验')

            self.form_input("//*[@placeholder='Security Code']", "ddd")
            self.is_text_equal('//*[@paychannel="CREDITCARD"]/dd/div/div[4]/p', "Please enter numbers only.",'SecurityCode非纯数字校验')

            self.form_input("//*[@placeholder='Security Code']", "11")
            self.is_text_equal('//*[@paychannel="CREDITCARD"]/dd/div/div[4]/p', 'Please enter 3 digits' ,'SecurityCode长度不够校验')

            self.form_input("//*[@placeholder='Security Code']", "111")
            self.isElementExist('//*[@paychannel="CREDITCARD"]/dd/div/div[4]/p', 'SecurityCode长度正确校验')

            print("Am卡——SecurityCode校验:")
            # self.driver.find_element_by_xpath("//*[@src='https://uidesign.gbtcdn.com/GB/images/others/check_out/57x35/american-express.png?imbypass=true").click()
            # self.driver.find_element_by_xpath("//*[@src='https://uidesign.gbtcdn.com/GB/images/others/check_out/57x35/jcb.png?imbypass=true']/../../em[5]/img").click()

            self.form_input("//*[@placeholder='Card Number']", "37000000000007")
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 激活校验
            self.is_text_equal('//*[@paychannel="CREDITCARD"]/dd/div/div[4]/p',
                                          'Please enter 4 digits', 'SecurityCode为空校验')

            self.form_input("//*[@placeholder='Security Code']", "ddd")
            self.is_text_equal('//*[@paychannel="CREDITCARD"]/dd/div/div[4]/p',
                                          "Please enter numbers only.", 'SecurityCode非纯数字校验')

            self.form_input("//*[@placeholder='Security Code']", "1111")
            self.isElementExist('//*[@paychannel="CREDITCARD"]/dd/div/div[4]/p', 'SecurityCode长度正确校验')
            print("------------------------------------------------------------------")

            print("Cardholder校验：")
            # self.is_text_equal('//*[@paychannel="CREDITCARD"]/dd/div/div[5]/p', "Please enter the card holder's name" ,'Cardholder为空校验')

            self.form_input("//*[@placeholder='Card Holder']", "2")
            self.is_text_equal('//*[@paychannel="CREDITCARD"]/dd/div/div[5]/p', "Card holder's name can't be numeric.", 'Cardholder纯数字错误校验')

            self.form_input("//*[@placeholder='Card Holder']", "2|")
            self.is_text_equal('//*[@paychannel="CREDITCARD"]/dd/div/div[5]/p',
                                          "Card holder's name can't contain anyone of \/:*?\"<>|.", 'Cardholder特殊字符错误校验')

            self.form_input("//*[@placeholder='Card Holder']", "2s")
            self.isElementExist('//*[@paychannel="CREDITCARD"]/dd/div/div[5]/p', 'Cardholder填写正确校验')
            sleep(1)

        except Exception as msg:
            print(u"异常原因%s" % msg)
            self.save_screen_shot()
            raise

    def test_formtest_ebanxinstalment(self):
        self.is_clickable("//*[@class='placeOrder btn block toPayBtn']")
        print(self.driver.current_url)
        try:
            sleep(0.5)
            self.driver.execute_script("var q=document.body.scrollTop=5000")
            self.driver.find_element_by_xpath('//*[@src="https://uidesign.zafcdn.com/ZF/image/z_promo/20190418_9281/elo.png"]').click()
            sleep(1)
            print("ebanxinstalment巴西分期表单校验：")
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 激活校验
            sleep(0.5)
            print("CPF校验：")
            self.form_activation()  # 激活校验
            self.is_text_equal('//*[@curchannel="ebanxinstalment"]/div[2]/div[1]/p', 'Por favor entre com o número de CPF' ,'CPF为空校验')

            self.form_input("//*[@placeholder='CPF']", "hhhh()")
            self.is_text_equal('//*[@curchannel="ebanxinstalment"]/div[2]/div[1]/p',
                                          'Por favor insira apenas números',
                                          'CPF全字母错误校验')

            self.form_input("//*[@placeholder='CPF']", "1234567890")
            self.is_text_equal('//*[@curchannel="ebanxinstalment"]/div[2]/div[1]/p', 'CPF não pode ser menos de 11 dígitos' ,'CPF长度校验')

            self.form_input("//*[@placeholder='CPF']", "12345678901")
            self.isElementExist('//*[@curchannel="ebanxinstalment"]/div[2]/div[1]/p', 'CPF有效卡校验')

            print("número卡号校验：")
            self.is_text_equal('//*[@curchannel="ebanxinstalment"]/div[3]/p', 'Digite o número do seu cartão.' ,'número卡号为空校验')

            self.form_input("//*[@placeholder='Número de cartão']", "hhhh")
            self.is_text_equal('//*[@curchannel="ebanxinstalment"]/div[3]/p',
                                          'Use apenas números.',
                                          'número卡号全字母错误校验')

            self.form_input("//*[@placeholder='Número de cartão']", "1234567890")
            self.is_text_equal('//*[@curchannel="ebanxinstalment"]/div[3]/p', 'Os números dos cartões devem conter entre 12 e 20 caracteres numéricos.' ,'Card numbers长度校验')

            self.form_input("//*[@placeholder='Número de cartão']", "123456789012")
            self.is_text_equal('//*[@curchannel="ebanxinstalment"]/div[3]/p',
                                          'Números do cartão estão inválidos. Favor, certifique-se de que as informações do seu cartão estão corretas.',
                                          'Card numbers无效卡校验')

            self.form_input("//*[@placeholder='Número de cartão']", "6011111111111117")
            self.isElementExist('//*[@curchannel="ebanxinstalment"]/div[3]/p', 'Card numbers有效卡校验')
            print("------------------------------------------------------------------")

            print("date校验：")
            sleep(0.3)

            self.is_text_equal('//*[@curchannel="ebanxinstalment"]/div[4]/p', 'Selecione o prazo de validade do cartão.', 'date为空校验')
            Select(self.driver.find_element_by_xpath('//*[@name="expirationMonth"]')).select_by_value(
                "1")  ## 实例化Select 月份
            sleep(0.3)
            Select(self.driver.find_element_by_xpath('//*[@name="expirationYear"]')).select_by_value(
                "2019")  # 实例化Select 年份
            self.driver.find_element_by_xpath("//*[@id='content_wrap']").click()  # 激活校验
            self.is_text_equal('//*[@curchannel="ebanxinstalment"]/div[4]/p', "O prazo de vencimento eo ano devem ser uma data1 no futuro.", 'date小于今日校验')

            Select(self.driver.find_element_by_xpath('//*[@name="expirationYear"]')).select_by_value(
                "2022")  # 实例化Select 年份
            self.driver.find_element_by_xpath("//*[@id='content_wrap']").click()  # 激活校验
            self.isElementExist('//*[@curchannel="ebanxinstalment"]/div[4]/p', 'date正常填写校验')
            print("------------------------------------------------------------------")

            print("非Am卡——código de segurança安全码校验:")
            self.is_text_equal('//*[@curchannel="ebanxinstalment"]/div[6]/p', 'Favor insira o código de segurança' ,'código de segurança安全码为空校验')
            self.form_input("//*[@id='ebanxCvv']", "ddd")
            self.is_text_equal('//*[@curchannel="ebanxinstalment"]/div[6]/p', "Use apenas números.",'código de segurança安全码非纯数字校验')

            self.form_input("//*[@id='ebanxCvv']", "11")
            self.is_text_equal('//*[@curchannel="ebanxinstalment"]/div[6]/p', 'Digite 3 dígitos.' ,'código de segurança安全码长度不够校验')

            self.form_input("//*[@id='ebanxCvv']", "111")
            self.isElementExist('//*[@curchannel="ebanxinstalment"]/div[6]/p', 'código de segurança安全码长度正确校验')
            sleep(1)
            # js = "var q=document.getElementById('id').scrollTop=0"
            # driver.execute_script(js)
            print("Am卡——código de segurança校验:")
            # self.form_input("//*[@placeholder='Número de cartão']", "37000000000007")
            self.driver.find_element_by_xpath(
                '//*[@src="https://uidesign.gbtcdn.com/GB/images/others/check_out/57x35/elo.png?imbypass=true"]/../../em[4]/img').click()
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 激活校验
            sleep(0.3)
            self.is_text_equal('//*[@curchannel="ebanxinstalment"]/div[6]/p',
                                          'Digite 4 dígitos.', 'código de segurança长度校验')

            self.form_input("//*[@id='ebanxCvv']", "1111")
            self.isElementExist('//*[@curchannel="ebanxinstalment"]/div[6]/p', 'código de segurança长度正确校验')
            print("------------------------------------------------------------------")


            print("titular do cartão.卡主校验：")

            self.driver.find_element_by_xpath("//*[@placeholder='Titular do cartão']").clear()
            self.form_activation()
            self.is_text_equal('//*[@curchannel="ebanxinstalment"]/div[7]/p',
                                          "Digite o nome do titular do cartão.", 'titular do cartão.卡主为空校验')

            self.form_input("//*[@placeholder='Titular do cartão']", "2")
            self.is_text_equal('//*[@curchannel="ebanxinstalment"]/div[7]/p', "O nome do titular do cartão não pode ser números.", 'titular do cartão.卡主纯数字错误校验')
            self.form_input("//*[@placeholder='Titular do cartão']", "sd<")
            self.is_text_equal('//*[@curchannel="ebanxinstalment"]/div[7]/p', "O nome do titular do cartão não pode conter caracteres como V:*?\"<>I", 'titular do cartão.卡主特殊字符错误校验')
            self.form_input("//*[@placeholder='Titular do cartão']", "2s")
            self.isElementExist('//*[@curchannel="ebanxinstalment"]/div[7]/p', 'Cardholder填写正确校验')
            sleep(1)
        except Exception as msg:
            print(u"异常原因%s" % msg)
            self.save_screen_shot()
            raise


    def test_formtest_boleto(self):
        # self.is_clickable("//*[@class='placeOrder btn block toPayBtn']")
        print(self.driver.current_url)
        try:
            sleep(0.5)
            # driver.execute_script("var q=document.body.scrollTop=5000")
            self.driver.find_element_by_xpath(
                '//*[@src="https://uidesign.gbtcdn.com/check_out/beloto.png"]').click()
            sleep(0.5)
            print("boleto表单校验：")
            self.form_activation()
            sleep(0.5)
            print("CPF校验：")

            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 激活校验
            self.is_text_equal('//*[@curchannel="BOLETO"]/div[1]/div[1]/p',
                                          'Por favor entre com o número de CPF', 'CPF为空校验')

            self.form_input('//*[@curchannel="BOLETO"]/div[1]/div[1]/div/input[1]', "hhhh()")
            self.is_text_equal('//*[@curchannel="BOLETO"]/div[1]/div[1]/p',
                                          'Por favor insira apenas números',
                                          'CPF全字母错误校验')

            self.form_input('//*[@curchannel="BOLETO"]/div[1]/div[1]/div/input[1]', "1234567890")
            self.is_text_equal('//*[@curchannel="BOLETO"]/div[1]/div[1]/p',
                                          'CPF não pode ser menos de 11 dígitos', 'CPF长度校验')

            self.form_input('//*[@curchannel="BOLETO"]/div[1]/div[1]/div/input[1]', "12345678901")
            self.isElementExist('//*[@curchannel="BOLETO"]/div[1]/div[1]/p', 'CPF有效卡校验')
            sleep(0.5)
        except Exception as msg:
            print(u"异常原因%s" % msg)
            self.save_screen_shot()
            raise

    def test_formtest_ideal(self):
        self.is_clickable("//*[@class='placeOrder btn block toPayBtn']")
        print(self.driver.current_url)
        try:
            sleep(0.5)
            # driver.execute_script("var q=document.body.scrollTop=5000")
            self.driver.find_element_by_xpath(
                '//*[@src="https://icss1.gearbest.com/imagecache/GB2/images/domeimg/pay_method/ideal.png"]').click()
            sleep(0.5)
            print("ideal表单校验：")
            self.form_activation()
            sleep(0.5)
            print("ideal不选银行校验：")

            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 激活校验
            self.is_text_equal('//*[@curchannel="ideal"]/div/p',
                                          'Please select the issuing bank', 'ideal不选银行校验')

            print("ideal选银行校验：")
            Select(self.driver.find_element_by_xpath("//*[@name='IssueBank']")).select_by_value(
                "RABONL2U")
            self.form_activation()
            self.isElementExist('//*[@curchannel="ideal"]/div/p', 'ideal选银行校验')
            sleep(0.5)

        except Exception as msg:
            print(u"异常原因%s" % msg)
            self.save_screen_shot()
            raise


    def test_formtest_pse(self):
        self.is_clickable("//*[@class='placeOrder btn block toPayBtn']")
        print(self.driver.current_url)
        try:
            sleep(0.5)
            # driver.execute_script("var q=document.body.scrollTop=5000")
            self.driver.find_element_by_xpath(
                '//*[@src="http://www.wearesellers.com/uploads/answer/20170120/6d9cdbfcc224e1fc7dec9d401c5abbfd.jpg"]').click()
            sleep(0.5)
            print("pse表单校验：")
            self.form_activation()
            sleep(0.5)
            print("pse银行为空校验：")
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 激活校验
            self.is_text_equal('//*[@curchannel="PSE"]/div[1]/p[2]',
                                          'Por favor seleccione el Banco Emisor', 'pse银行为空校验')

            print("pse银行不为空校验：")
            Select(self.driver.find_element_by_xpath("//*[@name='pseBankCode']")).select_by_value(
                "banco_agrario")
            self.form_activation()
            self.isElementExist('//*[@curchannel="PSE"]/div[1]/p[2]', 'pse银行不为空校验')
            print("------------------------------------------------------------------")

            print("documento type为空校验：")
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 激活校验
            self.form_activation()
            sleep(0.3)
            self.is_text_equal('//*[@curchannel="PSE"]/div[2]/p', 'Por favor entre su documento', 'documento type为空校验')
            print("documento type不为空校验：")
            Select(self.driver.find_element_by_xpath('//*[@curchannel="PSE"]/div[2]/div/select')).select_by_value(
                "Cédula Ciudadana")
            self.form_activation()
            self.isElementExist('//*[@curchannel="PSE"]/div[2]/p', 'documento type不为空校验')
            print("------------------------------------------------------------------")

            print("documento 为空校验：")
            self.is_text_equal('//*[@curchannel="PSE"]/div[3]/p',
                                          'Por favor entre su documento', 'documento 为空校验')

            print("NIT (Número de Identificación Tributária)类型documento校验：")
            print("NIT (Número de Identificación Tributária)类型documento位数不够校验：")
            Select(self.driver.find_element_by_xpath('//*[@curchannel="PSE"]/div[2]/div/select')).select_by_value(
                "NIT (Número de Identificación Tributária)")
            self.form_input('//*[@curchannel="PSE"]/div[3]/div/input', "12345678")
            self.is_text_equal('//*[@curchannel="PSE"]/div[3]/p',
                                          'Por favor escriba de 9-10 digitos', 'NIT (Número de Identificación Tributária)类型documento位数不够校验')
            print("NIT (Número de Identificación Tributária)类型documento位数超过校验：")
            self.form_input('//*[@curchannel="PSE"]/div[3]/div/input', "12345678901")
            self.is_text_equal('//*[@curchannel="PSE"]/div[3]/p',
                                          'Por favor escriba de 9-10 digitos',
                                          'NIT (Número de Identificación Tributária)类型documento位数超过校验')
            print("NIT (Número de Identificación Tributária)类型document正确位数校验：")
            self.form_input('//*[@curchannel="PSE"]/div[3]/div/input', "1234567890")
            self.isElementExist('//*[@curchannel="PSE"]/div[3]/p','NIT (Número de Identificación Tributária)类型documento正确位数校验')

            print("Cédula Ciudadana类型documento位数不够校验：")
            Select(self.driver.find_element_by_xpath('//*[@curchannel="PSE"]/div[2]/div/select')).select_by_value(
                "Cédula Ciudadana")
            self.form_input('//*[@curchannel="PSE"]/div[3]/div/input', "1")
            self.is_text_equal('//*[@curchannel="PSE"]/div[3]/p',
                                          'Por favor escriba de 2-10 digitos',
                                          'Cédula Ciudadana类型documento位数不够校验')
            print("Cédula Ciudadana类型documento位数超过校验：")
            self.form_input('//*[@curchannel="PSE"]/div[3]/div/input', "12345678901")
            self.is_text_equal('//*[@curchannel="PSE"]/div[3]/p',
                                          'Por favor escriba de 2-10 digitos',
                                          'Cédula Ciudadana类型documento位数超过校验')
            print("Cédula Ciudadana类型document正确位数校验：")
            self.form_input('//*[@curchannel="PSE"]/div[3]/div/input', "12")
            self.isElementExist('//*[@curchannel="PSE"]/div[3]/p',
                                           'Cédula Ciudadana类型documento正确位数校验')


            print("Cédula de Extranjería类型documento位数超过校验：")
            Select(self.driver.find_element_by_xpath('//*[@curchannel="PSE"]/div[2]/div/select')).select_by_value(
                "Cédula de Extranjería")
            self.form_input('//*[@curchannel="PSE"]/div[3]/div/input', "12345678901")
            self.is_text_equal('//*[@curchannel="PSE"]/div[3]/p',
                                          'Por favor escriba de 1-6 digitos',
                                          'Cédula de Extranjería类型documento位数超过校验')
            print("Cédula de Extranjería类型document正确位数校验：")
            self.form_input('//*[@curchannel="PSE"]/div[3]/div/input', "1")
            self.isElementExist('//*[@curchannel="PSE"]/div[3]/p',
                                           'Cédula de Extranjería类型documento正确位数校验')


            Nombre = '//*[@curchannel="PSE"]/div[4]/div/input'
            Nombre_hnit = '//*[@curchannel="PSE"]/div[4]/p'
            Apellido = '//*[@curchannel="PSE"]/div[5]/div/input'
            Apellido_hnit = '//*[@curchannel="PSE"]/div[5]/p'
            Emaildirección = '//*[@curchannel="PSE"]/div[6]/div/input'
            Emaildirección_hnit = '//*[@curchannel="PSE"]/div[6]/p'
            NúmerodeTeléfono = '//*[@curchannel="PSE"]/div[7]/div/input'
            NúmerodeTeléfono_hnit = '//*[@curchannel="PSE"]/div[7]/p'
            # sleep(0.2)
            # self.driver.find_element_by_xpath(Nombre).clear()
            # sleep(0.3)
            # self.driver.find_element_by_xpath(Apellido).clear()
            # sleep(0.2)
            # self.driver.find_element_by_xpath(Emaildirección).clear()
            # sleep(0.2)
            # self.driver.find_element_by_xpath(NúmerodeTeléfono).clear()
            sleep(0.2)
            self.driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()  # 激活校验
            sleep(0.3)
            # print("Nombre为空校验：")
            # self.is_text_equal(Nombre_hnit, 'Por favor, introduzca su nombre de pila.', 'Nombre为空校验')
            print("Nombre非纯字母校验：")
            self.form_input(Nombre, "1a")
            self.is_text_equal(Nombre_hnit, 'Nombre inválido. Sólo se pueden introducir letras.', 'Nombre非纯字母校验')
            print("Nombre位数不够校验：")
            self.form_input(Nombre, "a")
            self.is_text_equal(Nombre_hnit, 'Por favor introduzca 2-32 carácteres.', 'Nombre位数不够校验')
            print("Nombre位数超过校验：")
            self.form_input(Nombre, "assjhfjshfkahfuishefuhasikuefhuiwshfukswahfe")
            self.is_text_equal(Nombre_hnit, 'Por favor introduzca 2-32 carácteres.',
                                          'Nombre位数超过校验')
            print("Nombre位数正确校验：")
            self.form_input(Nombre, "assjhfjsh")
            self.isElementExist(Nombre_hnit, 'Nombre位数正确校验')
            print("------------------------------------------------------------------")

            # print("Apellido为空校验：")
            # self.is_text_equal(Apellido_hnit, 'Por favor ingrese su apellido.', 'Apellido为空校验')
            print("Apellido非纯字母校验：")
            self.form_input(Apellido, "1a")
            self.is_text_equal(Apellido_hnit, 'Apellido inválido. Sólo se pueden introducir letras.',
                                          'Apellido非纯字母校验')
            print("Apellido位数不够校验：")
            self.form_input(Apellido, "a")
            self.is_text_equal(Apellido_hnit, 'Por favor introduzca 2-32 carácteres.',
                                          'Apellido位数不够校验')
            print("Apellido位数超过校验：")
            self.form_input(Apellido, "assjhfjshfkahfuishefuhasikuefhuiwshfukswahfe")
            self.is_text_equal(Apellido_hnit, 'Por favor introduzca 2-32 carácteres.',
                                          'Apellido位数超过校验')
            print("Apellido位数正确校验：")
            self.form_input(Apellido, "assjhfjsh")
            self.isElementExist(Apellido_hnit, 'Apellido位数正确校验')
            print("------------------------------------------------------------------")

            # print("Emaildirección为空校验：")
            # self.is_text_equal(Emaildirección_hnit, 'Por favor, introduzca su Dirección de E-mail.', 'Emaildirección为空校验')
            # print("Emaildirección非正确邮箱校验1：")
            self.form_input(Emaildirección, "583241254@")
            self.is_text_equal(Emaildirección_hnit, 'Por favor introduzca una dirección de correo válida.',
                                          'Emaildirección非正确邮箱校验1')
            print("Emaildirección非正确邮箱校验2：")
            self.form_input(Emaildirección, "583241254@qq.com.")
            self.is_text_equal(Emaildirección_hnit, 'Por favor introduzca una dirección de correo válida.',
                                          'Emaildirección非正确邮箱校验2')
            print("Emaildirección正确邮箱校验：")
            self.form_input(Emaildirección, "583241254@qq.com")
            self.isElementExist(Emaildirección_hnit, 'Emaildirección正确邮箱校验')
            print("------------------------------------------------------------------")

            # print("NúmerodeTeléfono为空校验：")
            # self.is_text_equal(NúmerodeTeléfono_hnit, 'Por favor, introduzca su Dirección de E-mail.', 'Emaildirección为空校验')
            print("NúmerodeTeléfono非正确电话号码校验1：")
            self.form_input(NúmerodeTeléfono, "`12")
            self.is_text_equal(NúmerodeTeléfono_hnit,
                                          'Por favor, ingrese un número de teléfono válido.',
                                          'NúmerodeTeléfono非正确电话号码校验1')
            print("NúmerodeTeléfono非正确电话号码校验2：")
            self.form_input(NúmerodeTeléfono, "-+123")
            self.is_text_equal(NúmerodeTeléfono_hnit,
                                          'Por favor, ingrese un número de teléfono válido.',
                                          'NúmerodeTeléfono非正确电话号码校验2')
            print("NúmerodeTeléfono非正确电话号码校验3：")
            self.form_input(NúmerodeTeléfono, "+12345678901234567890")
            self.is_text_equal(NúmerodeTeléfono_hnit,
                                          'Por favor, ingrese un número de teléfono válido.',
                                          'NúmerodeTeléfono非正确电话号码校验3')
            print("NúmerodeTeléfono正确电话号码校验：")
            self.form_input(NúmerodeTeléfono, "+123456")
            self.isElementExist(NúmerodeTeléfono_hnit, 'NúmerodeTeléfono正确电话号码校验')


            sleep(0.5)

        except Exception as msg:
            print(u"异常原因%s" % msg)
            self.save_screen_shot()
            raise


# if __name__ == "__main__":
#     GBFormCase.main()
    # GBFormCase.test_formtest_boleto

