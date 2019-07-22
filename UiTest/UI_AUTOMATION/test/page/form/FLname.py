from selenium.common.exceptions import TimeoutException
import selenium.webdriver.support.expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from UI_AUTOMATION.test.page.pageconfig.connect import GBConnect
import random
import string
import sys
import os

# class Logger(object):
#   def __init__(self, filename="Default.log"):
#     self.terminal = sys.stdout
#     self.log = open(filename, "a")
#   def write(self, message):
#     self.terminal.write(message)
#     self.log.write(message)
#   def flush(self):
#     pass

# path = os.path.abspath(os.path.dirname(__file__))
# type = sys.getfilesystemencoding()
# sys.stdout = Logger('a.txt')

url = GBConnect().GB_payurl()
print(url)
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

driver.refresh()
sleep(0.5)
##----------------------------------------------------------------------------------------------------
#creditcard:
def FLname_creditcard():
    print("----------------------------------------------------------------------------------------------------")
    print("FLname_creditcard")
    global src, Firstname, LastName, Firstnameerror, Lastnameerror
    src = '//*[@src="https://uidesign.zafcdn.com/ZF/image/z_promo/20190418_9281/discover.png"]'
    Firstname = "//*[@placeholder='First name']"
    LastName = "//*[@placeholder='Last Name']"
    Firstnameerror = "//*[@placeholder='First name']/../../p"
    Lastnameerror = "//*[@placeholder='First name']/../../p"
    sleep(0.5)
    driver.find_element_by_xpath(src).click()
    sleep(0.5)
    # driver.find_element_by_xpath("//*[@class='credit_editAddress']").click()
    sleep(0.5)
    i = 300
    while 1:
        try:
            driver.find_element_by_xpath(src).click()
            break
        except:
            print(i)
            driver.execute_script("var q=document.body.scrollTop=%s" % i)
            i = i + 300
            sleep(0.2)
            if i > 4000:
                i = 0
    sleep(0.5)
    try:
        driver.find_element_by_xpath("//*[@class='credit_editAddress']").click()
    except:
        pass
# ------------------------------------------------------------------------------------------------------------------------
#墨西哥分期:
def FLname_EBX_MXCC():
    print("----------------------------------------------------------------------------------------------------")
    print("FLname_EBX_MXCC")
    global src, Firstname, LastName, Firstnameerror, Lastnameerror
    src = '//*[@src="https://uidesign.gbtcdn.com/GB/image/z_promo/20190516_9912/MasterCard_debit.png"]'
    Firstname = "//*[@placeholder='Nombre']"
    LastName = "//*[@placeholder='Apellido']"
    Firstnameerror = Firstname + "/../../p"
    Lastnameerror = LastName + "/../../p"
    sleep(0.5)
    driver.find_element_by_xpath(src).click()
    sleep(0.5)
    # driver.find_element_by_xpath("//*[@class='credit_editAddress']").click()
    sleep(0.5)
    i = 300
    while 1:
        try:
            driver.find_element_by_xpath(src).click()
            break
        except:
            print(i)
            driver.execute_script("var q=document.body.scrollTop=%s" % i)
            i = i + 300
            sleep(0.2)
            if i > 4000:
                i = 0
    sleep(0.5)
    try:
        driver.find_element_by_xpath("//*[@class='credit_editAddress']").click()
    except:
        pass

# ------------------------------------------------------------------------------------------------------------------------
#巴西分期:
def FLname_ebanxinstalment():
    print("----------------------------------------------------------------------------------------------------")
    print("FLname_ebanxinstalment")
    global src, Firstname, LastName, Firstnameerror, Lastnameerror
    src = '//*[@src="https://uidesign.zafcdn.com/ZF/image/z_promo/20190418_9281/elo.png"]'
    Firstname = "//*[@placeholder='Primeiro nome']"
    LastName = "//*[@placeholder='Sobrenome']"
    Firstnameerror = "//*[@placeholder='Primeiro nome']/../../p"
    Lastnameerror = "//*[@placeholder='Sobrenome']/../../p"
    sleep(0.5)
    driver.find_element_by_xpath(src).click()
    sleep(0.5)
    # driver.find_element_by_xpath("//*[@class='credit_editAddress']").click()
    sleep(0.5)
    i = 300
    while 1:
        try:
            driver.find_element_by_xpath(src).click()
            break
        except:
            print(i)
            driver.execute_script("var q=document.body.scrollTop=%s" % i)
            i = i + 300
            sleep(0.2)
            if i > 4000:
                i = 0
    sleep(0.5)
    try:
        driver.find_element_by_xpath("//*[@class='credit_editAddress']").click()
    except:
        pass

# ------------------------------------------------------------------------------------------------------------------------
#boleto
def FLname_boleto():
    print("----------------------------------------------------------------------------------------------------")
    print("FLname_boleto")
    global src, Firstname, LastName, Firstnameerror, Lastnameerror
    src = '//*[@src="https://uidesign.gbtcdn.com/check_out/beloto.png"]'
    Firstname = "//*[@placeholder='Primeiro nome']"
    LastName = "//*[@placeholder='Sobrenome']"
    Firstnameerror = "//*[@placeholder='Primeiro nome']/../../p"
    Lastnameerror = "//*[@placeholder='Sobrenome']/../../p"
    sleep(0.5)
    i = 300
    while 1:
        try:
            driver.find_element_by_xpath(src).click()
            break
        except:
            print(i)
            driver.execute_script("var q=document.body.scrollTop=%s" % i)
            i = i + 300
            sleep(0.2)
            if i > 4000:
                i = 0
    sleep(0.5)
    try:
        driver.find_element_by_xpath("//*[@class='credit_editAddress']").click()
    except:
        pass
# ------------------------------------------------------------------------------------------------------------------------
#BEBC分期:
def FLname_BEBC():
    print("----------------------------------------------------------------------------------------------------")
    print("FLname_BEBC")
    global src, Firstname, LastName, Firstnameerror, Lastnameerror
    src = '//*[@src="https://uidesign.gbtcdn.com/check_out/Bancontact_b.png"]'
    Firstname = "//*[@placeholder='First name']"
    LastName = "//*[@placeholder='Last Name']"
    Firstnameerror = Firstname + "/../../p"
    Lastnameerror = LastName + "/../../p"
    sleep(0.5)
    i = 300
    while 1:
        try:
            driver.find_element_by_xpath(src).click()
            break
        except:
            print(i)
            driver.execute_script("var q=document.body.scrollTop=%s" % i)
            i = i + 300
            sleep(0.2)
            if i > 4000:
                i = 0
    sleep(0.5)
    try:
        driver.find_element_by_xpath("//*[@class='credit_editAddress']").click()
    except:
        pass

##------------------------------------------------------------------------------------------------------------------------
def FLname_PSE():
    print("----------------------------------------------------------------------------------------------------")
    print("FLname_PSE")
    global src, Firstname, LastName, Firstnameerror, Lastnameerror
    src = '//*[@src="http://www.wearesellers.com/uploads/answer/20170120/6d9cdbfcc224e1fc7dec9d401c5abbfd.jpg"]'
    Firstname = "//*[@placeholder='Nombre']"
    LastName = "//*[@placeholder='Apellido']"
    Firstnameerror = Firstname + "/../../p"
    Lastnameerror = LastName + "/../../p"
    sleep(0.5)
    i = 300
    while 1:
        try:
            driver.find_element_by_xpath(src).click()
            break
        except:
            print(i)
            driver.execute_script("var q=document.body.scrollTop=%s" % i)
            i = i + 300
            sleep(0.2)
            if i > 4000:
                i = 0
    sleep(0.5)
    try:
        driver.find_element_by_xpath("//*[@class='credit_editAddress']").click()
    except:
        pass


## ------------------------------------------------------------------------------------------------------------------------
#TRCC分期:
def FLname_TRCC():
    print("----------------------------------------------------------------------------------------------------")
    print("FLname_TRCC")
    global src, Firstname, LastName, Firstnameerror, Lastnameerror
    src = '//*[@src="https://uidesign.gbtcdn.com/GB/images/others/tr_installment_logo.png"]'
    Firstname = "//*[@placeholder='First name']"
    LastName = "//*[@placeholder='Last Name']"
    Firstnameerror = Firstname + "/../../p"
    Lastnameerror = LastName + "/../../p"
    sleep(0.5)
    i = 300
    while 1:
        try:
            driver.find_element_by_xpath(src).click()
            break
        except:
            print(i)
            driver.execute_script("var q=document.body.scrollTop=%s" % i)
            i = i + 300
            sleep(0.2)
            if i > 4000:
                i = 0
    sleep(0.5)
    try:
        driver.find_element_by_xpath("//*[@class='credit_editAddress']").click()
    except:
        pass


def run():
    # FLname_PSE()
    # FLname_boleto()
    strs = ['FLname_creditcard','FLname_EBX_MXCC','FLname_ebanxinstalment','FLname_boleto','FLname_BEBC','FLname_PSE', 'FLname_TRCC']
    for s in strs:
        globals().get(s)()
        # pass

        # 代码 校验执行脚本
        # a = "-., / @& !+:"
        a = "~ ` # $ % ^ * ( ) = [ ] { } \ | ‘ “ ; < >  - ' . , / @ & ! + :"
        a = a.replace(' ', '')
        x = len(a)
        # print(x)
        for i in range(x):
            # b = "h" + a[i]+''.join(random.sample(string.ascii_letters + string.digits, 8))
            b = a[i]+''.join(random.sample(string.ascii_letters, 8))
            driver.find_element_by_xpath(Firstname).clear()
            driver.find_element_by_xpath(Firstname).clear()
            driver.find_element_by_xpath(Firstname).send_keys(b)
            driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()
            sleep(0.3)
            c = driver.find_element_by_xpath(Firstnameerror).text
            # if c ==
            print("Firstname输入: %s ====》 校验结果: %s" % (b, c))
            driver.find_element_by_xpath(LastName).clear()
            driver.find_element_by_xpath(LastName).clear()
            driver.find_element_by_xpath(LastName).send_keys(b)
            driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()
            sleep(0.3)
            d = driver.find_element_by_xpath(Lastnameerror).text
            print("Lastname输入: %s ====》 校验结果: %s" % (b, d))
            print("Lastname输入: %s ====》 校验结果: " %d)
            sleep(0.3)

run()


