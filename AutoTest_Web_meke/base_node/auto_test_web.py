'''
@Description: python
@Version: 1.0
@Autor: liuhua
@QQ: 434375025@qq.com
@Link: https://github.com/choly1985
@Date: 2019-10-21 16:37:57
@LastEditors: liuhua
'''
from read_init import read_ini
from selenium import webdriver
import time
import os
import sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

sys.path.append(
    r'F:\Src\LearningPython\AutoTest_Web_meke\base_node\read_init.py')


class AutoTestBase(object):
    def __init__(self, browser):
        self.driver = self.open_browser(browser)

    def open_browser(self, browser):
        if browser == 'chrome':
            driver = webdriver.Chrome(
                'D:\Program Files\python\Scripts\chromedriver.exe')
        elif browser == 'firefox':
            driver = webdriver.Firefox()
        elif browser == 'ie':
            driver = webdriver.Ie()
        else:
            driver == webdriver.Edge()
        return driver

    def sleep(self, second=0.5):
        time.sleep(second)

    def handle_windows(self, *args):
        value = len(args)
        if value == 1:
            if args[0] == 'max':
                self.driver.maximize_window()
            elif args[0] == 'min':
                self.driver.minimize_window()
            elif args[0] == 'back':
                self.driver.back()
            elif args[0] == 'go':
                self.driver.forward()
            else:
                self.driver.refresh()
        elif value == 2:
            self.driver.set_window_size(args[0], args[1])
        else:
            print("你传递的参数有问题")

    def get_url(self, url):
        if self.driver != None:
            time.sleep(1)
            self.driver.maximize_window()
            if 'http://' in url:
                self.driver.get(url)
            elif 'https://' in url:
                self.driver.get(url)
            else:
                print('你输入的url有问题，请检查！')

    def open_url_is_true(self, url, title_name=None):
        '''
            通过title判断页面是否正确
        '''
        self.get_url(url)
        return self.asser_title(title_name)

    def asser_title(self, title_name=None):
        '''
            判断title是否正确
        '''
        if title_name != None:
            get_title = EC.title_contains(title_name)
            return get_title(self.driver)

    def refresh_f5(self):
        '''
            强制刷新
        '''
        pass

    def save_png(self):
        '''
            保存图片
        '''
        now_time = time.strftime('%Y%m%d-%H%M%S')
        file_path = os.getcwd() + '\\' + now_time
        print(file_path)
        self.driver.get_screenshot_as_file('{}.png'.format(file_path))

    def close_browser(self):
        self.driver.close()

    def quit_browser(self):
        self.driver.quit()

    def get_local_element(self, info):
        # [namee,email]
        """
            读取本地配置文件获取数据
        """
        data = read_ini.get_value(info)
        data_info = data.split('>')
        return data_info

    def get_element(self):
        '''
            获取元素element
            @parame by 定位元素的方式
            @parame value 定位置
            @return element 返回一个元素
        '''
        by, value = selef.get_element(info)
        element = None
        if by == 'id':
            element = self.driver.find_element_by_id(value)
        elif by == 'name':
            element = self.driver.find_element_by_name(value)
        elif by == 'css':
            element = self.driver.find_element_by_css_selector(value)
        elif by == 'class':
            element = self.driver.find_element_by_class_name(value)
        # else:
        #     element = self.driver.find_element_by_xpath(value)
        return element
