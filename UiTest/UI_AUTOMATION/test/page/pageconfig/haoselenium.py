from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait



class selenium_wait:


    def __init__(self, driver):
        self.driver = driver


    # 一直等待某元素可见，默认超时10秒
    def is_clickable(self, xpath, timeout=5):
        try:
            ui.WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            return True
        except TimeoutException:
            return False

    def is_element(self, element):
        if self.driver.find_element_by_xpath(element):
            return True
        else:
            return False
        # self.driver.implicitly_wait(20)

    def is_element_exist(self, xpath):
        s = self.driver.find_element_by_xpath(xpath)
        if len(s) == 0:
            print("元素未找到:%s" % xpath)
            return False
        elif len(s) == 1:
            return True
        # else:
        #     print("找到%s个元素：%s" % (len(s), xpath))
        #     return False

    def is_title_should_contains(self, title, timeout=10):

        try:
            ui.WebDriverWait(self.driver, timeout).until(EC.title_contains(title))
            # ui.WebDriverWait(self.driver, timeout).until(self.assertTrue(EC.title_contains(title)(xpath)))
            return True
        except TimeoutException:
            return False
    # self.assertTrue(EC.title_contains(u'百度')(dr))

    def test_visibility_of(self, xpath):
        search_text_field = self.driver.find_element_by_xpath(xpath)
        search_text_field_should_visible = EC.visibility_of(search_text_field)
        print(search_text_field_should_visible(self.driver))
        self.assertTrue(search_text_field_should_visible('False'))

# class selenium_assert:
#     def __init__(self, driver):
#         self.driver = driver

    def is_text_should_contains(self, xpath1, locator, timeout=10):
        # sleep(1)
        try:
            ui.WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element((By.XPATH, xpath1), locator))
            # ((By.CLASS_NAME, 'noBottom paymentsHeader alpha'), 'locator')
            return True
            a = "yes"
        except TimeoutException:
            return False
            self.driver.get_screenshot_as_base64()
            a = "no"
        return a
        print(a)

    def is_text_equal(self, xpath, text, Description, timeout=3):
        sleep(0.3)
        try:
            ui.WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            locator = ("xpath", xpath)
            text = text
            a = EC.text_to_be_present_in_element(locator, text)(self.driver)
            if a == True:
                print(a, "【%s】:校验通过"%Description)
            else:
                print(a, "【%s】:校验失败请检查"%Description)
                self.driver.get_screenshot_as_base64()
        except TimeoutException:
            self.driver.get_screenshot_as_base64()
            print("超时，请检查环境是否异常")
        sleep(0.2)


    def isElementExist(self, xpath, Description):
        # flag = True
        sleep(0.3)
        a = self.driver.find_element_by_xpath(xpath).text
        # return flag
        if a == '':
            print("True", "【%s】:校验通过" % Description)
        else:
            print("False", "【%s】:校验失败请检查" % Description)
        sleep(0.2)


# class form_test:
    global xpath_activation
    xpath_activation = "//*[@class='pc_orderinf']"

    # def __init__(self, driver):
    #     self.driver = driver

    def form_activation(self):
        self.driver.find_element_by_xpath(xpath_activation).click()  # 激活校验
        sleep(0.5)

    def form_input(self, xpath, send_keys):      #第一个参数xpath：输入的位置，第二个参数send_key：输入的内容
        self.driver.find_element_by_xpath(xpath).clear()
        self.driver.find_element_by_xpath(xpath).send_keys(send_keys)
        sleep(0.2)
        self.driver.find_element_by_xpath(xpath_activation).click()  # 激活校验
        sleep(0.3)
    # def from_check(self, xpath, hintword, hnitresult, ):     #
    #     selenium_assert.is_text_equal(self, xpath, hintword, hnitresult)














