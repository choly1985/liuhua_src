import random
from selenium import webdriver
from time import sleep
from UI_AUTOMATION.test.page.pageconfig.connect import *

driver = webdriver.Chrome()
driver.get(GBConnect().ZF_payurl())
driver.maximize_window()
driver.refresh()
sleep(0.5)

class CPF():
    def baxicpf(cpf):
        # driver = webdriver.Chrome()
        # driver.get("https://ceshi.zaful.net/?token=O190328013624162046MOR&lang=en")
        # driver.maximize_window()
        # driver.refresh()
        # sleep(0.5)
        #巴西分期:
        src = '//*[@src="https://uidesign.gbtcdn.com/GB/images/others/check_out/57x35/Hipercard.png?imbypass=true"]'
        CPF = "//*[@placeholder='CPF']"
        CPFerror = CPF + "/../../p"
        sleep(0.5)
        driver.find_element_by_xpath(src).click()
        while 1:
            try:
                driver.find_element_by_xpath(src).click()
                break
            except:
                driver.execute_script("var q=document.body.scrollTop=300")
                sleep(0.2)
                driver.find_element_by_xpath(src).click()
        sleep(0.2)
        driver.find_element_by_xpath(CPF).clear()
        driver.find_element_by_xpath(CPF).clear()
        driver.find_element_by_xpath(CPF).send_keys(cpf)
        driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()
        sleep(0.2)
        c = driver.find_element_by_xpath(CPFerror).text
        print("巴西分期CPF输入[%s] =======>> 校验结果: %s" % (cpf, c))

    # @boletocpf
    def boletocpf(cpf):
        #boleto:
        src = '//*[@src="https://icss1.gearbest.com/imagecache/GB2/images/boleto3.jpg"]'
        CPF = "//*[@placeholder='CPF']"
        CPFerror = CPF + "/../../p"
        sleep(0.5)
        driver.find_element_by_xpath(src).click()
        while 1:
            try:
                driver.find_element_by_xpath(src).click()
                break
            except:
                driver.execute_script("var q=document.body.scrollTop=300")
                sleep(0.2)
                driver.find_element_by_xpath(src).click()
        sleep(0.2)
        driver.find_element_by_xpath(CPF).clear()
        driver.find_element_by_xpath(CPF).clear()
        driver.find_element_by_xpath(CPF).send_keys(cpf)
        driver.find_element_by_xpath("//*[@class='placeOrder btn block toPayBtn']").click()
        sleep(0.2)
        c = driver.find_element_by_xpath(CPFerror).text
        print("boileto CPF输入[%s] =======>> 校验结果: %s" % (cpf, c))

def run():
    i = 0
    while 1:
        cpf = "".join(random.choice("0123456789") for i in range(11))
        # cpf = '38518065305'
        print(type(cpf), cpf)
        j = (int(cpf[0])*10 + 9*int(cpf[1]) + 8*int(cpf[2]) + 7*int(cpf[3]) + 6*int(cpf[4]) + 5*int(cpf[5]) + 4*int(cpf[6]) + 3*int(cpf[7]) + 2*int(cpf[8]))%11
        print(j)
        if j == 0 or j == 1:
            j = 0
        else:
            j = 11 - j
        print("最终", j)
        newcpf = list(cpf)
        newcpf[9] = str(j)
        # print(newcpf)
        cpf = "".join(newcpf)
        k = (int(cpf[0])*11 + 10*int(cpf[1]) + 9*int(cpf[2]) + 8*int(cpf[3]) + 7*int(cpf[4]) + 6*int(cpf[5]) + 5*int(cpf[6]) + 4*int(cpf[7]) + 3*int(cpf[8]) + 2*int(cpf[9]))%11
        print(k)
        if k == 0 or k == 1:
            k = 0
        else:
            k = 11 - k
        print("最终", k)
        newcpf = list(cpf)
        # newcpf[9] = str(j)
        newcpf[10] = str(k)
        newcpf = ''.join(newcpf)
        print("上面CPF合法应是：", newcpf)
        print("---------------------------------")

        if cpf[9] == str(j) and cpf[10] == str(k):
            print("合法的CPF：", cpf)
            print("尝试[%i]次后成功" %i)
            strs = ['baxicpf','boletocpf']
            # for s in strs:
            #     globals().get(s)(cpf)
            CPF.boletocpf(cpf)
            break
        else:
            strs = ['baxicpf', 'boletocpf']
            # for s in strs:
            #     globals().get(s)(cpf)
            CPF.boletocpf(cpf)
            i += 1


run()




















