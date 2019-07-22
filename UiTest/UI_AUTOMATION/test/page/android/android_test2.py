import os
import unittest
# from Util import Util
from appium import webdriver
from time import sleep
import warnings
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class BaTest(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)   # 取消Warning警告

        # 设置运行参数
        capabilities = {}
        capabilities['deviceName'] = '192.168.33.102:5555'
        capabilities['platformName'] = 'Android'
        capabilities['platformVersion'] = '7.0.0'
        capabilities['noReset'] = True   #取消每次都重新安装app

        capabilities['appPackage'] = 'com.globalegrow.app.gearbest'
        capabilities['appActivity'] = 'com.globalegrow.app.gearbest.SplashActivity'
        capabilities['app'] = r'C:/Users/jiangjiahao/Desktop/gearbest_v4.9.0_develop.apk'
        capabilities['unicodeKeyboard'] = 'True'
        capabilities['resetKeyboard'] = 'True'
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
        self.driver = driver
        self.LIST_LATIN = "adb shell ime set com.android.inputmethod.latin/.LatinIME"
        self.LIST_APPIUM = "adb shell ime set io.appium.android.ime/.UnicodeIME"

    def test_login(self):
        print("登陆：")
        sleep(10)
        ### 切换环境
        # self.driver.find_element_by_id("android:id/button1").click()  # 确认生效
        # sleep(3)
        # self.driver.find_element_by_xpath("//*[@text='GearBest']").click()
        # sleep(5)
        # self.driver.find_element_by_id(
        #     "com.globalegrow.app.gearbest:id/iv_category").click()  # choose your favorate categories
        # self.driver.find_element_by_id("com.globalegrow.app.gearbest:id/confirm_edit_bt").click()
        # try:
        #     self.driver.find_element_by_id("com.globalegrow.app.gearbest:id/sdl__negative_button").click()
        # except:
        #     pass

        self.driver.find_element_by_xpath("//*[@text='Account']").click()
        self.driver.find_element_by_id("com.globalegrow.app.gearbest:id/tv_sign_in").click()
        # sleep(1)
        # # 切换输入法
        # os.system(self.LIST_LATIN)
        self.driver.find_element_by_id("com.globalegrow.app.gearbest:id/et_login_username").send_keys("583241254@qq.com")
        sleep(1)
        self.driver.find_element_by_id("com.globalegrow.app.gearbest:id/et_login_password").click()
        sleep(1)
        self.driver.find_element_by_id("com.globalegrow.app.gearbest:id/et_login_password").send_keys("abc456456")
        self.driver.find_element_by_id("com.globalegrow.app.gearbest:id/btn_login").click()
        # # 切换输入法
        # os.system(self.LIST_APPIUM)
        sleep(3)
        print("over")

    def test_bug(self):
        print("商品购买：")












    # def tearDown(self):
    #     self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(BaTest)
    unittest.TextTestRunner(verbosity=2).run(suite)    ## verbosity=2 测试结果的输出详细













