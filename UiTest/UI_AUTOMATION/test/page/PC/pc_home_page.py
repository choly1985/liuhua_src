from time import sleep
from UI_AUTOMATION.test.page.PC.pc_locators import *
from UI_AUTOMATION.test.page.base_page import BasePage


class PublicComponent(BasePage):
    pass


class LoginPage(BasePage):

    def login(self, email, pwd):
        self.send_keys(email, *LoginPageLoc.email)
        sleep(0.5)
        self.send_keys(pwd, *LoginPageLoc.password)
        sleep(0.5)
        self.click(*LoginPageLoc.sign_in)


class PaymentPage(BasePage):

    def Touch_Paybutton(self):

        self.click(*PaymentInfoPageLoc.pay_button)
        sleep(0.5)
        # self.is_element_exist(*PaymentInfoPageLoc.pay_currencyselect)
        print(self.is_element_exist(*PaymentInfoPageLoc.pay_currencyselect)(self.driver))
        if self.is_element_exist(*PaymentInfoPageLoc.pay_currencyselect)(self.driver):
            self.click(*PaymentInfoPageLoc.pay_currencyselect)
            self.click(*PaymentInfoPageLoc.pay_currencyconfirm)
            sleep(0.5)
            self.click(*PaymentInfoPageLoc.pay_button)





class HomePage(BasePage):

    def visit_gb(self, url):
        self.get(url)

    def sign_in(self):
        self.click(*HomePageLoc.sign_in)
        sleep(2)

    def logout(self):
        self.move_to_element(*HomePageLoc.user_info)
        sleep(0.5)
        self.click(*HomePageLoc.logout)
        sleep(2)

    def close_pop_win(self):
        if self.find_element(*HomePageLoc.new_user_pop):
            self.click(*HomePageLoc.close_pop)












