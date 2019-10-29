'''
@Description: python
@Version: 1.0
@Autor: liuhua
@QQ: 434375025@qq.com
@Link: https://github.com/choly1985
@Date: 2019-10-10 17:07:07
@LastEditors: liuhua
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Page(object):
    log_url = 'http://www.126.com'

    def __init__(self, selenium_driver, base_url=log_url):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)

    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)


class LoginPage(Page):
    url = '/'
    username_loc = (By.ID, 'username')
    password_loc = (By.ID, 'password')
    submit_loc = (By.XPATH, '//*[@id="login_div"]/form/input[2]')

    def type_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    def submit(self):
        self.find_element(*self.submit_loc).click()


def test_user_login(driver, username, password):
    login_page = LoginPage(driver, 'http://user.hqygou.com/login/index/login/')
    login_page.open()
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.submit()


def main():
    try:
        driver = webdriver.Firefox()
        username = 'zhangwei'
        password = 'zhang1wei'
        test_user_login(driver, username, password)
        time.sleep(3)
        text = driver.find_element_by_xpath(
            "//*[@id='header']/div[2]/ul/li[1]/strong").text
        assert (text == u'张渭'), "用户名不匹配登录失败"
    finally:
        driver.close()


if __name__ == "__main__":
    # main()
    pass
    # from selenium.webdriver.common.keys import keys
    # from selenium.webdriver.common.action_chains import action_chains
